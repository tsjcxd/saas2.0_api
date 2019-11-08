# 查看教练等级列表
# 新增教练等级
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from base.rest_client import Rest_Client
from public.get_token import get_token
from api.staff.coach_level import CoachLevel
import jsonpath

coach_level = CoachLevel(get_token("st65271088319", "m562e7Qh"))


class TestCoachLevelCreate(TestCase):
    """教练等级新增接口"""

    # def test01_coachlevel_create_success(self):
    #     """case01: """
    #     payload={
    #          "setting_name": "金牌教练"
    #     }
    #     resp = coach_level.coach_level_create(payload)
    #     print(resp.json())
    #     self.assertEquals(resp.json()["code"],0)
        



class TestCoachLevelList(TestCase):
    """查看教练等级列表接口"""
    def test01_coachlevel_list(self):
        resp = coach_level.coach_level_list()
        # print(resp.json())
        # ret=jsonpath.jsonpath(resp.json(),'$..id')
        coach_id = [i["id"] for i in resp.json()["data"]["list"]][-1]

        print(coach_id)



# class TestCoachLevelDelete(TestCase):
#     '''删除教练等级（教练等级的ID数据库中获取）'''
#     def test01_coachlevel_delete_success(self):
#         resp = coach_level.coach_level_delete()
#         print(resp)






if __name__ == "__main__":
    import unittest


    