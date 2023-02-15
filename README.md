# STATIC SITE GENERATOR
This is a simple Python script that converts Markdown files to HTML files.
The script is designed to be flexible and configurable, allowing you to specify the folder where your Markdown files are located and automatically converting them to HTML files.

## Requirements 
This are the requirements for running the Static Site Generator 
* Python 3 
* Markdown2 module 
* json
* jinja2 module

## Configuration
The script reads a configuration file in JSON format to specify the folder where your Markdown files are located. The file should contain a single JSON object with the following structure: 
`
{
    "folder_path": "./markdowns"
}
`
Replace ./markdowns with the path to the folder where your Markdown files are located.


# Usage
1. Download or clone the repository to your Machine.

        git clone https://github.com/shemian/static.git

2. Make sure 'markdwon2  `module is installed as well by running` pip install markdwon2`.
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

## Error Handling 
The Script also  includes error andling for the following scenarios:
` 
. Missing configuration file
. Invalid JSON format in configuration file
. Missing Markdown files
. Other errors that may occur during the conversion process

`
In the event of an error, a descriptive error message will be displayed in the terminal or command prompt.

## Output 
For each Markdown file, a corresponding HTML file will be created in the same folder with the same name and a `.html` extension. For example, a Markdown file named `example.md` will be converted to an HTML file named `example.html`.

## Notes 
The script uses the `markdown2` library to convert the Mardowns to HTML 
The script only converts files with a `.md` extension. Other files in the folder will be ignored.
The template for this project is available on `https://startbootstrap.com/themes/blog-news` 


## Contributions
If you find a bug or would like to suggest a feature, please create a new issue or pull request. Your contributions are greatly appreciated!