import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Kiebel-Gamer-PC-Goliath-184395-10x3-3GHz/dp/B003VN4BP8?pf_rd_p=012efe24-acb3-45ca-a485-03c9c1dfafdb&pd_rd_wg=u32Ls&pf_rd_r=3F00TKW241EPFY07J314&ref_=pd_gw_cr_wsim&pd_rd_w=YOyl5&pd_rd_r=e0787d9d-0a3c-460f-a050-1d6be6be2bf8&th=1'

headers = {"User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def amazon_de():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    sep = ','
    con_price = price.split(sep, 1)[0]
    converted_price = int(con_price.replace('.',''))

    #price
    print(title.strip())
    print(converted_price)

    if (int(converted_price) < 2000):
        send_mail()
    else:
        print("Price has not dropped!\n")

link = 'https://www.notebooksbilliger.de/lg+34um88+p/eqsqid/7e3681c6-f6be-4f28-a254-671d99b3eadd'

def notebooksbilliger():

    page = requests.get(link, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser') 

    #title
    strip_title = str(soup.find("h1"))
    strip_title1 = strip_title.replace('<h1 class="name squeezed">','')
    strip_title2 = strip_title1.replace('</h1>','')
    strip_title3 = strip_title2.replace('\n','')

    #price
    strip_price = soup.find("div", attrs={"id": "product_detail_price"})
    strip_price1 = str(strip_price.find(attrs = {"class": "nbb-svg-base"}))
    strip_price2 = strip_price1.replace("tspan dx=","")
    strip_price3 = strip_price2[47:]
    sep = ','
    price = int(strip_price3.split(sep,1)[0])

    print(strip_title3.strip())
    print(price)
    if (price < 300):
        send_mail()
    else:
        print("Price has not dropped!\n")

linked = 'https://www.edustore.at/lenovo-thinkvision-p44w-led-display-110-2-cm-43-4-zoll-ultrawide-full-hd-gebogen-matt-schwarz'

def edustore():
    page = requests.get(linked, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #title
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

  server.login(EMAIL,PASSWORD)

  subject = 'Price fell down!'

  body = 'Check the link:\
  https://www.amazon.de/Kiebel-Gamer-PC-Goliath-184395-10x3-3GHz/dp/B003VN4BP8?pf_rd_p=012efe24-acb3-45ca-a485-03c9c1dfafdb&pd_rd_wg=\
  u32Ls&pf_rd_r=3F00TKW241EPFY07J314&ref_=pd_gw_cr_wsim&pd_rd_w=YOyl5&pd_rd_r=e0787d9d-0a3c-460f-a050-1d6be6be2bf8&th=1'

  msg = f"Subject: {subject}\n\n{body}"

  server.sendmail(
   'Price check',
   'lazar.gugleta@gmail.com',
   msg
  )
  print('Hey Email has been sent!')

  server.quit()
   
notebooksbilliger()
amazon_de()
edustore()
