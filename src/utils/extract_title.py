import re


def extract_title(markdown:str):
    match = re.match(r"^# .+",markdown)
    if not match:
        raise ValueError("Markdown missing title")
    return match.group().strip().replace("# ", "")