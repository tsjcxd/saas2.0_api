from api.course.brand_personal_course import BrandPersonalCourse
from api.course.store_personal_course import StorePersonalCourse

class Course:
    def __init__(self,token):
        self.brand_personal_course = BrandPersonalCourse(token)
        self.store_personal_course = StorePersonalCourse(token)