from base.rest_client import Rest_Client

class Change_Store:
    def __init__(self,token):
        rest_client = Rest_Client(token)
        
    def change_store(self,data=None):
        resp = Rest_Client.put(self,"/v1/account/switch/shop",data=data)
        return resp