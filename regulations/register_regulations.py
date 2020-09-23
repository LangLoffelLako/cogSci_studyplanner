"""
This file contains three functions 'register_po_bachelor_11', 'register_po_bachelor_19()', 'register_po_master_19()'
turning the data saved in the corresponding regulation files into a class based structure
using the classes from the /cls folder. This structures get then saved in /./data folder.
The 'register_modules' function is  necessary for this operation.
"""

import pickle
from regulations import \
    bsc_11_regulations as bachelor_11, \
    bsc_19_regulations as bachelor_19, \
    msc_19_regulations as master_19
from cls.classes import Collector, Course


def register_all_po():
    """
    Call all register functions at once
    :return:
    """

    register_po_bachelor_11()
    register_po_bachelor_19()
    register_po_master_19()


def register_po_bachelor_19():
    """
    Tranform and save the data structure of the Bachelor 19 study regulation.
    Does use the 'register_modules' function to transform the data into a class structure
    :return:
    """
    degree = {}

    degree.update({'structure': register_modules(module_list=bachelor_19.degree),
                   'placeholder': register_modules(module_list=bachelor_19.placeholder),
                   'pflichtbereich': register_modules(module_list=bachelor_19.pflichtbereich),
                   'wahlpflichtbereich': register_modules(module_list=bachelor_19.wahlpflichtbereich),
                   })

    save = open('data/po_ba_19_data.pkl', 'wb')
    pickle.dump(degree, save)
    save.close()


def register_po_master_19():
    """
    Tranform and save the data structure of the master 19 study regulation.
    Does use the 'register_modules' function to transform the data into a class structure
    :return:
    """
    degree = {}

    degree.update({'structure': register_modules(module_list=master_19.degree)})

    save = open('data/po_ma_19_data.pkl', 'wb')
    pickle.dump(degree, save)
    save.close()


def register_po_bachelor_11():
    """
    Tranform and save the data structure of the bachelor 11 study regulation.
    Does use the 'register_modules' function to transform the data into a class structure
    :return:
    """
    degree = {}

    degree.update({'structure': register_modules(module_list=bachelor_11.degree),
                   'placeholder': register_modules(module_list=bachelor_11.placeholder),
                   'pflichtbereich': register_modules(module_list=bachelor_11.pflichtbereich),
                   'wahlpflichtbereich': register_modules(module_list=bachelor_11.wahlpflichtbereich),
                   })

    save = open('data/po_ba_11_data.pkl', 'wb')
    pickle.dump(degree, save)
    save.close()


def register_modules(module_list, collector=None):
    """
    This function skillfully enfolds the information nested in module_list by recursion over the 'module' index until
    only reaching empty 'module' elements.
    The function will return the given collector or the first collector created in the function.

    :param module_list: list of data for class structure
    :param collector:   collector class instance
    :return:            collector class instance
    """

    for submodule in module_list:
        if submodule['type'] == 'collector':

            child_module = Collector(name=submodule['name'], code=submodule['code'],
                                     required_credits=submodule['credits'])

            #  if cond only used for the first iteration
            if collector is None:
                collector = child_module
            else:
                collector.add_module(child_module, weight=submodule['weight'])

            register_modules(submodule['modules'], child_module)

        elif submodule['type'] == 'course':

            child_module = Course(name=submodule['name'], code=submodule['code'], init_credits=submodule['credits'])

            #  if cond only used for the first iteration
            if collector is None:
                collector = child_module
            else:
                collector.add_module(child_module, weight=submodule['weight'])

    return collector


if __name__ == '__main__':
    register_all_po()
