##
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/computers/printers-inks/printers/epson~brand/pr?sid=6bo,ffn,t64&otracker=clp_metro_expandable_3_4.metroExpandable.METRO_EXPANDABLE_Epson_printer-inks-store_Q15SM7PLHL&fm=neo%2Fmerchandising&iid=M_66120718-6d6a-4e22-8cda-bb35d84493a4_3.Q15SM7PLHL&ppt=Homepage&ppn=Homepage"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'lxml')
containers = soup.find_all("div",class_= "_3liAhj _1R0K0g")

filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Price\n"
f.write(headers)

for container in containers:
    product = container.findAll("a", class_ = "_2cLu-l")
    #actprice = container.findAll("div", class_ = "_3auQ3N")
    discprice = container.findAll("div", class_ = "_1vC4OE")
    productname = product[0].text
    productname = productname.replace(",", "|")
    #actualprice = actprice[0].text
    discountedprice = discprice[0].text
    discountedprice = discountedprice.replace("\u20b9", "Rs")
    discountedprice = discountedprice.replace(",", "")
    print(productname)
    #print(actprice)
    print(discountedprice)
    f.write(productname + "," + discountedprice + "\n")
f.close()

