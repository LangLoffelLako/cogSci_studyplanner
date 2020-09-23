"""
Classes that are used to implement the courses, modules, theses, degrees present in the study regulations.
They are able to be interdependent, as they can be attributed to one each other as submodules or
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
        Collectors are observer. The collectors list does contain the elements, that may change if this Module changes.
        The other attributes contain the information that is made explicit in the name.
                :param name:
        :param code:
        :param init_credits:
        """
        self.name = name
        self.code = code
        self.weight = None
        self.collectors = []
        self.__credits = init_credits
        self.__passed = False
        self.__grade = None

    def __str__(self):
        """Print command"""
        return str(self.__class__) + ": " + str(self.__dict__)

    def structure(self):
        """abstract method"""
        pass

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        """
        Does ensure, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Calls the 'updates_collectors' function of the class.
        """

        #set grade
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


        # call update
        self.update_collectors()

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, val):
        """
        Ensures, that only integers greater equal 0 are set.
        Calls the 'update_collectors' function of the class.
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
        Ensures that passed is a boolean.
        Calls the 'update_collectors' function of the class
        """
        if isinstance(passed, bool):
            self.__passed = passed

        self.update_collectors()

    def update_collectors(self):
        """
        This function does update the collectors in the 'self.collectors' list.
        """
        for collector in self.collectors:
            collector.update()


class Course(Module):
    """
    Class for course implementation.
    Minor deviation from Module class:
        -new parameter: 'semester'
        -if 'grade' is set 'passed' is changed
    """

    def __init__(self, name, code=None, init_credits=0, semester=None):
        """
        See Module class.
        Attributes contain the information that is made explicit in the name.
        :param name:
        :param code:
        :param init_credits:
        :param semester:
        """
        Module.__init__(self, name, code, init_credits)
        self.semester = semester

    def structure(self):
        """Print command"""
        return str(self.name)

    @property
    def grade(self):
        return super().grade

    @grade.setter
    def grade(self, grade):
        """
        Ensures, that grades are in the range defined in the study regulations (1-4 and 5 for failed).
        Calls the 'update_collectors' function of the class.
        Sets 'self.passed' accordingly.
        """
        # set grade
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

        # call update
        if self.__grade is not None:
            self.update_collectors()

        # set passed
        if self.__grade is None:
            self.passed = False
        elif 1 <= self.__grade <= 4:
            self.passed = True
        else:
            self.passed = False


class Collector(Module):
    """
    Class for implementing modules, theses, degrees
    Deviations from Module:
    - New parameters: __required credits, __submodules
    - 'structure' function returns the submodule structure recursively

    """

    def __init__(self, name, code=None, required_credits=0):
        """
        See Module class.
        Attributes contain the information that is made explicit in the name.
        :param name:
        :param code:
        :param required_credits:
        """
        Module.__init__(self, name, code, init_credits=0)
        self.__required_credits = required_credits
        self.__submodules = []

    def structure(self):
        """
        Calls the same function for all submodules in the '__submodules' list.
        Thereby a nice overview over the tree structure of submodules is created and returned.
        :return:  The recursive submodule structure of the class
        """
        my_name = self.name
        submodules = ", ".join([module.structure() for module in self.__submodules])
        structure = f"{my_name}: [{submodules}]"

        return structure

    @property
    def required_credits(self):
        return self.__required_credits

    @required_credits.setter
    def required_credits(self, val):
        """
        Ensures, only integers greater equal 0
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
        -This function is used to calculate the achieved 'credits' through the '__calc_credits' function,
        if the Module is 'passed' through the '__calc_passed' function and its 'grade' through the '__calc_grade'
        function.
        -The function is mainly used in the 'update_collectors' function (see Module)
        -Order is important here, as self.calcPassed uses self.credits and self.requiredCredits
        :return:
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
        Does check, if all submodules are passed and compares acquired and required credits
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
        Calculates the grad from weighted passed submodules with grades.
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
    !!Legacy!!
    """
    old_collector.remove_module(module)
    new_collector.add_module(module, weight)
