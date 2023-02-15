import datetime
import time
import pywhatkit

import requests
from lxml import etree

result = requests.get('https://www.kijiji.ca/b-cats-kittens/ottawa/kitten/k0c125l1700185')
tree = etree.HTML(result.text)
links = tree.xpath(
    '/html/body/div[@id="MainContainer"]/div[@id="mainPageContent"]/div[@class="layout-3 "]/div[@class="col-2 "]/main/div/div/@data-vip-url')
# imgs = tree.xpath('/html/body/div[@id="MainContainer"]/div[@id="mainPageContent"]/div[@class="layout-3 "]/div[@class="col-2 "]/main/div/div/div/div[@class="left-col"]/div[@class="image"]/picture/source/@data-srcset')
# print(imgs)

result = requests.get('https://www.kijiji.ca/b-cats-kittens/ottawa/kitten/k0c125l1700185')
tree = etree.HTML(result.text)
prevLinks = tree.xpath(
    '/html/body/div[@id="MainContainer"]/div[@id="mainPageContent"]/div[@class="layout-3 "]/div[@class="col-2 "]/main/div/div/@data-vip-url')

while True:
    links = tree.xpath(
        '/html/body/div[@id="MainContainer"]/div[@id="mainPageContent"]/div[@class="layout-3 "]/div[@class="col-2 "]/main/div/div/@data-vip-url')
    for listing in links:
        if (listing not in prevLinks):
            pywhatkit.sendwhatmsg('+13435429907', listing, datetime.datetime.now().hour,
                                  datetime.datetime.now().minute + 1)
            # pywhatkit.sendwhatmsg('+16135136708', listing, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)

    prevLinks = links
    time.sleep(60)
