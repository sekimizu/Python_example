from bs4 import BeautifulSoup
import urllib.request
import ssl

def main():
    # create context
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    _sum = 0

    #url = "http://py4e-data.dr-chuck.net/comments_42.html"
    #url = "http://py4e-data.dr-chuck.net/comments_75926.html"
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    spans = soup.find_all("span")
    for item in spans:
        #print(item.string)
        _sum += int(item.string)

    print(_sum)

if __name__ == '__main__':
    main()