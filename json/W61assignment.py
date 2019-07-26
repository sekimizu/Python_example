import urllib.request
import json, ssl
#http://py4e-data.dr-chuck.net/comments_42.json

def main():
    _sum = 0

    # create ctx for https
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # get file from url
    #html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.json', context = ctx)
    html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_75929.json', context = ctx)
    # read body and decode from utf-8 to unicode
    context = html.read().decode()
    #print(context)

    # load json to Python
    tree = json.loads(context)
    for item in tree["comments"]:
        _sum += int(item["count"])
        #print(item["count"])

    print(_sum)

if __name__ == "__main__":
    main()