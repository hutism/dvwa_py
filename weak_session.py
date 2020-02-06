from seleniumwire import webdriver

LOGIN = "http://10.0.2.13:8080/login.php"
URL = "http://10.0.2.13:8080/vulnerabilities/weak_id/"
browser = webdriver.Firefox()
browser.get(LOGIN)
browser.find_element_by_name('username').send_keys('admin')
browser.find_element_by_name('password').send_keys('password')
browser.find_element_by_name('Login').click()
browser.get(URL)
browser.find_element_by_tag_name('input').click()
for request in browser.requests:
    if(str(request)==URL):
        try:
            print(request.response.headers['Set-Cookie'])
            id = request.response.headers['Set-Cookie']
        except KeyError:
            print('skip')
        except AttributeError:
            print('skip')

browser.close()
