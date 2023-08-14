***********************************************************************
***********************************************************************
WINDOWS
***********************************************************************
***********************************************************************

1. Install Python:
>Download the python installer from the official site:
https://www.python.org/downloads/windows/

>Run the installer and make sure to check the "Add Python X.X to PATH" box (X.X represents the version of Python you are installing).
     Click "Install Now" to start the installation.

2. Open the command line:
>Open the start menu and search for "Command Prompt" or "CMD".
>Right click on "Command Prompt" and choose "Run as administrator" to make sure you have the necessary permissions.

3. Update pip and setuptools:

python -m pip install --upgrade pip setuptools


4. Install virtualenv:

pip install virtualenv


5. Create and activate a virtual environment:

>Navigate to the folder where you want to create your project (you can use the cd command to change directories).
   
>Create a new virtual environment with the following command:

virtualenv environment_name


>Activate the virtual environment:

environment_name\Scripts\activate

6. Install libraries:
Now that you are in the virtual environment, you can install the necessary libraries. For example, to install Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn:

pip install pandas numpy matplotlib seaborn scikit-learn


7. Create requirements.txt file:

>Create a file called requirements.txt in the root of your project.
>Open the file with a text editor and list the libraries and their versions, one per line:

pandas==1.3.1
numpy==1.21.1
matplotlib==3.4.3
seaborn==0.11.1
scikit-learn==0.24.2


8. Save the virtual environment and requirements.txt:

>To save the virtual environment and installed libraries to the requirements.txt file, run:


pip freeze > requirements.txt


9. Deactivate the virtual environment:
>When you have finished working on your project, you can disable the virtual environment with the following command:

deactivate


***********************************************************************
***********************************************************************
LINUX
***********************************************************************
***********************************************************************

1. Install Python:
>Most Linux distributions already come with Python pre-installed. To verify, open a terminal and type:

python3 --version


If Python is not installed, you can install it from your distribution's package manager. For example, on Ubuntu:

sudo apt-get update
sudo apt-get install python3

2. Open the terminal:

3. Update pip and setuptools:


python3 -m pip install --upgrade pip setuptools


4. Install virtualenv:

pip3 install virtualenv


5. Create and activate a virtual environment:

> Navigate to the folder where you want to create your project (you can use the cd command to change directory).
> Create a new virtual environment with the following command:

python3 -m venv environment_name


>Activate the virtual environment:

source environment_name/bin/activate


6. Install libraries:

>Now that you are in the virtual environment, you can install the necessary libraries. For example, to install Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn:


pip install pandas numpy matplotlib seaborn scikit-learn




7. Create requirements.txt file:
Create a file called requirements.txt in the root of your project.
Open the file with a text editor and list the libraries and their versions, one per line:

pandas==1.3.1
numpy==1.21.1
matplotlib==3.4.3
seaborn==0.11.1
scikit-learn==0.24.2


8. Save the virtual environment and requirements.txt:
>To save the virtual environment and installed libraries to the requirements.txt file, run:

pip freeze > requirements.txt

9. Deactivate the virtual environment:

>When you have finished working on your project, you can disable the virtual environment with the following command:

deactivate

