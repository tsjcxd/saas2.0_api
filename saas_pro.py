from api.staff.staff import Staff


class SaasPro:

    def __init__(self,token):
        self.staff = Staff(token)
