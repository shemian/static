# STATIC SITE GENERATOR
A simple Python script to convert markdown files to HTML files. 
The script takes a folder path as an input and converts all the files with ".md" extension in that folder to HTML files.

## Requirements 
Python 3 
Markdown2 module 

# Usage
1. Download or clone the repository to your Machine.
2. Make sure 'markdwon2` module is installed as well by running `pip install markdwon2`.
2. Navigate to the repository where the project is stored.
3. Run `script.py` to start the program. 

Once you have the requirements installed, you can run the script as follows:

## Windows 
1. Download or clone the repository to your local machine.
2. Open the Command Prompt and navigate to the directory where the script is located.
3. Run the following command to convert the markdown files in the `markdowns` directory to HTML files:
`python3 script.py`.
Note: Replace the  'project-root' with the path to the root folder of the project.


> cd 'project-root' 
> python3 venv env  //install the virtual env.
> python3 -m pip install --user virtualenv // if the first one fails.
> env\Scripts\activate //activate the virtual environment.

Run `python3 script.py`.

## MacOS
1. Download or clone the repository to your local machine.
2. Open the Command Prompt and navigate to the directory where the script is located.
3. Run the following command to convert the markdown files in the `markdowns` directory to HTML files:
`python3 script.py`.
Note: Replace the  'project-root' with the path to the root folder of the project.

$ cd 'project-root'
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt



Note: If you've installed Python 3 using a method other than Homebrew, you might need to type python in the second command instead of python3.
