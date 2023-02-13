#import os , json and Markdown modules
import os
import markdown2
import json

def read_config(config_file): # Reads the Configuration File and returns the dictionary 
    try:
        with open(config_file) as configuration_file:
            config = json.load(configuration_file)
            return config
    except FileNotFoundError:
        print(f'Error: Configuration file {config_file} not found.')
        return None
    except json.JSONDecodeError as error:
        print(f'Error decoding JSON: {error}')
        return None


def convert_md_to_html(folder_path):
    for filename in os.listdir(folder_path): #loop through all the files as specified by `folder_path`
        if filename.endswith('.md'): # check if the file ends with an `.md` , then convert it to HTML
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as file: #open the file in read mode 
                    markdown_text = file.read() 
                    html = markdown2.markdown(markdown_text) #the markdown library converts the md file to HTML
                    html_filename = filename.replace('.md', '.html') #Replace the .md expension with the .html to get the html files
                    html_file_path = os.path.join(folder_path, html_filename)# Constructing the full HTML file path by joining the `folder_path` and `html_filename`
                    with open(html_file_path, 'w') as html_file: #open the HTMl file in write Mode
                        html_file.write(html)
                        print(f'Converted {filename} to {html_filename}')

            except FileNotFoundError:
                 print(f'Error: Markdown file {file_path} not found.')
            except Exception as error:
                print(f'Error converting file {filename}: {error}')

def main():
    config_file = 'config.json'
    config = read_config(config_file)

    if config:
        folder_path = config['folder_path']
        if os.path.isdir(folder_path):
            convert_md_to_html(folder_path)

        else:
            print(f'Error: Folder {folder_path} not found.')
if __name__ == '__main__':
    main()

