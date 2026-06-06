import os
import re
import shutil
from textnode import TextNode

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



def main():
    copy_src_directory_to_destination()

main()