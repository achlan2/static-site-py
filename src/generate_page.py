from markdown_to_html import markdown_to_html_node
from extract import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    markdown = ""
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
        with open(template_path, 'r', encoding="utf-8") as t_file:
            template = t_file.read()

            res_html = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            template = template.replace('{{ Title }}', title)
            template = template.replace('{{ Content }}', res_html)
            template = template.replace('href="/', f'href="{basepath}')
            template = template.replace('src="/', f'href="{basepath}')

            try:

                with open(dest_path, 'x', encoding="utf-8") as d_f:
                    d_f.write(template)
                print('file successfully created')
            except FileExistsError:
                print("File already exists")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for dirpath, dirnames, filenames in os.walk(dir_path_content):
        relative_path = os.path.relpath(dirpath, dir_path_content)

        dest_path = os.path.join(dest_dir_path, relative_path)
        os.makedirs(dest_path, exist_ok=True)

        for filename in filenames:
            f_name = filename.replace('.md', '.html')
            file_path = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest_path, f_name)
            generate_page(file_path, template_path, dest_file, basepath)
