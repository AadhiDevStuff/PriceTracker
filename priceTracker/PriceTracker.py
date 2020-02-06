import smtplib
import requests
from bs4 import BeautifulSoup

URL = """https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i7/dp/B07SDPRFCM/ref=sr_1_1_ 
      sspa?crid=QP1K2HL85YP&keywords=macbook+pro+15+inch&qid=1580525432&sprefix=Macbook%2Caps%2C335&sr=8-1- 
      spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBWFJDQ1hHNTFIU1cmZW5jcnlwdGVkSWQ9QTAxNjA2MTIzN0dGU1U1UzJQVEh 
      HJmVuY3J5cHRlZEFkSWQ9QTEwMTE2MjIxTDlLNjBBVUFaUkc2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="""

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

maxProductPrice = float(200000)


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product = soup.find(id="productTitle").get_text()
    productPrice = soup.find(id='priceblock_ourprice').get_text()

    productPrice = productPrice.replace(',', '')
    productPrice = productPrice.replace('₹', '')
    convertedINR = float(productPrice)

    print(product.strip())
    print(convertedINR)

    if convertedINR < maxProductPrice:
        sendMail()

def sendMail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('codethorn@gmail.com','pmedvzobtuukmsag')

    subject = "Price Fell down!"
    body = """ Check the amazon link: https://www.amazon.in/Apple-MacBook-Pro-9th-Generation-Intel-Core-i7/dp/B07SDPRFCM/ref=sr_1_1_ 
      sspa?crid=QP1K2HL85YP&keywords=macbook+pro+15+inch&qid=1580525432&sprefix=Macbook%2Caps%2C335&sr=8-1- 
      spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBWFJDQ1hHNTFIU1cmZW5jcnlwdGVkSWQ9QTAxNjA2MTIzN0dGU1U1UzJQVEh 
      HJmVuY3J5cHRlZEFkSWQ9QTEwMTE2MjIxTDlLNjBBVUFaUkc2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="""

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'codethorn@gmail.com',
        'ms.aadeshwar@gmail.com',
        msg
    )

    print("Email has been sent")

    server.quit()

check_price()





