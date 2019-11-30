from base.rest_client import Rest_Client

class Change_Store:
    def __init__(self,token):
        self.rest_client = Rest_Client(token)
        
    def change_store(self,data=None):
        resp = self.rest_client.put("/v1/account/switch/shop",data=data)
        return resp