# 查看教练等级列表
# 新增教练等级
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from saas_pro import SaasPro
from operation.get_coach_id import get_coach_name_id
import jsonpath
from public.mysql.mysql_connect import ExecuteSQL


saas_pro = SaasPro(is_store=False)
connect = ExecuteSQL('saas_test')

class TestCoachLevelCreate(TestCase):
    """教练等级新增接口"""


    def test01_coachlevel_create_success(self):
        """case01: """
        payload={
             "setting_name": "自动化0109"
        }
        resp = saas_pro.staff.coach_level.coach_level_create(data=payload)
        sql_data = connect.get_singledata('''SELECT * FROM `app_setting` where setting_name="{}";'''.format(payload["setting_name"]))
        self.assertIsNotNone(sql_data,"新增数据失败")
        self.assertEquals(sql_data["result"], 1)
        self.assertEquals(sql_data["status"], 2)

        # connect.close_conn()
        



# class TestCoachLevelList(TestCase):
#     """查看教练等级列表接口"""
#     def test01_coachlevel_list(self):
#         resp = saas_pro.staff.coach_level.coach_level_list()
#         self.assertEquals()


# class TestCoachLevelEdit(TestCase):
#     '''编辑教练等级（教练等级的ID从教练列表中获取）'''
#     def test01_coachlevel_edit_success(self):
#         payload={
#              "setting_name": "金牌教练编辑后"
#         }
#         resp = saas_pro.staff.coach_level.coach_level_edit(get_coach_name_id(saas_pro,"金牌教练"),data=payload)
#         print(resp.text)
#         self.assertEquals(resp.json()["code"],0)


# class TestCoachLevelDelete(TestCase):
#     '''删除教练等级（教练等级的ID从教练列表中获取）'''
#     def test01_coachlevel_delete_success(self):
#         resp = saas_pro.staff.coach_level.coach_level_delete(get_coach_name_id(saas_pro, "金牌教练编辑后"))
#         print(resp.text)
#         self.assertEquals(resp.json()["code"],0)






if __name__ == "__main__":
    import unittest


    