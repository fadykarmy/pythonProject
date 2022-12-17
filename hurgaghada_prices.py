import requests
import bs4
#import csv
#from itertools import zip_longest
import pandas as pd

"""
Itertools is a module in Python that enables fast,
 and memory-efficient iteration over iterable data structures.
"""

url="https://www.olx.com.eg/properties/hurghada/q-%D8%B9%D9%82%D8%A7%D8%B1%D8%A7%D8%AA-%D8%A7%D9%84%D8%BA%D8%B1%D8%AF%D9%82%D9%87/"
page = requests.get(url)
#page.encoding=page.apparent_encoding
wbdata=page.content
#print(wbdata)
soup=bs4.BeautifulSoup(wbdata,"html.parser")
#print(soup)

home_name,home_price,link,details,home_summary=[],[],[],[],[]
homes_names=soup.find_all("div",{"class":"a5112ca8"})
#print(soup.find_all("div",{"class":"a5112ca8"}))
homes_prices=soup.find_all("div",{"class":"_52497c97"})
homes_links=soup.find_all("article",{"class":"_7e3920c1"})
#print(homes_prices)


for i in range(len(homes_names )):
        home_name.append(homes_names[i].text)
        home_price.append(homes_prices[i].text)
        lin="https://www.olx.com.eg"+homes_links[i].find("a").attrs['href']
        link.append(lin)

for linknum in link:
        page = requests.get(linknum)
        wbdata = page.content
        soup = bs4.BeautifulSoup(wbdata, "html.parser")
        summary=soup.find("div",{"class":"_0f86855a"}).span
        home_summary.append(summary.text)

   #    detail=soup.find("div",{"class":"_59317dec"})
   #      update_detail=detail.text.split()
   #     details.append(update_detail)


dataRepresent={
          "المنزل " : home_name
          ,"السعر ": home_price
       #  ,"الوصف":details
         ,"التفاصيل":home_summary
        ,"رابط المنزل ":link


        #,"التفاصيل ": home_summary
}
#print(len(home_summary))
#print(len(link))
df=pd.DataFrame(dataRepresent)
df.to_csv("OLX-dataset_hur_prices.csv",index=False,encoding='utf-8-sig')






"""
for i in range(len(home_price)):
   "" print (home_name[i])
    print (home_price[i])
    print (summary[i])
    print (detail[i])
    print (link[i])
"""



"""
#last_list =[home_name,home_price]
#paired_data=zip_longest(*last_list)
with open ("OLX_hurghada_prices.csv","w") as myfile:
   writer= csv.writer(myfile)
     # (*) to unback data in data structure
   #zip_logest use to pair data proveded in list
   writer.writerow(["Home Name","Home Price"])
   writer.writerows([home_name,home_price])
f=open("l.csv")
"""