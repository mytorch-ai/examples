# Llama-3.2-1B Infer example

This is a demo that will show the exact same code (`llama_infer.py`) running either locally (if run with a PyTorch venv) or in the cloud (if run with a MyTorch venv).

## Prerequistes
You need to have the "HUGGING_FACE_TOKEN" environment variable set up in your shell for things to run.  You can get the required token by setting up an account on HuggingFace 
if you don't already have one.

## Create a Python env

MyTorch requires Python 3.10 or greater.  MyTorch replaces PyTorch and other Machine Learning libraries so it is important that you start with a clean enviroment. The easiest way to do that is with Python's virtualenv as shown here:

`python3 -m venv ~/venv_mytorch_server`

`source ~/venv_mytorch_server/bin/activate`

`pip install https://raw.githubusercontent.com/mytorch-ai/examples/main/mytorch-0.3.0-py3-none-any.whl`

## Running the demo
You are now ready to run the demo.  Simply run the program like you would any PyTorch program.

`python llama_infer.py`

## Notes:

