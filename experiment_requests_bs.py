import requests
from bs4 import BeautifulSoup
import re
def prettify_output(html, tag):
    html = re.sub(f'[ \n]+<{tag}>[ \n]+',f'<{tag}>', html)
    html = re.sub(f'[ \n]+</{tag}>[ \n]+',f'</{tag}>', html)
    return html


if __name__ == '__main__':
    # https://www.amazon.in/s?k=headphones to get headphones wala webpage
    website = requests.get('https://www.amazon.in/s?k=headphones')
    soup = BeautifulSoup(website.content, 'html.parser')
    print(soup.title)
    print(str(soup.pr))
    file = open('amazon.html', 'w')
    file.write(str(website.content))
    file.close()
    print(soup.prettify())
