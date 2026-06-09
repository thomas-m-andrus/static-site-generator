import os
import re
import shutil
from textnode import TextNode
from utils.block_to_html import markdown_to_html_node
from utils.extract_title import extract_title

'''
os.path.exists
os.listdir
os.path.join
os.path.isfile
os.mkdir
shutil.copy
shutil.rmtree
'''

def get_spaces(path: str):
    number_of_spaces = path.count('/')
    spaces = ''
    for _ in range(number_of_spaces):
        spaces = f"{spaces}    "
    return spaces

def copy_src(pathSrc: str, pathDestination: str):
    if not os.path.exists(pathSrc) or len(os.listdir(pathSrc)) == 0:
        return
    if not os.path.exists(pathDestination):
        print(f"{get_spaces(pathDestination)}create '{pathDestination}'")
        os.mkdir(pathDestination)
    contents = os.listdir(pathSrc)
    for content in contents:
        updated = {
            "src": os.path.join(pathSrc, content),
            "destination": os.path.join(pathDestination, content)
        }
        if os.path.isfile(updated['src']):
            print(f"{get_spaces(updated['destination'])}copy '{updated['src']}' -> '{updated['destination']}'")
            shutil.copy(updated['src'], updated['destination'])
        else:
            copy_src(updated['src'], updated['destination'])
    

def copy_src_directory_to_destination():
    print(os.listdir('.'))
    public_path = './public'
    public_exists = os.path.isdir(public_path)
    if public_exists:
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    static_path = './static'
    static_exists = os.path.isdir(static_path)
    if static_exists:
        copy_src(static_path, public_path)

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path).read()
    template_file = open(template_path,"r").read()
    md = markdown_to_html_node(from_file)
    html = md.to_html()
    title = extract_title(from_file)
    template_file = template_file.replace("{{ Title }}", title).replace("{{ Content }}",html)
    print(template_file)
    path = os.path.dirname(dest_path)
    print(path, os.path.exists(path))
    if path != '' and not os.path.exists(path):
        os.makedirs(path)
    try:
        with open(dest_path, 'x') as f:
            f.write(template_file)
    except FileExistsError:
        print("The file already exists.")
        



def main():
    copy_src_directory_to_destination()
    generate_page("./content/index.md","./template.html","public/index.html")

main()