import re
import requests

url = 'https://www.lotto.pl/'
response = requests.get(url)

text = response.text
pattern = '\s<span>(\d{1,2})<\/span>'

match = re.findall(pattern, text)
if match:
    print(match[:6])