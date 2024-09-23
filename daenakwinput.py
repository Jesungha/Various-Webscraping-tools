# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:04:08 2022

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

import selenium 
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.options import Options
slep = int(input(("Enter Sleep Time\n\n")))
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
link_to_message = str(input("Enter file name\n"))
driver = webdriver.Edge(executable_path= r'/Users/jesung/Downloads/msedgedriver.exe', options=options)


torf = True

def login():
    driver.find_element(By.NAME , "user_id").send_keys("")
    sleep(slep)
    driver.find_element(By.NAME, "password").send_keys("")
    sleep(slep)
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/form/button').click()

def notify(discord, input):
    discord.post(content=input)


def send(link):
    readthis = open(link, 'r', encoding="UTF-8")
    txtread = readthis.read()
    readthis.close()
    return txtread
def main(i, Discordlink, slep):    
    sleep(slep)
    title = driver.find_element(By.XPATH, '//*[@id="bd_5665468_0"]/div/table/tbody/tr['+i+']/td[2]/a[1]').text
    sleep(1)
    x1 = title.find("대낙")
    y1 = title.find("대금")
    z1 = title.find("머낙")
    z2 = title.find("신뢰의")
    if(x1 == -1 and y1 == -1 and z1 == -1):
        
        print("Not Found")
        sleep(10)
        return True
    elif(z2 != -1):
        print("wrong one")
        sleep(10)
        return True
    else:
        print("Found!\n")
        print(title)
        notify(Discordlink, "Daenak Found")
        login()
        sleep(slep)
        driver.find_element(By.XPATH, '//*[@id="bd_5665468_0"]/div/table/tbody/tr['+i+']/td[2]/a[1]').click()
        thisid = driver.current_url
        y = thisid.split("=")
        finalid = y[-1]
        driver.find_element(By.ID , "editor_"+finalid).send_keys("ㅌㅅ")
        sleep(slep)
        driver.find_element(By.XPATH, '//*[@id="'+finalid+'_comment"]/div[2]/form/div/input').click()
        print("comment posted")
        notify(Discordlink, "comment posted")
        sleep(slep)
        driver.find_element(By.CLASS_NAME, 'vote_label').click()
        print("upvoted")
        notify(Discordlink, "upvoted")
        return False

txtread = send(link_to_message)


driver.get('https://www.fmkorea.com/index.php?mid=fifa_online&category=5665557')
sleep(slep)
while(torf == True):
    try:
        driver.refresh()
    except:
        sleep(slep)
        continue
    else:
        sleep(slep)
    
        try:
            
            driver.find_element(By.XPATH, '//*[@id="bd_5665468_0"]/div/table/tbody/tr[5]/td[2]/a[1]').is_displayed()
            
        except:
            try:
                driver.find_element(By.XPATH, '//*[@id="bd_5665468_0"]/div/table/tbody/tr[6]/td[2]/a[1]').is_displayed()
            except:
                try:
                    driver.find_element(By.XPATH, '//*[@id="bd_5665468_0"]/div/table/tbody/tr[7]/td[2]/a[1]').is_displayed()
  
                except:
                    
                    continue
                    
                else:
                    torf = main('7', Discordlink, slep)
              
            else:
                torf = main('6', Discordlink, slep)
        else:
            
            torf = main('5', Discordlink, slep)
         
      

    

torf = True
while(torf == True):
    driver.refresh()
    sleep(5)
    isnotice = False
    try :
        driver.find_element(By.XPATH, '//*[@id="FM_NOTICE"]/a/span[1]').is_displayed()
    except :
        print("can't find")
    else:
        isnotice = True
    while(isnotice):
        try:
            
            driver.find_element(By.XPATH, '//*[@id="bd_capture"]/div[1]/div[1]/div[2]/div[1]/a').click()
            sleep(slep)
            driver.find_element(By.XPATH, '//*[@id="popup_menu_area"]/ul/li[1]/a').click()
            sleep(slep)

        except:
            sleep(20)
            continue
        else:
            sleep(slep)
            window_after = driver.window_handles[1]
            sleep(5)
            driver.switch_to.window(window_after)
            sleep(slep)
            driver.find_element(By.ID, 'message_title').send_keys("대낙")
            sleep(slep)
            driver.find_element(By.CLASS_NAME, 'inputTextarea').send_keys(txtread)
            sleep(slep)
            driver.find_element(By.CLASS_NAME, "editor_button").click()
            print("message sent")
            notify(Discordlink, "message sent")
            sleep(slep)
            Alert(driver).accept()
            sleep(10)
            Alert(driver).accpet()
            torf = False
    sleep(20)


