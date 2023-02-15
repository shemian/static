# STATIC SITE GENERATOR
This is a simple Python script that converts Markdown files to HTML files.
The script is designed to be flexible and configurable, allowing you to specify the folder where your Markdown files are located and automatically converting them to HTML files.

## Requirements 
This are the requirements for running the Static Site Generator 
* Python 3 
* Markdown2 module 
* json
* jinja2 module


# Usage
1. Download or clone the repository to your Machine.

        git clone https://github.com/shemian/static.git

2. Navigate to the project folder then  activate the virtual Envrionment 
    
    In Windows Run:

        source env/Scripts/activate

    In MacOs Run:
         
        source env/bin/activate


3. Make sure markdown2 and Jinja2 module are installed.
        
        pip install markdown2 Jinja2 



4. Run `script.py` to start the program.

        python3 script.py


Note: If you've installed Python 3 using a method other than Homebrew, you might need to type python in the second command instead of python3.


## Configuration
The application reads a configuration file config.json to determine the paths to the input markdown files, images, and templates. Here's an example config.json file

    `
    {
    "folder_path": "./markdowns",
    "image_path": "./assets/images",
    "template_path": "./templates"
    }

    `

* `folder_path` : specifies the path to the folder containing the input markdown files.
* `image_path` : specifies the path to the folder containing any images used in the markdown files.
* `template_path`:  specifies the path to the folder containing the Jinja2 templates.

`Note` :Make sure to update the paths in config.json to match the paths on your local machine.

## File Structure 
* `markdowns` : This directory contain the markdown files.

* `templates` : This directory contains the HTML files.

* `templates/base.html` : This is the main html file that the other generated .html files inherit from 

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