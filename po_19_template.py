""""""
import pickle
import logging
from classes import Module, Collector, Course

def poBachelor2019():
    """Create all predefined nodes and all required courses for the PO2019 bachelor.
    Create the tree structure of the study regulations"""

    #some naming conventions to make for consistent naming
    mandatoryName = 'Pflichtbereich'
    electiveName = 'Wahlpflichtbereich'

    #zero row of node
    degree = Collector('Bachelor PO 2019', requiredCredits=180)

    #first row of nodes
    thesis = Course('Bachelor Thesis', credits=12)
    mandatoryCourses = Collector('Bereichsnoten')
    electiveCourses = Collector('Profilbildener Wahlbereich', code='CS-BW', requiredCredits=22)

    degree.addModule(thesis, 1)
    degree.addModule(mandatoryCourses,2)
    degree.addModule(electiveCourses,0)

    #second/third row of nodes
    mandatoryOralCollector = Collector('Modulübergreifende mündliche Prüfung', requiredCredits=3)
    AIBWP = Collector('Artificial Intelligence', requiredCredits=20)
    CNPBWP = Collector('Cognitive (Neuro-)Psychology', requiredCredits=20)
    CLBWP = Collector('Computational Linguistics', requiredCredits=20)
    INFBWP = Collector('Informatics', requiredCredits=21)
    MATBWP = Collector('Mathematics', requiredCredits=15)
    MCSBWP = Collector('Methods of Cognitive Science', requiredCredits=20)
    NIBWP = Collector('Neuroinformatics', requiredCredits=20)
    NSBWP = Collector('Neuroscience', requiredCredits=20)
    PHILBWP = Collector('Philosophy of Cognitive Science', requiredCredits=20)

    AIBP = Collector('Artificial Intelligence', requiredCredits=20)
    CNPBP = Collector('Cognitive (Neuro-)Psychology', requiredCredits=20)
    CLBP = Collector('Computational Linguistics', requiredCredits=20)
    INFBP = Collector('Informatics', requiredCredits=21)
    MATBP = Collector('Mathematics', requiredCredits=6)
    MCSBP = Collector('Methods of Cognitive Science', requiredCredits=20)
    NIBP = Collector('Neuroinformatics', requiredCredits=20)
    NSBP = Collector('Neuroscience', requiredCredits=20)
    PHILBP = Collector('Philosophy of Cognitive Science', requiredCredits=20)

    placeholderModuleBP = Collector(mandatoryName)
    placeholderModuleBWP = Collector(electiveName)

    mandatoryCourses.addModule(mandatoryOralCollector,1)
    for i in range(0,4):
        mandatoryCourses.addModule(placeholderModuleBWP,1)
    for i in range(4,9):
        mandatoryCourses.addModule(placeholderModuleBP,0)

    mandatoryOralCollector.addModule(placeholderModuleBWP,0)

    #fourth row of nodes
    mandatoryAI = Collector('Artificial Intelligence' + ' ' + mandatoryName, code='CS-BP-AI', requiredCredits=8)
    mandatoryCNP = Collector('Cognitive (Neuro-)psychology' + ' ' + mandatoryName, code='CS-BP-CNP', requiredCredits=8)
    mandatoryCL = Collector('Computational Linguistics' + ' ' + mandatoryName, code='CS-BP-CL', requiredCredits=8)
    mandatoryINF = Collector('Informatics' + ' ' + mandatoryName, code='CS-BP-INF', requiredCredits=9)
    mandatoryIKWMAT = Collector('IKW Mathematics' + ' ' + mandatoryName, code='CS-BP-MAT', requiredCredits=6)
    mandatoryFB6MAT = Collector('FB6 Mathematics' + ' ' + mandatoryName, code='CS-BP-MAT', requiredCredits=9)
    mandatoryMCS = Collector('Methods of Cognitive Science' + ' ' + mandatoryName, code='CS-BP-MCS', requiredCredits=8)
    mandatoryNI = Collector('Neuroinformatics' + ' ' + mandatoryName, code='CS-BP-NI', requiredCredits=12)
    mandatoryNS = Collector('Neuroscience' + ' ' + mandatoryName, code='CS-BP-NS', requiredCredits=8)
    mandatoryPHIL = Collector('Philosophy of Cognitive Science' + ' ' + mandatoryName, code='CS-BP-PHIL', requiredCredits=10)

    electiveAI = Collector('Artificial Intelligence' + ' ' + electiveName, code='CS-BWP-AI', requiredCredits=12)
    electiveCNP = Collector('Cognitive (Neuro-)psychology' + ' ' + electiveName, code='CS-BWP-CNP', requiredCredits=12)
    electiveCL = Collector('Computational Linguistics' + ' ' + electiveName, code='CS-BWP-CL', requiredCredits=12)
    electiveINF = Collector('Informatics' + ' ' + electiveName, code='CS-BWP-INF', requiredCredits=9)
    electiveMAT9 = Collector('IKW Mathematics' + ' ' + electiveName, code='CS-BWP-MAT', requiredCredits=9)
    electiveMAT18 = Collector('IKW Mathematics' + ' ' + electiveName, code='CS-BWP-MAT', requiredCredits=18)
    electiveMCS = Collector('Methods of Cognitive Science' + ' ' + electiveName, code='CS-BWP-MCS', requiredCredits=12)
    electiveNI = Collector('Neuroinformatics' + ' ' + electiveName, code='CS-BWP-NI', requiredCredits=8)
    electiveNS = Collector('Neuroscience' + ' ' + electiveName, code='CS-BWP-NS', requiredCredits=12)
    electivePHIL = Collector('Philosophy of Cognitive Science' + ' ' + electiveName, code='CS-BWP-PHIL', requiredCredits=10)

    placeholderBP = Collector('Module')
    placeholderBWP = Collector('Module')

    AIBWP.addModule(mandatoryAI,1)
    AIBWP.addModule(electiveAI,1)
    AIBP.addModule(mandatoryAI,1)
    CNPBWP.addModule(mandatoryCNP,1)
    CNPBWP.addModule(electiveCNP,1)
    CNPBP.addModule(mandatoryCNP,1)
    CLBWP.addModule(mandatoryCL,1)
    CLBWP.addModule(electiveCL,1)
    CLBP.addModule(mandatoryCL,1)
    INFBWP.addModule(mandatoryINF,1)
    INFBWP.addModule(electiveINF,1)
    INFBP.addModule(mandatoryINF,1)
    MATBWP.addModule(mandatoryIKWMAT,1)
    MATBWP.addModule(electiveMAT9,1)
    MATBP.addModule(mandatoryIKWMAT,1)
    MCSBWP.addModule(mandatoryMCS,1)
    MCSBWP.addModule(electiveMCS,1)
    MCSBP.addModule(mandatoryMCS,1)
    NIBWP.addModule(mandatoryNI,1)
    NIBWP.addModule(electiveNI,1)
    NIBP.addModule(mandatoryNI,1)
    NSBWP.addModule(mandatoryNS,1)
    NSBWP.addModule(electiveNS,1)
    NSBP.addModule(mandatoryNS,1)
    PHILBWP.addModule(mandatoryPHIL,1)
    PHILBWP.addModule(electivePHIL,1)
    PHILBP.addModule(mandatoryPHIL,1)

    placeholderModuleBWP.addModule(placeholderBP,1)
    placeholderModuleBWP.addModule(placeholderBWP,1)
    placeholderModuleBP.addModule(placeholderBP,1)

    #preexistent courses
    courseIWS = Course('Anleitung zum wissenschaftlichen Arbeiten', code='CS-BW-IWS', credits=6)
    mandatoryOralExamen = Course('Modulübergreifende mündliche Prüfung', credits=3)

    mandatoryOralCollector.addModule(mandatoryOralExamen,1)
    electiveCourses.addModule(courseIWS,1)

    save = open('po_19_data.pkl','wb')
    pickle.dump(degree,save)
    save.close()

if __name__ == "__main__":
    poBachelor2019()