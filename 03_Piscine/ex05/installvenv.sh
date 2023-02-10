#!/bin/bash

# Create virtual environment
python3 -m venv django_venv

# Activate virtual environment
source django_venv/bin/activate

#Install last versions
pip install -r requirements.txt