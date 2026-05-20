class Student:
    def __init__(self, name, student_id):
        self.info = {
            "name" : name,
            "id" : student_id,
            "grades" : [],
            "attendance" : 0
        }
    def add_grade(self,score):
        self.info['grades'].append(score)
        print(f'added score')
    def calculate_average(self):
        grades = self.info['grades']
        if not grades:
            return 0
        return sum(grades) / len(grades)
    def display(self):
        print(f"Name: {self.info['name']}")
        print(f"ID: {self.info['id']}")
        print(f"Grades: {self.info['grades']}")
        print(f"Average: {self.calculate_average()}")
        


s1 = Student("Vincent", 1)
s1.add_grade(90)
s1.add_grade(85)
s1.display()