
from base.rest_client import RestClient

class PersonalCourse(RestClient):

    # def __init__(self, token):
    #     super().__init__(token)

    def brand_personal_course_list(self,params=None,**kwargs):
        resp = self.get("/v1/course/personal/brand",params=params,**kwargs)
        return resp
    
    def store_personal_course_list(self,params=None,**kwargs):
        resp = self.get("/v1/course/personal/shop",params=None,**kwargs)
        return resp

    def brand_store_personal_course_lise(self,params=None,**kwargs):
        resp = self.get("/v1/course/personal/brand/shop",params=None,**kwargs)
        return resp
    

