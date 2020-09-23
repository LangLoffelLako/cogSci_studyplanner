"""
Structure for the study bachelor of science 2019 study regulations
"""

from regulations import naming_conventions as name

degree = \
    [
        {'name': name.bsc_11_degree_en, 'code': None, 'credits': 180, 'weight': 1, 'type': 'collector',
         'modules': [
            {'name': name.bsc_11_thesis_en, 'code': None, 'credits': 12, 'weight': 1, 'type': 'course'},
            {'name': 'Bereichsnote', 'code': None, 'credits': 0, 'weight': 2, 'type': 'collector', 'modules': [
                {'name': name.oral_modul_en, 'code': None, 'credits': 0, 'weight': 1,
                 'type': 'collector', 'modules': [
                    {'name': name.oral_modul_en, 'code': None, 'credits': 3, 'weight': 1,
                     'type': 'course'}
                    # Here will be inserted one placeholder BWP
                    ]
                 },
                # Here will be inserted four placeholder BWP
                # Here will be inserted four placeholder BP
            ]},
            {'name': name.free_elective_en, 'code': 'CS-BW', 'credits': 22, 'weight': 0, 'type': 'collector',
             'modules': [
                {'name': name.foxie_11_en, 'code': 'CS-BW-IWS', 'credits': 3, 'weight': 1,
                 'type': 'course'}
                ]
             }
            ]
         },
    ]

# placeholder modules mandatory (weight = 1) and elective (weight = 0)
placeholder = \
    [
        {'name': 'placeholderModuleBWP', 'code': None, 'credits': 0, 'weight': 1, 'type': 'collector', 'modules': [
            {'name': 'placeholderBWP', 'code': None, 'credits': 0, 'weight': 1, 'type': 'collector', 'modules': []}
            ]
         },
        {'name': 'placeholderModuleBP', 'code': None, 'credits': 0, 'weight': 0, 'type': 'collector', 'modules': [
            {'name': 'placeholderBP', 'code': None, 'credits': 0, 'weight': 0, 'type': 'collector', 'modules': []}
            ]
         },
    ]

# predefined module structures
# Pflichtbereich
# TODO : add codes
pflichtbereich =\
    [
        {'name': name.ai_en + ' ' + name.mandatory_en, 'code': None, 'credits': 6, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.cnp_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.cl_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.inf_en + ' ' + name.mandatory_en, 'code': None, 'credits': 9, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.bsc_11_mathematics_en + ' ' + name.mandatory_en, 'code': None, 'credits': 9, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.bsc_11_statistics_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.bsc_11_logic_en + ' ' + name.mandatory_en, 'code': None, 'credits': 6, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.ni_en + ' ' + name.mandatory_en, 'code': None, 'credits': 12, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.ns_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 0,
         'type': 'collector', 'modules': []},
        {'name': name.phil_en + ' ' + name.mandatory_en, 'code': None, 'credits': 10, 'weight': 0,
         'type': 'collector', 'modules': []},
    ]
# TODO: add codes
wahlpflichtbereich =\
    [
        {'name': name.ai_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 20, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.ai_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 1,
             'type': 'collector', 'modules': []},
            {'name': name.ai_en + ' ' + name.elective_en, 'code': None, 'credits': 12, 'weight': 1,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.cnp_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 16, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.cnp_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 1,
             'type': 'collector', 'modules': []},
            {'name': name.cnp_en + ' ' + name.elective_en, 'code': None, 'credits': 8, 'weight': 1,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.cl_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 20, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.cl_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 1,
             'type': 'collector', 'modules': []},
            {'name': name.cl_en + ' ' + name.elective_en, 'code': None, 'credits': 12, 'weight': 1,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.inf_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 18, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.inf_en + ' ' + name.mandatory_en, 'code': None, 'credits': 9, 'weight': 1,
             'type': 'collector', 'modules': []},
            {'name': name.inf_en + ' ' + name.elective_en, 'code': None, 'credits': 9, 'weight': 1,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.bsc_11_mathematics_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 18,
         'weight': 1, 'type': 'collector', 'modules': [
            {'name': name.bsc_11_mathematics_en + ' ' + name.mandatory_en, 'code': None, 'credits': 9, 'weight': 1,
             'type': 'collector', 'modules': []},
            {'name': name.bsc_11_mathematics_en + ' ' + name.elective_en, 'code': None, 'credits': 9, 'weight': 1,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.ni_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 24, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.ni_en + ' ' + name.mandatory_en, 'code': None, 'credits': 12, 'weight': 0,
             'type': 'collector', 'modules': []},
            {'name': name.ni_en + ' ' + name.elective_en, 'code': None, 'credits': 12, 'weight': 0,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.ns_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 20, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.ns_en + ' ' + name.mandatory_en, 'code': None, 'credits': 8, 'weight': 0,
             'type': 'collector', 'modules': []},
            {'name': name.ns_en + ' ' + name.elective_en, 'code': None, 'credits': 12, 'weight': 0,
             'type': 'collector', 'modules': []}
            ]
         },
        {'name': name.phil_en + ' ' + name.mand_elec_name_en, 'code': None, 'credits': 18, 'weight': 1,
         'type': 'collector', 'modules': [
            {'name': name.phil_en + ' ' + name.mandatory_en, 'code': None, 'credits': 10, 'weight': 0,
             'type': 'collector', 'modules': []},
            {'name': name.phil_en + ' ' + name.elective_en, 'code': None, 'credits': 8, 'weight': 0,
             'type': 'collector', 'modules': []}
            ]
         },
    ]
