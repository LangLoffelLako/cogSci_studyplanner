"""
Classes that are used to implement the courses, modules, theses, degrees present in the study regulations.
Especially they are able to be interdependent, as they can be attributed to one each other as submodules or
collectors. This means changes in grades or newly added courses/modules can change modules that contain them.
This allows for the tree structure a study degree possesses.
"""

import logging


class Module:
    """
    Base class for implementing courses or modules, theses, degrees
    """

    def __init__(self, name, code=None, init_credits=0):
        """
        Collectors are observer.
        """
        self.name = name
        self.code = code
        self.weight = None
        self.collectors = []
        self.__credits = init_credits
        self.__passed = False
        self.__grade = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def print_structure(self):
        """
        Abstract
        """
        pass

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        """
        Does ensure, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Updates collectors.
        """
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
        self.update_collectors()

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, val):
        """
        Only integers greater equal 0.
        Updates collectors.
        """
        try:
            val = int(val)
            if 0 <= val:
                self.__credits = val
            else:
                raise ValueError('ValueError negativ value')
        except Exception:
            raise
        self.update_collectors()

    @property
    def passed(self):
        return self.__passed

    @passed.setter
    def passed(self, passed):
        """
        Only booleans.
        Updates collectors.
        """
        if isinstance(passed, bool):
            self.__passed = passed
        self.update_collectors()

    def update_collectors(self):
        """
        As all collectors that contain a module should be updated, when one of its submodules change, this ensures it.
        """
        for collector in self.collectors:
            collector.update()
            logging.debug('Collectors updated')


class Course(Module):
    """
    Class for course implementation.
    """

    def __init__(self, name, code=None, init_credits=0, semester=None):
        Module.__init__(self, name, code, init_credits)
        self.semester = semester

    def print_structure(self):
        return str(self.name)

    @property
    def grade(self):
        return super().grade

    @grade.setter
    def grade(self, grade):
        """
        Does ensure, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Does set the self.passed attribute accordingly.
        """
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
            if grade is None:
                self.__grade = grade
            else:
                raise TypeError('TypeError only numbers or "None" allowed')
        except Exception:
            raise Exception

        if self.__grade is not None:
            self.update_collectors()

        if self.__grade is None:
            self.passed = False
        elif 1 <= self.__grade <= 4:
            self.passed = True
        else:
            self.passed = False


class Collector(Module):
    """
    Class for implementing modules, theses, degrees
    """

    def __init__(self, name, code=None, required_credits=0):
        Module.__init__(self, name, code, init_credits=0)
        self.__required_credits = required_credits
        self.__submodules = []

    def print_structure(self):

        my_name = self.name
        submodules = ", ".join([module.print_structure() for module in self.__submodules])
        structure = f"{my_name}: [{submodules}]"

        return structure

    @property
    def required_credits(self):
        return self.__required_credits

    @required_credits.setter
    def required_credits(self, val):
        """
        Only integers greater equal 0
        """
        try:
            val = int(val)
            if 0 <= val:
                self.__required_credits = val
            else:
                raise ValueError('ValueError negativ value')
        except Exception:
            raise

    @property
    def submodules(self):
        return self.__submodules

    def add_module(self, module, weight):
        """
        Adds a submodule
        Order is important here, as self.update uses self.__submodules
        """
        module.weight = weight
        self.__submodules.append(module)
        module.collectors.append(self)
        self.update()

    def remove_module(self, module):
        """
        Removes a submodule
        Order is important here, as self.update uses self.__submodules
        """
        module.weight = None
        self.__submodules.remove(module)
        module.collectors.remove(self)
        self.update()

    def update(self):
        """
        Order is important here, as self.calcPassed uses self.credits and self.requiredCredits
        """
        if all(isinstance(module, Collector) for module in self.__submodules):
            self.__required_credits = sum(module.required_credits for module in self.__submodules)
        self.credits = self.__calc_credits()
        self.passed = self.__calc_passed()
        self.grade = self.__calc_grade()

    def __calc_credits(self):
        """
        Adds up credits of passed submodules
        """
        new_credits = 0
        for module in self.__submodules:
            if module.passed:
                new_credits += module.credits
        return new_credits

    def __calc_passed(self):
        """
        Does check, if all submodules are passed and compares aquired and required credits
        """
        pass_cond = True
        for module in self.__submodules:
            if not module.passed:
                pass_cond = False
            if self.credits < self.required_credits:
                pass_cond = False
            else:
                logging.info('Not enough credits')
        return pass_cond

    def __calc_grade(self):
        """
        Calculates the grad from weighted passed submodules with grades
        """
        new_grade = 0
        weights = 0
        if not self.__submodules:
            new_grade = None
        else:
            for module in self.__submodules:
                weights += module.weight
                if module.passed:
                    if module.grade is not None:
                        new_grade += module.grade * module.weight
            if weights != 0:
                new_grade /= weights
            else:
                new_grade = None

        return new_grade


def move_module(module, old_collector, new_collector, weight):
    """
    Does move a module from one collector to the other
    """
    old_collector.remove_module(module)
    new_collector.add_module(module, weight)
