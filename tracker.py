import requests
from bs4 import BeautifulSoup
import smtplib

URL= "https://www.amazon.in/ASUS-17-3-inch-GTX-1650-Graphics-G713IH-HX020T/dp/B09CBZFPZR/ref=sr_1_1_sspa?crid=2VBXKNQ0UFJZQ&dchild=1&keywords=asus+rog+strix+g15&qid=1635411126&sprefix=asus+rog+strix%2Caps%2C301&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRllFMjA5WDdZTTM4JmVuY3J5cHRlZElkPUEwNDM5MDU4M1JNSVlKR0s1WUJMTCZlbmNyeXB0ZWRBZElkPUEwNzY0Mzc5MlFTRE82SkRLRTAzNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


def check_price():
    page= requests.get(URL,headers=headers)
    soup= BeautifulSoup(page.content,"html.parser") 

    title= soup.find(id="productTitle").get_text()

    price= soup.find(id="priceblock_dealprice").get_text()
    without_comma=price.replace(',','')
    converted_price=float(without_comma[1:])

    if(converted_price>70000.0):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("from@gmail.com","password")

    subject="Price fell down!"
    body="Check this out: https://www.amazon.in/ASUS-17-3-inch-GTX-1650-Graphics-G713IH-HX020T/dp/B09CBZFPZR/ref=sr_1_1_sspa?crid=2VBXKNQ0UFJZQ&dchild=1&keywords=asus+rog+strix+g15&qid=1635411126&sprefix=asus+rog+strix%2Caps%2C301&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRllFMjA5WDdZTTM4JmVuY3J5cHRlZElkPUEwNDM5MDU4M1JNSVlKR0s1WUJMTCZlbmNyeXB0ZWRBZElkPUEwNzY0Mzc5MlFTRE82SkRLRTAzNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
    msg= f"Subject:{subject}\n\n{body}"
    server.sendmail(
        "from@gmail.com",
        "to@gmail.com",
        msg
    )
    print("MESSAGE SENT!")

    server.quit()    

check_price()