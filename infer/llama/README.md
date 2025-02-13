# Llama-3.2-1B Infer example

This is a demo that will show the exact same code (`llama_infer.py`) running either locally (if run with a PyTorch venv) or in the cloud (if run with a MyTorch venv).

##Prerequiste setup
You need to have two environmental variables set up in your shell for things to run:

`HUGGING_FACE_TOKEN`

and

`MYTORCH_SERVER_IP`

In addition, you need the ability to run the MyTorch server on the machine with the provided IP.


## Running the MyTorch server
Setting up the server is very straightforward:

- download the repo
- create a Python venv
- run the server

###Download the repo

If you do not have an invite to be a collaborator on the myTorch repo, contact Greg

`git clone git@github.com:mytorch-ai/mytorch.git`

###Create a Python env

NOTE: myTorch requires Python 3.10 or greater
`cd mytorch/server`

`python3 -m venv venv_mytorch_server`

`source venv_mytorch_server/bin/activate`

`pip install -r requirements.txt`

###Run the MyTorch Server
`cd mytorch/server`

`python server.py --log debug`

## Running the demo

To run the demo, we first run `llama_infer.py` in one virtual environment and then the other. First, let's create both virtual environments:

`./env_setup.sh`

This will generate a `venv_pytorch` folder, and a `venv_mytorch` folder

### Run the script locally using PyTorch
`source venv_pytorch/bin/activate`

`python llama_infer.py`

`deactivate`

### Run the script in on a remote resource using MyTorch
`source venv_mytorch/bin/activate`

`python llama_infer.py`

`deactivate`

###Notes:

