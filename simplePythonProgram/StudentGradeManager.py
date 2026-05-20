class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_score(self,score):
        self.grades.append(score)
        print('Added scored')
    def calculate_average(self):
        total = 0
        for grade in self.grades:
            total+=grade
        average = total / len(self.grades)
        return average
    def get_letter_grade(self):
        if self.calculate_average() >= 90:
           return 'A'
        elif self.calculate_average() >=80:
            return 'B'
        elif self.calculate_average() >=75:
            return 'C'
        else:
            return "Failed"

    def display(self):
        count = len(self.grades)
        print('Data of this student::')
        print(f'Student name: {self.name}')
        print(f'Student Id: {self.student_id}')
        print(f'Student total grades: {count}')
        if count > 0:
            for grade in self.grades:
                print(f'{grade}')
        else:
            print('No score or grade added')
        print(f'Total average: {self.calculate_average()}')
        print(f'Grade Letter: {self.get_letter_grade()}')

class GradeBook:
    def __init__(self):
        self.students = []
        self.nextId = 1

    def add_students(self,name):
        new_student = Student(name,self.nextId)
        self.students.append(new_student)
        print(f'Added new student data')
        self.nextId += 1

    def find_student(self,student_id):
        for student in self.students:
            if student_id == student.student_id:
                print(f'Student found {student.name}')
                return student
        print("Not Found")
        return None

    def remove_student(self,student_id):
          for i in range(len(self.students)):
            if student_id == self.students[i].student_id:
                removed = self.students.pop(i)
                print(f"{removed.name} is deleted")
                return True
            
          print('Not Found')
          return False



gb = GradeBook()

while True:
      print(f'1.add student')
      print(f'2.find student')
      print(f'3.removed student')

      choice = input('Enter choice: ')

      if choice == '1':
         add = input('Enter student name to add: ')
         gb.add_students(add)
      elif choice == '2':
         find = int(input('Enter student id: '))
         found = gb.find_student(find)
       
         select = input('Enter what to do? ')
         if found:
            print(f'What to do? ')
            print(f'1. add score')
            print(f'2. display student data')
            if select == '1':
               score = int(input('Enter score:'))
               found.add_score(score)
            elif select == '2':
                 found.display()
            else:
                print('invalid option')
         else:
            print('Student not found, returning to main menu')
      elif choice == '3':
           student_id = int(input('Enter student id to remove: '))
           gb.remove_student(student_id)

      elif choice == '4':
           print('Bye')
           break
      else:
        print('Invalid choice')