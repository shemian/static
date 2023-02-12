#import os and Markdown modules
import os
import markdown2

folder_path = './markdowns' # Setting the `folder_path` to './markdowns'

def convert_md_to_html(folder_path):
    for filename in os.listdir(folder_path): #loop through all the files as specified by `folder_path`
        if filename.endswith('.md'): # check if the file ends with an `.md` , then convert it to HTML
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file: #open the file in read mode 
                markdown_text = file.read() 
                html = markdown2.markdown(markdown_text) #the markdown library converts the md file to HTML

                html_filename = filename.replace('.md', '.html') #Replace the .md expension with the .html to get the html files
                html_file_path = os.path.join(folder_path, html_filename)# Constructing the full HTML file path by joining the `folder_path` and `html_filename`
                with open(html_file_path, 'w') as html_file: #open the HTMl file in write Mode
                    html_file.write(html)


convert_md_to_html(folder_path) #calling the function and passing the arguments