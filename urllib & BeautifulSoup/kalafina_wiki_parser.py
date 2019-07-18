import urllib.request
# pip install BeautifulSoup
from bs4 import BeautifulSoup
# pip install openpyxl
from openpyxl import Workbook
import re, ssl

def as_text(value):
    if value is None:
        return ""
    return str(value)

def main():
    # create ctx for https
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # create excel document
    wb = Workbook()
    ws = wb.active

    html = urllib.request.urlopen('https://zh.wikipedia.org/zh-tw/Kalafina', context = ctx)
    soup = BeautifulSoup(html, 'html.parser')

    #links = soup.find_all('tr', href=re.compile("^/(my_link)"), id='link2')
    tables = soup.find_all('table', {"class" : "wikitable"})
    #print("size = ", len(tables))
    for table in tables:
        tr_nodes = table.find_all('tr')
        for tr_item in tr_nodes:
            td_nodes = tr_item.find_all('td')
            if len(td_nodes) == 0:
                continue
            
            m_list = []
            for td_item in td_nodes:
                m_list.append(str(td_item.text).strip())
                #print(td_item)
            print(m_list)
            ws.append(m_list)

    #print(dir(ws.column_dimensions))
    wb.save('love.xlsx')
    
if __name__ == "__main__":
    main()