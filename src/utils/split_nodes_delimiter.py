from textnode import TextNode, TextType


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
                

        
