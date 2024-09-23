# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:46:55 2022

@author: Jesung
"""

from discordwebhook import Discord
def discord(): 
    read = open("discordlink.txt", 'r')
    urlst = read.read()
    discord = Discord(url=urlst)
    read.close()
    return discord

Discordlink = discord()
from requests_html import HTMLSession
from time import sleep
session = HTMLSession()
def link():
    read = open("link.txt", "r")
    url = str(read.read())
    read.close()
    return url
def notify(discord, input):
    discord.post(content=input)


linkstr = str(link())
r = session.get(linkstr)
fixedtitle = str(r.html.xpath('//*[@id="srp-river-results"]/ul/li[2]/div/div[2]/a/div/span/text()')[0])
dupfixedtitle = fixedtitle
sleep(1)
while True:
    try:
        r = session.get(linkstr)
        sleep(1)
        title = r.html.xpath('//*[@id="srp-river-results"]/ul/li[2]/div/div[2]/a/div/span/text()')[0]
        sleep(1)
        priced= r.html.xpath('//*[@id="srp-river-results"]/ul/li[2]/div/div[2]/div[2]/div[1]')
        sleep(1)
        for j in priced:
            prices = j.text


        if dupfixedtitle != title:
            links = []
            link = r.html.find("a.s-item__link:link, a.s-item__link:hover, a.s-item__link:focus, a.s-item__link:active")
            links2 = ' '.join(map(str, link))
            joined = links2.split()
            i = 0
            while i < len(joined):
                if 's-item__link' in joined[i]:
                    f = str(joined[i+1])
                    f=f.replace("href='", '')
                    f=f.replace("'>", '')
                    links.append(f)
                i += 1
                
            notify(Discordlink, ("@Scalaperfetta" + "     "+ title + "     " +  prices))
            sleep(1)
            notify(Discordlink,"[Link]("+links[1]+")")
            sleep(1)
            dupfixedtitle = title
            sleep(5)

        print(dupfixedtitle)
        print(title+prices)

        sleep(20)
        continue
    except:
        continue

