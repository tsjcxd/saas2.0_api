import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from unittest import TestCase
from base.rest_client import Rest_Client
from public.get_token import get_token
from api.account.chang_store import ChangeStore

change_store = ChangeStore(get_token("st30273013056", "bnKD9667"))

class TestGetStoreToken(TestCase):
    def test01_get_store_token(self):
        payload={
            "shop_id":179734466593137
        }
        resp = change_store.change_store(payload)
        return(resp.json()["data"]["token"])
        print(resp.json()["data"]["token"])

