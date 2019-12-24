from api.course.personal_course import PersonalCourse

class Course:
    def __init__(self,token):
        self.personal_course = PersonalCourse(token)
        