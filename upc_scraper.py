"""
This script scrapes the ecommerce website Amazon.in for the product details of the product with the UPC code 190198000000.
"""


from requests_html import HTMLSession
from DB import queries, db

conn = db.cheapifydb_Connect()

url = 'https://www.amazon.in/s?k=iphone'
session = HTMLSession()
r = session.get(url)

r.html.render(sleep=1, scrolldown=1)

prices = []
amazon_price = r.html.find('span.a-price-whole')
amazon_title = r.html.find('a-color-base.a-text-normal')
for title in amazon_title:
    print(title.text)

for price in amazon_price:
    number = int(price.text.replace(',', ''))
    prices.append(number)
products = r.html.find('div[data-asin]')
asins = []
for product in products:
    if product.attrs['data-asin'] != '':
        asins.append(product.attrs['data-asin'])
    # asins.append(product.attrs['data-asin'])


print(asins)
print(len(asins))
print(min(len(amazon_price), len(amazon_title), len(asins)))

for i in range(min(len(amazon_price), len(amazon_title), len(asins))):
    message =  db.fetch(conn, queries.insert_product.format(asins[i], amazon_title[i].text, f"amazon.in/s?q={amazon_title[i].text}", "https://m.media-amazon.com/images/I/31qeR3U2bdL._SX342_SY445_.jpg", 'amazon', 'mobile phones', int(amazon_price[i].text)))
    print(message)
    
db.close(conn)
