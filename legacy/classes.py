#module and course classes

import logging

# this class stores information about courses

class unit:

    def __init__(self, name, code=None):
        self.name = name
        self.code = code

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        try:
            floatValue = float(value)
            if 0 <= value:
                self.__grade = float(value)
            else:
                self.__grade = float(0)
        except TypeError:
            if value == None:
                self.__grade = value
                return
            raise TypeError('TypeError only numbers or "None" allowed')

class mandatoryCourse(unit):

    def __init__(self, name, code=None, semester=None, credits=0):
        unit.__init__(self, name, code)
        self.semester = semester

    # setters and getters

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits):
        if 0 <= credits:
            self.__credits = credits
        else:
            raise ValueError('ValueError negativ value')

    # @property
    # def grade(self):
    #     return self.grade

    @unit.grade.setter
    def grade(self, value):
        unit.__grade = value
        #super().grade.fset(self,value)
        if self.__grade == None:
            self.passed = False
        elif 0 <= self.__grade <= 4:
            self.passed = True
        else:
            self.passed = False

    #else:
    #   raise(ValueError,'ValueError only numerics')

# this class can collect course classes

class module(unit):

    def __init__(self, name, mand_credits=0, elec_credits=0):
        credits = {'mandatory': mand_credits, 'elective': elec_credits}
        unit.__init__(self, name, credits)
        self.__mandatoryPass = False
        self.__electivePass = False
        self.__mandatoryCourses = []
        self.__electiveCourses = []



    def add_unit(self, sub_unit, mandatory, weight = 1):
        """adds a course/module to this module, a weight is given to the course/module"""

        if mandatory:

            sub_unit.weight = weight

    def remove_unit(self, sub_unit):
        """removes a course/module from this module, the weight is removed from the course/module"""
        try:
            self.__mandatoryCourses.remove(sub_unit)
            sub_unit.weight = None
            logging.debug('%s found in %s module mandatories', sub_unit.name, self.name)
        except:
            pass

        try:
            self.__electiveCourses.remove(sub_unit)
            sub_unit.weight = None
            logging.debug('%s found in %s module electives', sub_unit.name, self.name)
        except:
            pass

    def __get_mandatoryCourses(self):
        return self.__mandatoryCourses

    mandatoryCourses = property(__get_mandatoryCourses)

    def __get_electiveCourses(self):
        return self.__electiveCourses

    electiveCourses = property(__get_electiveCourses)

    def updatePass(self):
        '''Does update the private variables mandatoryPass and electivePass'''
        pass

    def calc_grade(self):
        self.grade = 0
        courses = self.__mandCourses + self.__elecCourses

        for course in courses:
            self.grade += course.grade * course

        #self.grade /=
