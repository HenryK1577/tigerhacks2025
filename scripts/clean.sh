#!/bin/bash

cd ..
cd flask_backend
rm -r .venv
rm -r __pycache__

cd ..
cd react_frontend
rm -r node_modules
cd ..