#!/bin/bash -e

cd $(dirname $0)

if [ "$RUNCOVERAGE" == "1" ]; then
    #python3 -m coverage run --source ctre -m pytest --cov-report html --cov-report term --cov ctre "$@"
    python3 -m pytest --cov-report html --cov-report term --cov ctre "$@"
    #python3 -m coverage report -m
else
    python3 -m pytest "$@"
fi
