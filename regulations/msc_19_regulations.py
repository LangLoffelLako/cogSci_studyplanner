"""
Structure for the study master of science 2019 study regulations. Under the 'degree' list we find the
general structure of the curriculum.

Remarks:
-'credits' does equal the required credits in the class structure.
-To understand how this information will be transformed into the class structure look at the
register_regulations.register_modules function.
"""

from regulations import naming_conventions as names

degree = \
    [
        {'name': names.msc_19_degree_de, 'code': None, 'credits': 120, 'weight': 1, 'type': 'collector', 'modules': [
             {'name': names.msc_19_thesis_de, 'code': None, 'credits': 30, 'weight': 2, 'type': 'course'},
             {'name': names.msc_focus_modules_de, 'code': None, 'credits': 32, 'weight': 2, 'type': 'collector',
              'modules': [
                  # here have to be inserted two modules
              ]
              },
             {'name': names.msc_study_project_de, 'code': 'CS-MP-SP', 'credits': 24, 'weight': 1, 'type': 'collector',
              'modules': [
                  {'name': names.msc_study_project_de, 'code': 'CS-MP-SP', 'credits': 24, 'weight': 1, 'type': 'course'}
              ]
              },
             {'name': names.msc_interdisc_de, 'code': 'CS-MP-IDC', 'credits': 12, 'weight': 0, 'type': 'collector',
              'modules': []}
         ]},
        {'name': names.ai_de, 'code': 'CS-MWP-AI', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
        {'name': names.cnp_de, 'code': 'CS-MWP-CNP', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
        {'name': names.cl_de, 'code': 'CS-MWP-CL', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
        {'name': names.ni_de, 'code': 'CS-MWP-NI', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
        {'name': names.ns_de, 'code': 'CS-MWP-NS', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
        {'name': names.phil_de, 'code': 'CS-MWP-PHIL', 'credits': 16, 'weight': 1, 'type': 'collector', 'modules': []},
    ]
