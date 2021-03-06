import requests
from conf import BASE_URL,APP_VERSION,APP_ID
from public.get_token import get_token


class RestClient:
    """HTTP方法封装"""
    def __init__(self, token):
        header = {
            "app-id": APP_ID,
            "app-version" : APP_VERSION,
            "token" : token
        }
        self.session= requests.session()
        self.session.headers.update(header)
        
    
    # def get(self,api,**kwargs):
    #     resp = self.tangtang("get",api,**kwargs)
    #     return resp

    # def tangtang(self,method,api,**kwargs):
    #     url = BASE_URL+api
    #     if method == "get":
    #         resp = self.session.get(url,**kwargs)
    #         return resp



    def get(self,api,params=None,**kwargs):
        resp = self.request("get",api,params=params,**kwargs)
        return resp

    def post(self,api,data=None,json=None,**kwargs):
        resp = self.request("post",api,data=data,json=json,**kwargs)
        return resp

    def delete(self,api,**kwargs):
        resp = self.request("delete",api)
        return resp

    def put(self,api,data=None,**kwargs):
        resp = self.request("put",api, data=data, **kwargs)
        return resp

    def request(self,method,api,params=None,data=None,json=None,**kwargs):
        url = BASE_URL+api
        if method=="get":
            resp = self.session.get(url,params=params)
        if method=="post":
            resp = self.session.post(url,data=data,json=json,**kwargs)
        if method=="delete":
            resp = self.session.delete(url,**kwargs)
        if method =="put":
            resp = self.session.put(url,data=data, **kwargs)
        return resp




    
    