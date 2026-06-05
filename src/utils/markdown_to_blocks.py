def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = markdown.split('\n\n')
    result = []
    for block in blocks:
        cleaned_block = block.strip()
        if len(cleaned_block) > 0:
            result.append(cleaned_block)
    return result