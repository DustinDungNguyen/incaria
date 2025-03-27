#!/bin/bash


# This script runs local development environment web service


# This script prepares the python virtual environment
# and runs database migrations
# then starts up the server


# Virtual environment directory will be created in the /code directory
# of the container, which will be in the root of your project.
VENV_DIR=incaria_venv


# DJANGO_PROJECT_DIRECTORY=incaria # TODO: Change this to the directory that contains your manage.py (generated during django project setup)


# Create the virtualenv only if it does not exist already.
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv $VENV_DIR
fi


# Activating the virtual environment
. ./$VENV_DIR/bin/activate


# Installing python packages into virtual environment
pip install -r requirements.txt


# Change directory into the django project directory, then run DB migrations and start server
cd /code/
python /code/manage.py migrate
python /code/manage.py runserver 0.0.0.0:8000