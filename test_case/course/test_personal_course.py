import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from saas_pro import SaasPro

store_course = SaasPro(is_store=True)
brand_course = SaasPro(is_store=False)

class TestBrandPersonalCourse(TestCase):

    def test01_brand_personal_course_list(self):
        payload = {
            "page":1,
            "size":3
        }
        resp = brand_course.course.personal_course.brand_personal_course_list(payload)
        self.assertEqual(len(resp.json()["data"]["list"]),3)
        # print(resp.json())

class TestStorePersonalCourse(TestCase):

    def test02_store_personal_course_list(self):
        payload={
            "page":1,
            "size":20
        }
        resp = store_course.course.personal_course.store_personal_course_list(payload
        )
        print(resp.json())

class TestBrandStorePersonalCourse(TestCase):

    def test03_brand_store_personal_course_list(self):
        payload={
            "page":1,
            "size":20,
            "shop_id":352231090618557
        }
        resp = brand_course.course.personal_course.brand_store_personal_course_lise(payload)


        