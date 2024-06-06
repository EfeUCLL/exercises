class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return 'A'
        elif 80 <= score <= 89:
            return 'B'
        elif 70 <= score <= 79:
            return 'C'
        elif 60 <= score <= 69:
            return 'D'
        return 'F'

    def add_course(self, course_name, score):
        letterGrade = self.calculate_letter_grade(score)
        key = course_name
        self.__courses[key] = letterGrade

    def get_courses(self):
        return self.__courses
