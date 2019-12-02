import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from unittest import TestCase
from api.systerm_setting.course_type import CourseType
from public.get_token import get_token

course_type = CourseType(get_token("st30273013056", "bnKD9667"))

class Test_Course_Type(TestCase):
    def test01_create_course_type(self):
        payload={
            "setting_name":"自动化类型"
        }
        resp = course_type.course_type(data=payload)
        return resp.json()

        

