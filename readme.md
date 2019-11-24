

Ubuntu users follow the given steps. We have already created a conda environment with the required packages listed. On importing the environment.yml file the listed packages get installed on the users system. 

Use the terminal or an Anaconda Prompt for the following steps:


Install Anaconda 
  bash ~/Downloads/Anaconda3-2019.03-Linux-x86_64.sh    
Include the bash command regardless of whether or not you are using Bash shell.
If you did not download to your Downloads directory, replace ~/Downloads/ with the path to the file you downloaded.
Choose “Install Anaconda as a user” unless root privileges are required.
The installer prompts “Do you wish the installer to initialize Anaconda3 by running conda init?” We recommend “yes”.
If you enter “no”, then conda will not modify your shell scripts at all. In order to initialize after the installation process is
done, first run source <path to conda>/bin/activate and then run conda init. See FAQ.


Create the environment from the environment.yml file:
conda env create -f environment.yml
The first line of the yml file sets the new environment's name. 

Activate the new environment: conda activate myenv

Note: Replace myenv with the environment name.

Verify that the new environment was installed correctly:
conda list

The packages already mentioned in this environment gets listed and




Windows users download the pre requisites from the following links.

# Install Flask
http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/

# Install Anaconda 
https://docs.anaconda.com/anaconda/install/windows/

# Install Jupyter Notebook
https://jupyter.readthedocs.io/en/latest/install.html

# Visual studio code
https://code.visualstudio.com/download


After completing all installations follow the given steps

1. Load the flask-proj folder into virtual studio code.
2. Click on run terminal.
3. In the terminal type "python app.py"
4. After excecution the above code go to any browser and type "localhost:5000"

