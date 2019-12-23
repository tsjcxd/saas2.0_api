from base.rest_client import RestClient

class StorePersonalCourse(RestClient):
    # def __init__(self, token):
    #     super().__init__(token)

    def store_personal_course_list(self,params=None,**kwargs):
        resp = self.get("/v1/course/personal/shop",params=None,**kwargs)
        return resp
