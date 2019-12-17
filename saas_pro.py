from api.staff.staff import Staff
from public.get_token import get_token


class SaasPro:

    def __init__(self, is_store=True, **kawrgs):
        token = get_token("st30273013056","bnKD9667",is_store=True, **kawrgs)
        self.staff = Staff(token)
