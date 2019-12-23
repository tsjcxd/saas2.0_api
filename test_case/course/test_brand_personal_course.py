import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from saas_pro import SaasPro

saas_pro = SaasPro(is_store = False)

class TestBrandPersonalCourse(TestCase):

    def test01_brand_personal_course_list(self):
        payload = {
            "page":1,
            "size":3
        }
        resp = saas_pro.course.brand_personal_course.brand_personal_course_list(payload)
        self.assertEqual(len(resp.json()["data"]["list"]),3)
        # print(resp.json())

        