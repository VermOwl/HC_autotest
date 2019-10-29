import requests
import configparser

class request_hc():


    def login(self, site, email, password): # логинимся для получения и возврата токена
        
        url = "" + site + "/api/v1/auth/login"

        payload = "{\n    \"email\": \"" + email + "\",\n    \"password\": \"" + password + "\"\n}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.16.3",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "827c578b-a061-477f-98de-399a333c2d68,b4527ec9-6dba-403c-ab44-8abc2292b25f",
            'Host': "front.stage.helpcubes.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "68",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        #response = requests.request("POST", url, data=payload, headers=headers)
        wef = requests.request("POST", url, data=payload, headers=headers).json()
        print(wef)

        return wef['access_token']
        

    def get_back_passwrod(self, site, email, password): # этот модуль будет возвращать пароль в исходное сотосяние необходимо для теста change_password.py
                
        token = self.login(site, email, password)

        url = "" + site + "/api/v1/auth/account-password"

        payload = "{\n    \"password\": \"23072307\",\n    \"password_confirmation\": \"23072307\",\n    \"current_password\": \"23072307qS\"\n}"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token + "",
            'User-Agent': "PostmanRuntime/7.16.3",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "18d85cfb-3034-461a-b4ff-ae63e4f7a714,4bffba72-7555-44b3-a06b-21628669400e",
            'Host': "front.stage.helpcubes.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "109",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)


#requesthc = request_hc()
#requesthc.get_back_passwrod()