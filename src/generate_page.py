from markdown_to_html import markdown_to_html_node
from extract import extract_title

def generate_page(from_path, template_path, dest_path):
    markdown = ""
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()
        with open(template_path, 'r', encoding="utf-8") as t_file:
            template = t_file.read()

            res_html = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            template = template.replace('{{ Title }}', title)
            template = template.replace('{{ Content }}', res_html)

            try:

                with open(dest_path, 'x', encoding="utf-8") as d_f:
                    d_f.write(template)
                print('file successfully created')
            except FileExistsError:
                print("File already exists")
