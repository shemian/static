import os
import markdown2

def convert_md_to_html(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                markdown_text = file.read()
                html = markdown2.markdown(markdown_text)

                html_filename = filename.replace('.md', '.html')
                html_file_path = os.path.join(folder_path, html_filename)
                with open(html_file_path, 'w') as html_file:
                    html_file.write(html)

folder_path = './markdowns'
convert_md_to_html(folder_path)