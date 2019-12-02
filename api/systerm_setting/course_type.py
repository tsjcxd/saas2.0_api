from base.rest_client import Rest_Client


class CourseType:
    def __init__(self,token):
        self.rest_client = Rest_Client(token)
    
    def course_type(self,data=None,**kwarg):
        resp = self.rest_client.post("/v1/setting/course",data=data)
        return resp