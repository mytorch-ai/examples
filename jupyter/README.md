Welcome to MyTorch!

MyTorch provides all the features of PyTorch.
The code in these examples is identical to PyTorch.
MyTorch offers transparent access to cloud GPUs with zero code changes.
Simply pip install mytorch-ai instead of torch.
But first, one more step: register with MyTorch.net and get an access token.
Put that token into a file named ~/.mytorch (in your home directory).

> echo "token=xxx" > ~/.mytorch

Make sure you set up your environment correctly:
> python3 -m venv ~/venv_mytorch  
> source ~/venv_mytorch/bin/activate  
> pip install --upgrade pip  
> pip install --upgrade mytorch-ai  

That's how easy it is to use MyTorch.
To launch these demo notebooks, do this:

> git clone https://github.com/mytorch-ai/examples.git  
> pip install jupyter ipykernel matplotlib numpy scikit-learn  
> python -m ipykernel install --user --name=mytorch --display-name="Python (mytorch)"  
> jupyter notebook

Follow the instructions in your terminal to open your browser to the Jupyter page.
Select the /examples/jupyter/water_leak_detection.ipynb file.
Once open, select the "Python (mytorch)" kernel.
