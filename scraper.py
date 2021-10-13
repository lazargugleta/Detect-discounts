import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

<<<<<<< HEAD
URL = 'https://www.amazon.de/gp/product/B0756CYWWD/ref=as_li_tl?ie=UTF8&tag=idk01e-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B0756CYWWD&linkId=18730d371b945bad11e9ea58ab9d8b32'
=======
URL = 'https://www.amazon.de/dp/B07XVWXW1Q/ref=sr_1_10?keywords=laptop&qid=1581888312&sr=8-10'
>>>>>>> update
def amazon_de():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
<<<<<<< HEAD
    price = soup.find(id="priceblock_ourprice").get_text()
=======
    price = soup.find(id="buyNew_noncbb").get_text()
>>>>>>> update
    sep = ','
    con_price = price.split(sep, 1)[0]
    converted_price = int(con_price.replace('.', ''))

    # price
    print(title.strip())
    print(converted_price)

    if (int(converted_price) < 200):
        send_mail()
    else:
        print("Price has not dropped!\n")


linked = 'https://www.edustore.at/lenovo-thinkvision-p44w-led-display-110-2-cm-43-4-zoll-ultrawide-full-hd-gebogen-matt-schwarz'
def edustore():
    page = requests.get(linked, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # title
    title = str(soup.find("h1").text)
    strip_price = str(soup.find("span", attrs={"class": "price"}))
    price = int(''.join(i for i in strip_price if i.isdigit()))

    print(title)
    print(price)

    if (price < 1000):
        send_mail()
    else:
        print("Price has not dropped!\n")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lazar.gugleta@gmail.com', 'lafydtbsoiufkwye')

    subject = 'Price fell down!'

    body = 'Check the link:\
  https://www.amazon.de/gp/product/B0756CYWWD/ref=as_li_tl?ie=UTF8&tag=idk01e-21&camp=1638&creative=6742&linkCode=as2&creativeASIN=B0756CYWWD&linkId=18730d371b945bad11e9ea58ab9d8b32'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Price check',
        'lazar.gugleta@gmail.com',
        msg
    )
    print('Hey Email has been sent!')

    server.quit()


amazon_de()
<<<<<<< HEAD
edustore()
=======
#edustore()
>>>>>>> update
