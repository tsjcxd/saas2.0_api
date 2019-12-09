from base.rest_client import RestClient

class ChangeStore:
    def __init__(self,token):
        self.rest_client = RestClient(token)
        
    def change_store(self,data=None):
        resp = self.rest_client.put("/v1/account/switch/shop",data=data)
        return resp