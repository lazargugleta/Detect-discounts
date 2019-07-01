import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Kiebel-Gamer-PC-Goliath-184395-10x3-3GHz/dp/B003VN4BP8?pf_rd_p=012efe24-acb3-45ca-a485-03c9c1dfafdb&pd_rd_wg=u32Ls&pf_rd_r=3F00TKW241EPFY07J314&ref_=pd_gw_cr_wsim&pd_rd_w=YOyl5&pd_rd_r=e0787d9d-0a3c-460f-a050-1d6be6be2bf8&th=1'

headers = {"User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    sep = ','
    con_price = price.split(sep, 1)[0]
    converted_price = int(con_price.replace('.',''))

    print(converted_price)
    print(title.strip())

    if (int(converted_price) < 2000):
        send_mail()



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lazar.gugleta@gmail.com','lafydtbsoiufkwye')

    subject = 'Price fell down!'

    body = 'Check the amazon link: https://www.amazon.de/Kiebel-Gamer-PC-Goliath-184395-10x3-3GHz/dp/B003VN4BP8?pf_rd_p=012efe24-acb3-45ca-a485-03c9c1dfafdb&pd_rd_wg=u32Ls&pf_rd_r=3F00TKW241EPFY07J314&ref_=pd_gw_cr_wsim&pd_rd_w=YOyl5&pd_rd_r=e0787d9d-0a3c-460f-a050-1d6be6be2bf8&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Price check',
        'lazar.gugleta@gmail.com',
        msg
    )
    print('Hey Email has been sent!')

    server.quit()
    
check_price()