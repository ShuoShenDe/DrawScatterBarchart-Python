import asyncio
from pyppeteer import launch
from lxml import etree
#import pandas as pd
from intoMongo import Fangtianxia


async def main(url):
    mongo = Fangtianxia()
    browser = await launch({'headless': False,'dumpio':True,'excutablePath':r"E:\\pyppeteer\\local-chromium\Win_x64\\575458\\chrome.exe"})
    page = await browser.newPage()

    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.setViewport({'width': 1080, 'height': 960})
    await page.goto(url)
    await asyncio.sleep(3)
    response = etree.HTML(await page.content())
    divs = response.xpath("//div[@class='houseList']/dl")
    for div in divs:
        try:
            item = {}
            item['title'] = div.xpath("./dd/p[@class='title']/a/@title")[0]
            item['url'] = div.xpath("./dd/p[@class='title']/a/@href")
            if item['url']:
                item['url'] = 'http://cd.zu.fang.com/' + item['url'][0]
            item['type'] = div.xpath("./dd/p[2]/text()[1]")[0]
            if item['type']:
                item['type'] = item['type'].strip()
            item['nums'] = div.xpath("./dd/p[2]/text()[2]")[0]
            item['area'] = div.xpath("./dd/p[2]/text()[3]")[0]
            item['toward'] = div.xpath("./dd/p[2]/text()[4]")
            if item['toward']:
                item['toward'] = item['toward'][0].strip()
            item['price'] = div.xpath("./dd//span[@class='price']/text()")[0]
            item['address'] = div.xpath("./dd/p[3]/a[1]/span/text()")[0]
            print(item)
            mongo.process_item(item)
        except:
            print('error')

    next_url = await page.xpath("//div[@class='fanye']/a[text()='下一页']")
    while next_url:
        try:
            await next_url[0].click()
        except:
            pass
        await asyncio.sleep(3)
        try:
            response2 = etree.HTML(await page.content())
            divs = response2.xpath("//div[@class='houseList']/dl")
        except:
            print('eeee')
        for div in divs:
            try:
                item = {}
                item['title'] = div.xpath("./dd/p[@class='title']/a/@title")[0]
                item['url'] = div.xpath("./dd/p[@class='title']/a/@href")
                if item['url']:
                    item['url'] = 'http://cd.zu.fang.com/' + item['url'] [0]
                item['type'] = div.xpath("./dd/p[2]/text()[1]")[0]
                if item['type']:
                    item['type'] = item['type'].strip()
                item['nums'] = div.xpath("./dd/p[2]/text()[2]")[0]
                item['area'] = div.xpath("./dd/p[2]/text()[3]")[0]
                item['toward'] = div.xpath("./dd/p[2]/text()[4]")
                if item['toward']:
                    item['toward'] = item['toward'][0].strip()
                item['price'] = div.xpath("./dd//span[@class='price']/text()")[0]
                item['address'] = div.xpath("./dd/p[3]/a[1]/span/text()")[0]
                print(item)
                mongo.process_item(item)
            except:
                print('error')

        next_url = await page.xpath("//div[@class='fanye']/a[text()='下一页']")
        await asyncio.sleep(2)

url = 'https://cd.zu.fang.com/'
asyncio.get_event_loop().run_until_complete(main(url))
