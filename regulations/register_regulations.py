""""""
import pickle
from regulations import \
    bsc_11_regulations as bachelor_11, \
    bsc_19_regulations as bachelor_19, \
    msc_19_regulations as master_19
from cls.classes import Collector, Course

def register_all_po():

    register_po_bachelor_11()
    register_po_bachelor_19()
    register_po_master_19()

def register_po_bachelor_19():
    """

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

    :return:
    """
    degree = {}

    degree.update({'structure': register_modules(module_list=master_19.degree)})

    save = open('data/po_ma_19_data.pkl', 'wb')
    pickle.dump(degree, save)
    save.close()

def register_po_bachelor_11():
    """

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
    :param module_list: list of collector class and course class instances
    :param collector:   collector class instance
    :return:            list of collector class
    """

    modules = []

    for submodule in module_list:
        if submodule['type'] == 'collector':
            child_module = Collector(name=submodule['name'], code=submodule['code'],
                                     required_credits=submodule['credits'])

            if collector is None:
                modules.append(child_module)
            else:
                collector.add_module(child_module, weight=submodule['weight'])

            register_modules(submodule['modules'], child_module)

        elif submodule['type'] == 'course':
            child_module = Course(name=submodule['name'], code=submodule['code'], init_credits=submodule['credits'])
            if collector is None:
                modules.append(child_module)
            else:
                collector.add_module(child_module, weight=submodule['weight'])

    return modules


if __name__ == '__main__':
    register_all_po()
