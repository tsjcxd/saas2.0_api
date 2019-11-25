from base.rest_client import Rest_Client

class Coach_list:
    def __init__(self, token):
        self.rest_client = Rest_Client(token)



    def coach_list(self,params=None,**kwargs):
        resp = self.rest_client.get("/v1/staff/coach",params=params,**kwargs)
        return resp
