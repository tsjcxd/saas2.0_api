
from unittest import TestCase
from base.rest_client import Rest_Client
from public.get_token import get_token
from api.account.chang_store import Change_Store

change_store = Change_Store(get_token("",""))

class TestGetStoreToken(TestCase):
    def test01_get_store_token(self):
        palyload={
            "shop_id":123456
        }
        resp = change_store.change_store(palyload)
        print(resp.text)

