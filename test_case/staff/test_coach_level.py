# 查看教练等级列表
# 新增教练等级
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from base.rest_client import Rest_Client
from public.get_token import get_token
from api.staff.coach_level import CoachLevel
from operation.get_coach_id import get_coach_name_id
import jsonpath

coach_level = CoachLevel(get_token("st30273013056", "bnKD9667"))


# class TestCoachLevelCreate(TestCase):
#     """教练等级新增接口"""

#     def test01_coachlevel_create_success(self):
#         """case01: """
#         payload={
#              "setting_name": "金牌教练"
#         }
#         resp = coach_level.coach_level_create(payload)
#         print(resp.json())
#         self.assertEquals(resp.json()["code"],0)
        



# class TestCoachLevelList(TestCase):
#     """查看教练等级列表接口"""
#     def test01_coachlevel_list(self):
#         resp = coach_level.coach_level_list()
#         self.assertEquals()


class TestCoachLevelEdit(TestCase):
    '''编辑教练等级（教练等级的ID从教练列表中获取）'''
    def test01_coachlevel_edit_success(self):
        payload={
            "id": 292729603555381,
             "setting_name": "金牌教练编辑3"
        }
        resp = coach_level.coach_level_edit(get_coach_name_id(coach_level,"金牌教练编辑2"),data=payload)
        print(resp.text)
        self.assertEquals(resp.json()["code"],0)


# class TestCoachLevelDelete(TestCase):
#     '''删除教练等级（教练等级的ID从教练列表中获取）'''
#     def test01_coachlevel_delete_success(self):
#         resp = coach_level.coach_level_delete(get_coach_name_id(coach_level, "金牌教练"))
#         print(resp.text)
#         self.assertEquals(resp.json()["code"],0)






if __name__ == "__main__":
    import unittest


    