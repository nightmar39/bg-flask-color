#!/bin/sh
export FLASK_APP=./color/index.py
pipenv --python 3.8
pipenv run flask --debug run -h 0.0.0.0
