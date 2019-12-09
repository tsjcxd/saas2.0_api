from api.staff.coach_level import CoachLevel
from api.staff.coach_list import CoachList


class Staff:

    def __init__(self,token):
        self.coach_level = CoachLevel(token)
        self.coach_list = CoachList(token)

