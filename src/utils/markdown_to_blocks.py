def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = markdown.split('\n\n')
    result = []
    for block in blocks:
        if len(block) > 0:
            result.append(block.strip())
    return result