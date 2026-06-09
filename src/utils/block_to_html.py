import re
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from utils.block_to_block_type import block_to_block_type, BlockType
from utils.markdown_to_blocks import markdown_to_blocks
from utils.split_nodes_delimiter import text_to_textnodes

def compile_html_list_children(prefix: str,block: str):
    children = []
    rm_new_line = block.split('\n')
    for child in rm_new_line:
        child = text_to_textnodes(re.sub(prefix, '', child))
        child_segments = []
        for segment in child:
            child_segments.append(text_node_to_html_node(segment))
        children.append(ParentNode('li', child_segments))
    return children

def remove_redundant_space(text:str):
    return re.sub(r'\s{2,}', ' ', text)

def create_block_node(block:str):
    block_type = block_to_block_type(block)
    tag = ''
    raw_children = []
    children = []
    match block_type:
        case BlockType.PARAGRAPH:
            tag = 'p'
            raw_children = text_to_textnodes(remove_redundant_space(block.replace('\n', ' ')))
            children = []
            for child in raw_children:
                children.append(text_node_to_html_node(child))
        case BlockType.QUOTE:
            tag = 'blockquote'
            cleaned = re.sub(r'(^> ?|\n>)','',block)
            raw_children = text_to_textnodes(remove_redundant_space(cleaned))
            children = []
            for child in raw_children:
                children.append(text_node_to_html_node(child))
        case BlockType.UNORDERED_LIST:
            tag = 'ul'
            children = compile_html_list_children("- ", block)
        case BlockType.ORDERED_LIST:
            tag = 'ol'
            children = compile_html_list_children(r"^\d+\. ", block)
        case BlockType.HEADING:
            prefix = re.search(r"^#{1,6} ", block)
            h_number = len(re.findall("#",prefix.group()))
            tag = f"h{h_number}"
            content = re.sub(r"^#{1,6} ", '', block)
            nodes = text_to_textnodes(content)
            for child in nodes: 
                children.append(text_node_to_html_node(child))
        case _:
            pass

    return ParentNode(tag,children)

def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is not BlockType.CODE:
            nodes.append(create_block_node(block))
        else:
            clean_code = block.replace('```\n','').replace('```','')
            clean_code = re.sub(r' {2,}', '', clean_code)
            code_node = TextNode(clean_code, TextType.CODE)
            nodes.append(ParentNode('pre', [text_node_to_html_node(code_node)]))
    return ParentNode('div', nodes)
        


        
