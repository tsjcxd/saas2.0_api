from api.staff.staff import Staff
from public.get_token import get_token
from api.course.course import Course


class SaasPro:


    def __init__(self, is_store=True, **kawrgs):
        self.token = get_token("st30273013056","bnKD9667",is_store, **kawrgs)
        self.staff = Staff(self.token)
        self.course = Course(self.token)

    # def staff(self):
    #     staff = Staff(self.token)
    #     return staff