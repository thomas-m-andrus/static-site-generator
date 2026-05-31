from textnode import TextNode, TextType
from utils.extract_url_markdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    updated_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            updated_nodes.append(node)
        else:
            deconstructed = node.text.split(delimiter)
            delimiter_count = len(deconstructed) - 1
            if delimiter_count == 0:
                updated_nodes.append(node)
            elif delimiter_count % 2 == 1:
                raise ValueError(f"Incorrect markdown syntax: '{node.text}'")
            else:
                isDelimited = False
                for fragment in deconstructed:
                    if fragment != '':
                        updated_nodes.append(TextNode(fragment, text_type if isDelimited else TextType.TEXT, None))
                    isDelimited = not isDelimited
    return updated_nodes

def extract_next(result: list[str | int],text:str, patterns: list[str], idx: int = 0):
    if len(patterns) == 0:
        return result
    pattern = patterns[0]
    extracted = text.split(pattern,1)
    if len(extracted) == 1:
        raise ValueError(f"patterns do not align with text; text: '{text}', pattern: '{pattern}', idx: {idx}")
    if extracted == ['', '']:
        result.append(idx)
        return result
    result.extend([extracted[0], idx])
    if extracted[1] == '':
        return result
    return extract_next(result, extracted[1], patterns[1:], idx+1)
    

def split_url_nodes(extract_from_pattern, format_pattern, text_type: TextType):
    def split_nodes(old_nodes: list[TextNode]) -> list[TextNode]:
        updated_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                updated_nodes.append(node)
            else:
                text = node.text
                extracted = extract_from_pattern(text)
                if len(extracted) == 0:
                    updated_nodes.append(node)
                else:
                    patterns = []
                    for extract in extracted:
                        content, url = extract
                        patterns.append(format_pattern(content, url))
                    fragments = extract_next([], text, patterns)
                    for fragment in fragments:
                        if isinstance(fragment,str):
                            updated_nodes.append(TextNode(fragment, TextType.TEXT))
                        else:
                            content, url = extracted[fragment]
                            updated_nodes.append(TextNode(content, text_type, url))
        return updated_nodes
    return split_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_url_nodes(extract_markdown_links, lambda content, url: f"[{content}]({url})", TextType.LINK)(old_nodes)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return split_url_nodes(extract_markdown_images, lambda content, url: f"![{content}]({url})", TextType.IMAGE)(old_nodes)