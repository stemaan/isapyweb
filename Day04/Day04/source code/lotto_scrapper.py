import requests

url = 'https://www.lotto.pl'
response = requests.get(url)
content = response.text
lotto_numbers_start_pos = content.find('resultsItem lotto')
result_number_pos = content.find('resultnumber', lotto_numbers_start_pos)

for i in range(6):
    span_pos1 = content.find('span', result_number_pos) + len('span>')
    span_pos2 = content.find('</span', span_pos1)

    print(content[span_pos1:span_pos2])
    result_number_pos = span_pos2 + len('span')


