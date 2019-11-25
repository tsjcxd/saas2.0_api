import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from unittest import TestCase
from api.staff.coach_list import Coach_list
from public.get_token import get_token

coach_list = Coach_list(get_token("st30273013056", "bnKD9667"))


class TestCoachList(TestCase):
    def test01_coach_list(self):
        resp = coach_list.coach_list()
        print(resp.text)
        self.assertEquals(resp.json()["code"],40507)