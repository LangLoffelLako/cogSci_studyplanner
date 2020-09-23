# SPAM Replacement Backend

This is a backend for a new version of study planning tool for the cognitive
science programm at the university of Osnabrück.
The old one you find here https://portal.ikw.uni-osnabrueck.de/~SPAM/

## Where to find what? 

In the file /cls/classes.py you find the classes on which this backend is based.
They can be used to implement the structure of each study regulation and record
taken courses with there results.

In the regulations folder you find the study regulations put into a format, 
that can be read by the program, together with the file register_regulations.py.
This file is used to create a tree structure of the study regulation 
with the help of the classes from classes.py.

In the regulations/data folder you find pickled versions of the study regulation
brought into tree structure with register_regulations.py.

## Support

If you are interested in the project get into contact with:

[Marie Sindermann](marie.sindermann@uos.de)

[Luis Mienhardt](lmienhardt@uos.de)

## What to do now?

With the existing backend a way to display the tree structure could be established.
I suggest to do this recursively.

Further a way to include a new course should be created and the existing methods 
of the collector class to add and remove submodules used to make it possible to
rearrange the tree structure.

## Authors
LangLoffelLako

## Project Status

This project is currently discontinued, if you are interested to take it up get into 
contact with the above mentioned.
 