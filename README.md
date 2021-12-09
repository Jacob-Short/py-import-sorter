# py-import-sorter

Will sort all import statements in all python files within the given directory


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Download and install poetry 

    Windows

        (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

    Mac OS/ Linux

        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Avtivate virtual environment

    poetry shell

Install dependencies

    poetry install

Start CLI file

    python python main.py <directory-with-pyfiles>

