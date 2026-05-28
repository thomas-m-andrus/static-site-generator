class HTMLNode():

    def __init__(self, tag: str | None = None, value: str | None = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for key, value in self.props.items():
            result = f"{result} {key}=\"{value}\""
        return result
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"