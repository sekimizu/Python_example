import urllib.request
from bs4 import BeautifulSoup
import re

def main():
    html_doc = """
    <html><head><title>Hello World</title></head>
    <body><h2>Test Header</h2>
    <p>This is a test.</p>
    <a id="link1" href="/my_link1">Link 1</a>
    <a id="link2" href="/my_link2">Link 2</a>
    <p>Hello, <b class="boldtext">Bold Text</b></p>
    </body></html>
    """

    soup = BeautifulSoup(html_doc, 'html.parser')
    # dump all tree object
    #print(soup.prettify())
    """
    a_tags = soup.find_all(['a', 'p'])

    for tag in a_tags:
        print(tag.string)
        print(tag.get('href'))

    print("---------")

    target = soup.find(id = 'link2')
    print(target)
    print(dir(target))
    """
    links = soup.find_all('a', href=re.compile("^/(my_link)"), id='link2')
    print(links)
    
if __name__ == "__main__":
    main()