import re

text = 'Some long text with 30-415 post code somewhere in it.'
pattern = '\d{2}-\d{3}'

match = re.search(pattern, text)
if match:
    start_pos = match.start()
    end_pos = match.end()
    print(text[start_pos:end_pos])

