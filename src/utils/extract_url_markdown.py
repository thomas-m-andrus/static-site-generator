import re

def extract_markdown_images(text:str):
    pattern = r"!\[((?:\w+\s+)*\w+)\]\((https?:\/\/.+?)\)"
    matches = re.findall(pattern, text, 0)
    return matches

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def extract_markdown_links(text:str):
    pattern = r"(?<!!)\[((?:\w+\s+)*\w+)\]\((https?:\/\/.+?)\)"
    matches = re.findall(pattern, text, 0)
    return matches

