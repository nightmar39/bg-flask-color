#/bin/sh
FLASK_APP=./color/index.py
pipenv run flask --debug run -h 0.0.0.0
