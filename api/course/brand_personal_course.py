
from base.rest_client import RestClient

class BrandPersonalCourse(RestClient):

    # def __init__(self, token):
    #     super().__init__(token)

    def brand_personal_course_list(self,params=None,**kwargs):
        resp = self.get("/v1/course/personal/brand",params=params,**kwargs)
        return resp

