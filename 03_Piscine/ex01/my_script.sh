#!/bin/bash

# Display pip version
pip -V

# Set the log file name
LOG_FILE="path_py_install.log"

# Check if the local_lib folder exists
if [ -d "local_lib" ]; then
  # If the folder exists, remove it and its contents
  rm -rf local_lib
fi

# Install the library with pip into the local_lib folder
pip install --upgrade --log path_py_install.log --target ./local_lib git+https://github.com/jaraco/path.py.git &> /dev/null

# Check if it has been succesfully installed. If yes, it runs
if [ "$(grep "Successfully installed path" "$LOG_FILE")" ]; then
  python3 my_program.py
fi
