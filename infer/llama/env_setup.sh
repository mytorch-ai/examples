#!/bin/bash

echo -e  "\nCreating 'venv_mytorch'\n"
rm -rf venv_mytorch
python -m venv venv_mytorch
source venv_mytorch/bin/activate
pip install --upgrade pip
pip install mytorch-0.3.0-py3-none-any.whl
deactivate


echo -e  "\nCreating 'venv_pytorch'\n"
rm -rf venv_pytorch
python -m venv venv_pytorch
source venv_pytorch/bin/activate
pip install --upgrade pip
pip install -r pytorch_env_requirements.txt
deactivate

echo -e "\nBuild complete! To activate 'venv_mytorch' or 'venv_pytorch', run 'source venv_mytorch/bin/activate' or 'source venv_pytorch/bin/activate'\n"