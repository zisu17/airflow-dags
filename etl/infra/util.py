import re

def clear_text(text):
    text = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text = re.sub('\u200b', ' ', text)
    text = re.sub('\n', '', text)
    text = re.sub('   ', ' ', text)
    text = re.sub('  ', ' ', text)
    return text
