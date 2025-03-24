Welcome to MyTorch!
This Notebook demonstrates how easy it is to use our cloud-based GPUs.
Notice that we are using standard PyTorch syntax, but our venv has MyTorch instead.
That's how easy it is to use MyTorch.

Setup Instructions:
1) Register at MyTorch.net and get your access token, then save it to ~/.mytorch
   - echo "token=xxx" > ~/.mytorch
2) Set Up a Clean Virtual Environment:
   Create and activate a new virtual environment to isolate your MyTorch installation:
   - python3 -m venv ~/venv_mytorch
   - source ~/venv_mytorch/bin/activate
3) Install MyTorch and Jupyter
   - pip install --upgrade pip
   - pip install --upgrade mytorch-ai
   - pip install jupyterlab ipykernel jupyter
4) Register the Virtual Environment as a Jupyter Kernel. This makes your new environment available as a kernel named “mytorch (venv)” in Jupyter:
   - python -m ipykernel install --user --name mytorch_env --display-name "mytorch (venv)"
5) Launch Jupyter Notebook
   - jupyter notebook
