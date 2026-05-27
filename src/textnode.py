from enum import Enum
'''
text (plain)
**Bold text**
_Italic text_
`Code text`
Links, in this format: [anchor text](url)
Images, in this format: ![alt text](url)
'''
class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():

    def __init__(self, content: str, type: TextType, url: str | None = None):
        self.text = content
        self.text_type = type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        