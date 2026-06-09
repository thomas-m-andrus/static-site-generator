import re

def extract_markdown_images(text:str):
    pattern = r"!\[(.+?)\]\((.+?)\)"
    matches = re.findall(pattern, text, 0)
    return matches

def extract_markdown_links(text:str):
    pattern = r"(?<!!)\[(.+?)\]\((.+?)\)"
    matches = re.findall(pattern, text, 0)
    return matches

