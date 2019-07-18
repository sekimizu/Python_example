import urllib.request
import xml.etree.ElementTree as ET
import ssl

def main():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    _sum = 0
    url = input('Enter location: ')
    #url = "http://py4e-data.dr-chuck.net/comments_42.xml"
    data = urllib.request.urlopen(url, context = ctx).read() #bytes
    #print(type(data))
    tree = ET.fromstring(data)
    """
    https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/processing-xml-in-python-with-element-tree.html
    """
    for elem in tree.iter(tag='count'):
        _sum += int(elem.text)
    print(_sum)    

if __name__ == "__main__":
    main()