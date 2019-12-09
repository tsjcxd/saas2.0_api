from base.rest_client import RestClient


class CoachList(RestClient):

    def coach_list(self,params=None,**kwargs):
        resp = self.get("/v1/staff/coach",params=params,**kwargs)
        return resp
 