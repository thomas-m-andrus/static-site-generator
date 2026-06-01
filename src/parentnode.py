from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError()
        if self.children is None or len(self.children) == 0:
            raise ValueError("Missing required children")
        content = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            content = f"{content}{child.to_html()}"
        return f"{content}</{self.tag}>"
    