import requests
import re

res1 = requests.get('http://www.taiwantrade.com/products/search?word=facial%2Bmask&type=product&rows=100&style=supplier');
res2 = requests.get('http://www.taiwantrade.com/products/search?word=facial%2Bmask&type=product&page=2&rows=100&style=supplier');
result = res1.text + res2.text

email_regex = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', re.IGNORECASE)
emails = set()

processed_urls = set(re.findall(r'\/company\/.*\.html', result, re.I))
for val in processed_urls:
    company_page = requests.get('http://www.taiwantrade.com' + val)
    for email in email_regex.findall(company_page.text):
        emails.add(email)

for val in emails:
    print(val)

list = []
list.append('aaa@aaa.com')
list.append('bbb@bbb.com')
list.append('ccc@ccc.com')
#for index, val in enumerate(list):
#    print (val)