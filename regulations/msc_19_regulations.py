"""
structure for the master of science 2019 study regulation
"""

from regulations import naming_conventions

degree = \
    [
        {'name': naming_conventions.msc_19_degree_de, 'code': None, 'credits': 120, 'weight': 1, 'type': 'collector',
         'modules': [
             {'name': naming_conventions.msc_19_thesis_de, 'code': None, 'credits': 30, 'weight': 2, 'type': 'course'},
             {'name': naming_conventions.msc_focus_modules_de, 'code': None, 'credits': 32, 'weight': 2, 'type': 'collector',
              'modules': [
                  # here have to be inserted two modules
              ]
              },
             {'name': naming_conventions.msc_study_project_de, 'code': 'CS-MP-SP', 'credits': 24, 'weight': 1,
              'type': 'collector', 'modules': [
                  {'name': naming_conventions.msc_study_project_de, 'code': 'CS-MP-SP', 'credits': 24, 'weight': 1,
                   'type': 'course'}
              ]
              },
             {'name': naming_conventions.msc_interdisc_de, 'code': 'CS-MP-IDC', 'credits': 12, 'weight': 0, 'type': 'collector',
              'modules': []}
         ]},
        {'name': naming_conventions.ai_de, 'code': 'CS-MWP-AI', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
        {'name': naming_conventions.cnp_de, 'code': 'CS-MWP-CNP', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
        {'name': naming_conventions.cl_de, 'code': 'CS-MWP-CL', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
        {'name': naming_conventions.ni_de, 'code': 'CS-MWP-NI', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
        {'name': naming_conventions.ns_de, 'code': 'CS-MWP-NS', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
        {'name': naming_conventions.phil_de, 'code': 'CS-MWP-PHIL', 'credits': 16, 'weight': 1, 'type': 'collector',
         'modules': []},
    ]
