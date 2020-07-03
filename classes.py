"""Classes that are used to implement the courses, modules, theses, degrees present in the study regulations.
Especially they are able to be interdependent, as they can be attributed to one each other as submodules or
collectors. This means changes in grades or newly added courses/modules can change modules that contain them.
This allows for the tree structure a study degree possesses."""

import logging


class Module:
    """Base class for implementing courses or modules, theses, degrees
    """

    def __init__(self, name, code=None, credits=0):
        """Collectors are observer."""
        self.name = name
        self.code = code
        self.weight = None
        self.collectors = []
        self.__credits = credits
        self.__passed = False
        self.__grade = None

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        """Does ensure, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Updates collectors."""
        try:
            grade = float(grade)
            if grade < 1:
                self.__grade = float(1)
                logging.debug('Only values between 1 and 4 (or a 5) are supposed')
            elif grade > 4:
                self.__grade = float(5)
                if grade != 5:
                    logging.debug('Only values between 1 and 4 (or a 5) are supposed')
            else:
                self.__grade = grade
        except TypeError:
            if grade is None:
                self.__grade = grade
                return
            else:
                raise TypeError('TypeError only numbers or "None" allowed')
        self.updateCollectors()

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits):
        """Only integers greater equal 0.
        Updates collectors."""
        try:
            credits = int(credits)
            if 0 <= credits:
                self.__credits = credits
            else:
                raise ValueError('ValueError negativ value')
        except:
            raise
        self.updateCollectors()

    @property
    def passed(self):
        return self.__passed

    @passed.setter
    def passed(self, passed):
        """Only booleans.
        Updates collectors."""
        if isinstance(passed, bool):
            self.__passed = passed
        self.updateCollectors()

    def updateCollectors(self):
        """As all collectors that contain a module should be updated, when one of its submodules change, this ensures it."""
        for collector in self.collectors:
            collector.update()
            logging.debug('Collectors updated')

class Course(Module):
    """Class for course implementation."""

    def __init__(self, name, code=None, credits=0, semester=None):
        Module.__init__(self, name, code, credits)
        self.semester = semester

    @property
    def grade(self):
        return super().grade

    @grade.setter
    def grade(self, grade):
        """Does ensure, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Does set the self.passed attribute accordingly."""
        try:
            grade = float(grade)
            if grade < 1:
                self.__grade = float(1)
                logging.debug('Only values between 1 and 4 (or a 5) are supposed')
            elif grade > 4:
                self.__grade = float(5)
                logging.debug('Only values between 1 and 4 (or a 5) are supposed')
            else:
                self.__grade = grade
        except TypeError:
            if grade == None:
                self.__grade = grade
            else:
                raise TypeError('TypeError only numbers or "None" allowed')
        except:
            raise
        if not self.__grade is None:
            self.updateCollectors()

        if self.__grade is None:
            self.passed = False
        elif 1 <= self.__grade <= 4:
            self.passed = True
        else:
            self.passed = False


class Collector(Module):
    """Class for implementing modules, theses, degrees"""

    def __init__(self, name, code=None, requiredCredits=0):
        Module.__init__(self, name, code, credits=0)
        self.__requiredCredits = requiredCredits
        self.__submodules = []

    @property
    def requiredCredits(self):
        return self.__requiredCredits

    @requiredCredits.setter
    def requiredCredits(self, credits):
        """Only integers greater equal 0"""
        try:
            credits = int(credits)
            if 0 <= credits:
                self.__requiredCredits = credits
            else:
                raise ValueError('ValueError negativ value')
        except:
            raise

    @property
    def submodules(self):
        return self.__submodules

    def addModule(self, module, weight):
        """Adds a submodule
        Order is important here, as self.update uses self.__submodules"""
        module.weight = weight
        self.__submodules.append(module)
        module.collectors.append(self)
        self.update()

    def removeModule(self, module):
        """Removes a submodule
        Order is important here, as self.update uses self.__submodules"""
        module.weight = None
        self.__submodules.remove(module)
        module.collectors.remove(self)
        self.update()

    def update(self):
        """Order is important here, as self.calcPassed uses self.credits and self.requiredCredits"""
        if all(isinstance(module,Collector) for module in self.__submodules):
            self.__requiredCredits = sum(module.requiredCredits for module in self.__submodules)
        self.credits = self.calcCredits()
        self.passed = self.calcPassed()
        self.grade = self.calcGrade()

    def calcCredits(self):
        """Adds up credits of passed submodules"""
        newCredits = 0
        for module in self.__submodules:
            if module.passed:
                newCredits += module.credits
        return newCredits

    def calcPassed(self):
        """Does check, if all submodules are passed and adds them to the required credits"""
        passCond = True
        for module in self.__submodules:
            if not module.passed:
                passCond = False
            if self.credits < self.requiredCredits:
                passCond = False
            else:
                logging.info('Not enough credits')
        return passCond

    def calcGrade(self):
        """Calculates the grad from weighted passed submodules with grades"""
        newGrade = 0
        weights = 0
        if not self.__submodules:
            newGrade = None
        else:
            for module in self.__submodules:
                weights += module.weight
                if module.passed:
                    if not module.grade is None:
                        newGrade += module.grade * module.weight
            if weights != 0:
                newGrade /= weights
            else:
                newGrade = None
        return newGrade


def moveModule(module, oldCollector, newCollector, weight):
    """Does move a module from one collector to the other"""
    oldCollector.removeModule(module)
    newCollector.addModule(module, weight)
