from enum import Enum
import re

# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.fullmatch(r"^#{1,6} .+", block):
        return BlockType.HEADING
    if re.match(r"^`{3}\n?(.|\n)+`{3}$", block):
        return BlockType.CODE
    if re.fullmatch(r"^(> ?[^ ].*)\n?(((> .+)|>)\n?)*", block):
        return BlockType.QUOTE
    if re.fullmatch(r"^(- [^ ].*\s)*- .+", block):
        return BlockType.UNORDERED_LIST
    if re.fullmatch(r"((\d+)\. .+\n)*(\d+\. .+)", block) and all(index + 1 == int(number)  for (index, (_, number)) in enumerate(re.findall(r"((\d+)\. .+)", block))):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    