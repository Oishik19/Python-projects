import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?keywords=ssd+external&qid=1573065104&s=computers&sr=1-3"
headers = {
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
def check_price():
    page= requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title= soup.find(id="productTitle").get_text()
    
   
    price=soup.find(id="priceblock_ourprice").get_text()
    
    concise_title=title.strip()[0:37]
    print(concise_title)

    rounded_price=price[2:7]
    rounded_price=float(rounded_price.replace(",", ""))
    print(rounded_price)
    if(rounded_price < 5900.0):
         send_mail()
    

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('oishikgoswami.10@gmail.com','dkvwggvdaczlxrxf')

    subject="price fell down"
    body='check the amazon link https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?keywords=ssd+external&qid=1573065104&s=computers&sr=1-3'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'oishikgoswami.10@gmail.com',
        'oishikgoswami.10@gmail.com',
        msg
    )
    print("email sent")
    
    server.quit()

while True:
    check_price()
    time.sleep(60 * 60)


