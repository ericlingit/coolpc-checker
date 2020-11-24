import requests
from bs4 import BeautifulSoup

url = 'http://coolpc.com.tw/eachview.php?IGrp=12'

# Fetch
r = requests.get(url)
r.raise_for_status()

# Parse
soup = BeautifulSoup(r.text, 'lxml')

# Search
elems = soup.find_all(attrs={'class': 't'})

for e in elems:
    if '6800xt' in e.text.lower():
        if ('沒貨' not in e.text
                and '售完' not in e.text
                and '缺貨' not in e.text):
            # Notify
            print('AVAILABLE!')
        else:
            print(f'Not available: {e.text}')
