import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from unittest import TestCase
from saas_pro import SaasPro

saas_pro = SaasPro(is_store=True)


class TestCoachList(TestCase):
    def test01_coach_list(self):
        resp = saas_pro.staff.coach_list.coach_list()
        print(resp.text)
        self.assertEqual(resp.json()["code"],0)