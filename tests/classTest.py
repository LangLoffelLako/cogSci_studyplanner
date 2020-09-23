"""The Unittest for the classes "unit", "course" and "module". It tests the creation of the class, the setters and
getters if defined and the functions

To-Do:
Add testclass for the functionality of the classes.
"""

import unittest
from cls.classes import Module, Collector, Course


class BasicClassTest(unittest.TestCase):
    """Test for the Creation and variables of the classes"""

    def setUp(self) -> None:

        self.testModule = Module('test unit', code='123456')
        self.testCourse = Course('test course', code='123456', semester='WS20', init_credits=5)
        self.testCollector = Collector('test module', code='123456', required_credits=16)

    def tearDown(self) -> None:
        pass

    def testClassCreations(self):
        """tests the initiation of the classes in classes.py
        It tests that well defined instances are created
        when called with appropriate parameters"""

        #Module classes are initiated
        testUnit = Module('test unit')
        self.assertIsInstance(testUnit, Module)
        testUnit = Module('test unit', '1548hnn')
        self.assertIsInstance(testUnit, Module)
        testUnit = Module(name='test unit', code='1548hnn')
        self.assertIsInstance(testUnit, Module)

        #Course classes are initiated
        testCourse = Course('test course')
        self.assertIsInstance(testCourse, Course)
        testCourse = Course('test course', '123456', 5, 'WS20')
        self.assertIsInstance(testCourse, Course)
        testCourse = Course(name='test course', code='123456', semester='WS20', init_credits=5)
        self.assertIsInstance(testCourse, Course)

        #Collector classes are initiated
        testCollector = Collector('test module')
        self.assertIsInstance(testCollector, Collector)
        testCollector = Collector('test module', '123456', 16)
        self.assertIsInstance(testCollector, Collector)
        testCollector = Collector(name='test module', code='123456', required_credits=16)
        self.assertIsInstance(testCollector, Collector)

    def testClassPropertyGrades(self):
        """Tests the grad setters and getters functions of the classes in classes.py
        it tests, that the setters only set the property if provided with appropriate values
        and raises an error for inappropriate values"""

        # data for the unit class grad setter
        unitGradesPass = [None, 5, 51.5, 0, '1.5']
        unitGradesTypeError = [[1, 5]]
        unitGradesValueError = ['testString', -2, 456]

        # appropriate values
        for testGrade in unitGradesPass:
            self.testModule.grade = testGrade
            if testGrade is None:
                self.assertEqual(self.testModule.grade, testGrade)
            else:
                testGrade = float(testGrade)
                if testGrade < 1:
                    self.assertEqual(self.testModule.grade, 1)
                elif testGrade > 4:
                    self.assertEqual(self.testModule.grade, 5)
                else:
                    self.assertEqual(self.testModule.grade, testGrade)

        # inappropriate values
        with self.assertRaises(TypeError):
            for testGrade in unitGradesTypeError:
                self.testModule.grade = testGrade
        with self.assertRaises(ValueError):
            for testGrade in unitGradesValueError:
                self.testModule.grade = testGrade

        # data for the course class grad setter
        courseGrades = [0, 3, None, 78]

        # appropriate values
        for testGrade in courseGrades:
            self.testCourse.grade = testGrade

            if testGrade is None:
                self.assertFalse(self.testCourse.passed)
            elif testGrade > 4:
                self.assertFalse(self.testCourse.passed)
            else:
                self.assertTrue(self.testCourse.passed)

    def testClassPropertyCredits(self):
        """Tests the credit setters and getters of the classes in classes.py
         it tests, that the setters set appropriate values
         and raise errors for inappropriate values

         To-Do:
         Rework the module credits, such that mandatory and elective are properties and credits get private.
         """

        # data for the course credit setter
        creditsPass = [0, 1, 20, 5000, '2']
        creditsValueError = [-5, -1, None, 'test']
        creditsTypeError = [[5, 4]]

        # appropriate values
        for testCredits in creditsPass:
            self.testModule.credits = testCredits
            self.assertEqual(self.testModule.credits, int(testCredits))

        # inappropriate values
        with self.assertRaises(ValueError):
            for testCredits in creditsValueError:
                self.testModule.credits = testCredits
        with self.assertRaises(TypeError):
            for testCredits in creditsTypeError:
                self.testModule.credits = testCredits

    def testClassPropertyRequiredCredits(self):
        """Tests the requiredCredit setters and getters of the collectorClass in classes.py
         it tests, that the setters set appropriate values
         and raise errors for inappropriate values
         """

        # data for the course credit setter
        creditsPass = [0, 1, 20, 5000, '2']
        creditsValueError = [-5, -1, None, 'test']
        creditsTypeError = [[5, 4]]

        # appropriate values
        for testCredits in creditsPass:
            self.testCollector.required_credits = testCredits
            self.assertEqual(self.testCollector.required_credits, int(testCredits))

        # inappropriate values
        with self.assertRaises(ValueError):
            for testCredits in creditsValueError:
                self.testCollector.required_credits = testCredits
        with self.assertRaises(TypeError):
            for testCredits in creditsTypeError:
                self.testCollector.required_credits = testCredits

    def testCollectorFuncAddRemoveModule(self):
        """Tests the correct behavior of the addModule function of the collectorClass"""

        self.testCollector.add_module(self.testModule, 1)

        self.assertIn(self.testModule, self.testCollector.submodules)
        self.assertIn(self.testCollector, self.testModule.collectors)
        self.assertEqual(self.testModule.weight, 1)

        self.testCollector.remove_module(self.testModule)

        self.assertNotIn(self.testModule, self.testCollector.submodules)
        self.assertNotIn(self.testCollector, self.testModule.collectors)
        self.assertEqual(self.testModule.weight, None)

    def testCollectorCalcCredits(self):
        """Test the calcCredit function"""
        testCourses = [Course('Course 1', init_credits=6),
                       Course('Course 1', init_credits=4),
                       Course('Course 1', init_credits=4)]
        testCredits = 0

        for course in testCourses:
            self.testCollector.add_module(course, 1)

        self.assertEqual(self.testCollector.credits,testCredits)

        for course in testCourses:
            course.passed = True
            testCredits += course.credits

        self.assertEqual(self.testCollector.credits,testCredits)

    def testCollectorCalcGrade(self):
        """Test the calcGrade function"""
        testCourses = [Course('Course 1', init_credits=6),
                       Course('Course 1', init_credits=4),
                       Course('Course 1', init_credits=4)]
        grades = [4, 1, 5]
        weights = [2, 1, 45]
        testGrade = 0

        for course in testCourses:
            course.grade = grades[testCourses.index(course)]
            self.testCollector.add_module(course, weights[testCourses.index(course)])
            testGrade += grades[testCourses.index(course)] * weights[testCourses.index(course)]

        testGrade /= len(testCourses)


    def testCollectorCalcPassed(self):
        """Test the calcPassed function"""
        testCourses = [Course('Course 1', init_credits=6),
                       Course('Course 1', init_credits=4),
                       Course('Course 1', init_credits=4)]

        for course in testCourses:
            self.testCollector.add_module(course, 1)

        for course in testCourses:
            course.passed = False

        self.assertFalse(self.testCollector.passed)

        for course in testCourses:
            course.passed = True

        self.assertFalse(self.testCollector.passed)

        for course in testCourses:
            course.credits = 100

        self.assertTrue(self.testCollector.passed)

    def testUpdate(self):

        testCourses = [Course('Course 1', init_credits=6),
                       Course('Course 1', init_credits=4),
                       Course('Course 1', init_credits=4)]

        testCollectors = [Collector('Collector 1', required_credits=20),
                          Collector('Collector 1', required_credits=20),
                          Collector('Collector 1', required_credits=20)]

        for course in testCourses:
            self.testCollector.add_module(course, 1)

        self.assertEqual(self.testCollector.required_credits, 16)

        for collector in testCollectors:
            self.testCollector.add_module(collector, 1)

        self.assertEqual(self.testCollector.required_credits, 16)

        for course in testCourses:
            self.testCollector.remove_module(course)

        self.assertEqual(self.testCollector.required_credits, 60)



    def testMoveModule(self):
        """Test the moveModule function"""
        pass

if __name__ == "__main__":
    unittest.main()
