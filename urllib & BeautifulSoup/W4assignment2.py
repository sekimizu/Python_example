from bs4 import BeautifulSoup
import urllib.request
import ssl

def main():
    # create context
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    url = input("Enter URL:")
    count = int(input("Enter count:"))
    pos = int(input("Enter position:"))

    # i is 0, first capture.
    for i in range(count + 1):
        if i is 0 or len(spans) >= pos:
            if i > 0:
                url = spans[pos - 1].get('href', None)
            if url is not None:
                print("Retrieving:", url)
                html = urllib.request.urlopen(url, context = ctx).read()
                soup = BeautifulSoup(html, "html.parser")
                spans = soup.find_all("a")


if __name__ == '__main__':
    main()