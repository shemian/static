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

    
    {
    "folder_path": "./markdowns",
    "image_path": "./assets/images",
    "template_path": "./templates"
    }

    

* `folder_path` : specifies the path to the folder containing the input markdown files.
* `image_path` : specifies the path to the folder containing any images used in the markdown files.
* `template_path`:  specifies the path to the folder containing the Jinja2 templates.

`Note` :Make sure to update the paths in config.json to match the paths on your local machine.

## File Structure 
* `markdowns` : This directory contain the markdown files.

* `templates` : This directory contains the HTML files.

* `templates/base.html` : This is the main html file that the other generated .html files inherit from 

## Creating Content
* To create new content and add it to the site, Create a new markdown file in the `markdowns` directory for instance `example.md` 

* The start the program by running 
     
     python3 script.py

* corresponding HTML file will be created and stored in the `templates` folder with the same name and a `.html` extension. For example, a Markdown file named `example.md` will be converted to an HTML file named `example.html`.

* Navigate to the `templates` folder and include the file you have created in the `base.html` for instance in the navigation bar 
        
        <nav class="navbar navbar-expand-lg navbar navbar-light" style="background-color: #e3f2fd;">
            <div class="container">
                <a class="navbar-brand" href="base.html">Staic Site Generator</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="base.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="example.html">Example Page</a></li>
                    </ul>
                </div>
            </div>
        </nav>

         


## Error Handling 
The Script also  includes error andling for the following scenarios:
` 
. Missing configuration file
. Invalid JSON format in configuration file
. Missing Markdown files
. Other errors that may occur during the conversion process

`
In the event of an error, a descriptive error message will be displayed in the terminal or command prompt.

## Notes 
The script uses the `markdown2` library to convert the Mardowns to HTML 
The script only converts files with a `.md` extension. Other files in the folder will be ignored.

# Credits
The template at `https://startbootstrap.com/themes/blog-news` was used for this project.


## Contributions
If you find a bug or would like to suggest a feature, please create a new issue or pull request. Your contributions are greatly appreciated!

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.