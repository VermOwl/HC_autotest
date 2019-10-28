import requests
import configparser

class request_hc():


    def login(self, site, email, password):
        
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

        response = requests.request("POST", url, data=payload, headers=headers)
        wef = requests.request("POST", url, data=payload, headers=headers).json()
        print(wef)
        print(response.text)
        

    def get_back_passwrod(self, site, email, password):
        
        self.login(email, "23072307qS")

        url = "" + site + "/api/v1/auth/account-password"

        payload = "{\n    \"password\": \"23072307\",\n    \"password_confirmation\": \"23072307\",\n    \"current_password\": \"23072307qS\"\n}"
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjVjYzEwZGE4NmJlZGZhOTY0ODRkYzllN2E5NDRiODE4ZGM4MzJmZWE0N2U5OTkxMTFjMDRiZTYxYzQ3NWEwMzk4MzNiOGQzMjdjNmIyNTNkIn0.eyJhdWQiOiIxIiwianRpIjoiNWNjMTBkYTg2YmVkZmE5NjQ4NGRjOWU3YTk0NGI4MThkYzgzMmZlYTQ3ZTk5OTExMWMwNGJlNjFjNDc1YTAzOTgzM2I4ZDMyN2M2YjI1M2QiLCJpYXQiOjE1NzIyNzMzNjgsIm5iZiI6MTU3MjI3MzM2OCwiZXhwIjoxNjAzODk1NzY4LCJzdWIiOiI0MDAiLCJzY29wZXMiOltdfQ.MVg73DbHxzMCT4VKDoiGZWACCtyAkUgkOMGrsqtDBgHOVnS5KKGCScvw_m66eT0gOuTnu-dDIt-DddjiW3u57BtC5C2rHs5d_SWSbHnO9LK3WvE24sveqlcHfEUske-WdxAvGep28r58dLQ0EmbHgsfyD5WirK1vSdZeT45kXcm4Za25WRq8UYqMF996qoEJxHxRSbDQjWxkWY6oPGA_a_QF4pRjLJYMao_fEtbV_Kc1-DunCem9oWO4zVS6OJtgN-73ibx5q98GAcmfODp4L-AAFLNenXnnMEFhcJQg5gOUSPeb445n-Oc901oeGI72exQ_roHMiH9mKDLVRD63SLNd2qTYtmdFuPKQO9qHhGXSaDYP6Ndyk6isehgmlz17ZJwUkHgfJwKfAzwYDPnvHHZ-gZRZ8r7AGxhduR9we9c3ZQPVBWLn9rz86d_EOHrhJ7IwmKpZGgDutDM-yKUxmlirCWDCMWqhm8DdWuwy8wdHk9MWFYEIRTgXTEVpTWyaS_6qPOj1fSfaDnHfw6wamZDGwp5lDDkd-WQ5-Q-nVtZIxIcgEtjAWw9Mz2Pd5s0oSWHbyRAfzILUL661uAoK2e7zESKS2szOj-TLtiS8KofuHKfeQRo4NKoTJ7SvPb5PthLzAWls1Y2qyb7VzKwI1lZ7V3AN9BoFulUx0wQPoWE",
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