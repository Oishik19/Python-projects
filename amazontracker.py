import requests
from bs4 import BeautifulSoup
import smtplib
import time

#link of the product, modify it before running
URL="https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?keywords=ssd+external&qid=1573065104&s=computers&sr=1-3"
#uncomment the line below and enter the user agent of your browser
#headers = {
    "user agent'}
def check_price():
    page= requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title= soup.find(id="productTitle").get_text()
    
   
    price=soup.find(id="priceblock_ourprice").get_text()
    
    concise_title=title.strip()[0:37]
    print(concise_title)

    #check the string slicing before you run the program, it's modified according to my needs.
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

    #uncomment the line below and enter email and password
    
    #server.login('email','password')

    subject="price fell down"
    
    #enter the link from amazon
    
    body='check the amazon link https://www.amazon.in/Samsung-500GB-Portable-Solid-State/dp/B074WZJ4MF/ref=sr_1_3?keywords=ssd+external&qid=1573065104&s=computers&sr=1-3'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'your email',
        'receivers email',
        msg
    )
    print("email sent")
    
    server.quit()

while True:
    check_price()
    time.sleep(60 * 60)


