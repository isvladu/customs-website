#!/bin/bash

export FLASK_APP=./src/main.py
pipenv shell
# source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0
