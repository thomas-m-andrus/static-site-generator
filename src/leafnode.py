from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag: str, value: str, props:dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"