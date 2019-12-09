from base.rest_client import RestClient


class CourseType:
    def __init__(self,token):
        self.rest_client = RestClient(token)
    
    def course_type(self,data=None,**kwarg):
        resp = self.rest_client.post("/v1/setting/course",data=data)
        return resp