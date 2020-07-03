"""The Unittest for the classes "unit", "course" and "module". It tests the creation of the class, the setters and
getters if defined and the functions

To-Do:
Add testclass for the functionality of the classes.
"""

import unittest
from legacy.classes import unit, mandatoryCourse


class BasicClassTest(unittest.TestCase):
    """Test for the Creation and variables of the classes"""

    def setUp(self) -> None:

        self.testUnit = unit('test unit', code='123456')
        self.testCourse = mandatoryCourse('test course', code='123456', semester='WS20', credits=5)
        #self.testModule = module('test module', code='123456', mandatoryCredits=5, electiveCredits=9)

    def tearDown(self) -> None:
        pass

    def testClassCreations(self):
        """tests the initiation of the classes in classes.py
        It tests that well defined instances are created
        when called with appropriate parameters"""

        # unit classes are initiated
        testUnit = unit('test unit')
        self.assertIsInstance(testUnit, unit)
        testUnit = unit('test unit', '1548hnn')
        self.assertIsInstance(testUnit, unit)
        testUnit = unit('test unit', code='1548hnn')
        self.assertIsInstance(testUnit, unit)

        # course classes are initiated
        testCourse = mandatoryCourse('test course')
        self.assertIsInstance(testCourse, mandatoryCourse)
        testCourse = mandatoryCourse('test course', '123456', 'WS20', 5)
        self.assertIsInstance(testCourse, mandatoryCourse)
        testCourse = mandatoryCourse('test course', code='123456', semester='WS20', credits=5)
        self.assertIsInstance(testCourse, mandatoryCourse)

        # module classes are initiated
        # testModule = module('test module')
        # self.assertIsInstance(testModule, module)
        # testModule = module('test module', 5, 8)
        # self.assertIsInstance(testModule, module)
        # testModule = module('test module', code='123456', mandatoryCredits=5, electiveCredits=9)
        # self.assertIsInstance(testModule, module)

    def testClassPropertyGrades(self):
        """Tests the grad setters and getters functions of the classes in classes.py
        it tests, that the setters only set the property if provided with appropriate values
        and raises an error for inappropriate values"""

        # data for the unit class grad setter
        unitGradesPass = [None, 5, 51.5, 0]
        unitGradesTypeError = [[1, 5]]
        unitGradesValueError = ['testString', -2, 456]

        # appropriate values
        for testGrade in unitGradesPass:
            self.testUnit.grade = testGrade
            if testGrade is None:
                self.assertEqual(self.testUnit.grade, testGrade)
            elif testGrade < 1:
                self.assertEqual(self.testUnit.grade, 1)
            elif testGrade > 4:
                self.assertEqual(self.testUnit.grade, 5)
            else:
                self.assertEqual(self.testUnit.grade, testGrade)

        # inappropriate values
        with self.assertRaises(TypeError):
            for testGrade in unitGradesTypeError:
                self.testUnit.grade = testGrade
        with self.assertRaises(ValueError):
            for testGrade in unitGradesValueError:
                self.testUnit.grade = testGrade

        # data for the course class grad setter
        courseGrades = [0, 3, None, 78]

        # appropriate values
        for testGrade in courseGrades:
            self.testCourse.grade = testGrade

            if testGrade is None or testGrade > 4:
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
        courseCreditsPass = [0, 1, 20, 5000]
        courseCreditsValueError = [-5, -1, None]
        courseCreditsTypeError = ['test', [5, 4]]

        # appropriate values
        for testCredits in courseCreditsPass:
            self.testCourse.credits = testCredits
            self.assertEqual(self.testCourse.credits, testCredits)

        # inappropriate values
        with self.assertRaises(ValueError):
            for testCredits in courseCreditsValueError:
                self.testCourse.credits = testCredits
        with self.assertRaises(TypeError):
            for testCredits in courseCreditsTypeError:
                self.testCourse.credits = testCredits

        # data for the module credit setter
        # moduleCreditsPass = [[1, 2], [9, 15], [78, 444]]
        # moduleCreditsValueError = [[-1, 2], [None, 2], [1, 8, 9], [5, 'hello'], []]
        # moduleCreditsTypeError = [1, 'hello', None]
        #
        # # appropriate values
        # for testCredits in moduleCreditsPass:
        #     self.testModule.credits = testCredits
        #     self.assertEqual(self.testModule.credits, testCredits)
        #
        # # inappropriate values
        # with self.assertRaises(ValueError):
        #     for testCredits in moduleCreditsValueError:
        #         self.testCourse.credits = testCredits
        # with self.assertRaises(TypeError):
        #     for testCredits in moduleCreditsTypeError:
        #         self.testCourse.credits = testCredits

    # def testClassPropertyCourses(self):
    #     """tests the getter and setter of the course property of courses. The property should be read only."""
    #
    #     #not writeable
    #     with self.assertRaises(AttributeError):
    #         self.testModule.electiveCourses = [self.testCourse]
    #         self.testModule.mandatoryCourses = [self.testCourse]
    #
    #     #add data, that then can be accessed
    #     self.testModule.add_unit(self.testCourse, True)
    #     self.testModule.add_unit(self.testCourse, False)
    #
    #     #access data
    #     self.assertEqual(self.testModule.mandatoryCourses, [self.testCourse])
    #     self.assertEqual(self.testModule.electiveCourses, [self.testCourse])

# class FunctionTest(unittest.TestCase):
#     """This class tests the functions of the classes"""
#
#     def setUp(self) -> None:
#
#         self.testUnit = unit('test unit', code='123456')
#         self.testCourse = mandatoryCourse('test course', code='123456', semester='WS20', credits=5)
#         self.testModule = module('test module', code='123456', mandatoryCredits=5, electiveCredits=9)
#
#     def testModuleAdderRemoverUnit(self):
#         """Tests the adding of units. It tests, that the setters set appropriate values and raise errors for
#         inappropriate values. """
#
#         #data
#         self.testModule = module('addModule', 12, 8)
#         testCourseData = [{'mandatory': [4, 4, 4], 'elective': [2, 2, 6], 'pass': True},
#                           {'mandatory': [4, 4, 8], 'elective': [2, 2, 4], 'pass': True},
#                           {'mandatory': [4, 4, 2], 'elective': [2, 2, 6], 'pass': False},
#                           {'mandatory': [4, 4, 4], 'elective': [2, 2, 2], 'pass': False}]
#
#         for courseData in testCourseData:
#             for credit in courseData['mandatory']:
#                 testCourse = mandatoryCourse('testCourse', credits=credit)
#                 credit = testCourse
#                 self.testModule.add_unit(testCourse, True)
#
#             for credit in courseData['elective']:
#                 testCourse = mandatoryCourse('testCourse', credits=credit)
#                 credit = testCourse
#                 self.testModule.add_unit(testCourse, False)
#
#             self.assertEqual(self.testModule.mandatoryCourses, courseData['mandatory'])
#             self.assertEqual(self.testModule.electiveCourses, courseData['elective'])
#             self.assertEqual(self.testModule.passed, courseData['pass'])
#
#         for testCourse in self.testModule.mandatoryCourses + self.testModule.electiveCourses:
#             self.testModule.remove_unit(testCourse)
#
#         self.assertEqual(self.testModule.mandatoryCourses, [])
#         self.assertEqual(self.testModule.electiveCourses, [])

        # for elective in courseData:
        #     for credit in courseData[elective]:
        #         testCourse = course('testCourse', credits=credit)
        #         self.testModule.add_unit(testCourse, elective)
        #         testCourseData[courseData][elective][credit] = testCourse

        # self.testModule.add_unit(course('testCourse', credits=credit), elective)

    def testModuleGradCalculator(self):
        """Tests the class functions."""
        mandatoryGrade = 0
        electiveGrade = 0
        courseCount = 0

        for mandatoryCourse in self.testModule.mandatoryCourses
            if mandatoryCourse.grade is not None
                courseCount += mandatoryCourse.weight
                mandatoryGrade += mandatoryCourse.grade * mandatoryCourse.weight

        mandatoryGrade = mandatoryGrade / courseCount
        courseCount = 0

        for electiveCourse in self.testModule.electiveCourses
            if electiveCourse.grade is not None
                courseCount += electiveCourse.weight
                mandatoryGrade += electiveCourse.grade * electiveCourse.weight

        electiveGrade = electiveGrade / courseCount

        combinedGrade = (mandatoryGrade + electiveGrade) / 2

        self.assertEqual(testModule.calcGrade, combinedGrade)

if __name__ == "__main__":
    unittest.main()
