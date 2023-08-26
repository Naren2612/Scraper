import requests

from requests import session
from bs4 import BeautifulSoup as BS
import re
s=session()
s.headers['user-agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0'
url='https://www.maccosmetics.in/product/13825/32212/products/skincare/primer/prep-prime-fix?shade=Coconut'
response = s.get(url)
soup = BS(response.text,"html.parser")
product_id = re.search('"PRODUCT_ID":"PROD(.*?)","',response.text).group(1)
print(product_id)

import requests
import pandas as pd
Maccosmetics_review_data = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.maccosmetics.in/',
    'Origin': 'https://www.maccosmetics.in',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

params = {
    'paging.from': '0',
    'paging.size': '10',
    'filters': '',
    'search': '',
    'sort': 'Newest',
    'image_only': 'false',
    'page_locale': 'en_IN',
    '_noconfig': 'true',
    'apikey': '1d01c6a1-3fb0-429d-9b01-7b3d915933af',
}

response = requests.get(
    'https://display.powerreviews.com/m/269258/l/all/product/103725/reviews',
    params=params,
    headers=headers,
)
js = response.json()
total_products = js['paging'].get('total_results')
print(total_products)
for paging in range(0,50,10):
    params = {
    'paging.from': ''+str(paging)+'',
    'paging.size': '10',
    'filters': '',
    'search': '',
    'sort': 'Newest',
    'image_only': 'false',
    'page_locale': 'en_IN',
    '_noconfig': 'true',
    'apikey': '1d01c6a1-3fb0-429d-9b01-7b3d915933af',
    }
    response = requests.get(
    'https://display.powerreviews.com/m/269258/l/all/product/103725/reviews',
    params=params,
    headers=headers,
    )
    jsd = response.json()
    detail = js['results'][0]['reviews']
    for reviews in detail:
        name = reviews['details'].get('nickname')
        date = reviews['details'].get('created_date')
        location = reviews['details'].get('location')
        review = reviews['details'].get('comments')
        d = {"NAME":name, "DATE":date, "LOCATION":location, "REVIEW":review}

        Maccosmetics_review_data.append(d)
        print(d)

df = pd.DataFrame(Maccosmetics_review_data)
df.to_excel("Maccosmetics_review_data.xlsx", index=False)