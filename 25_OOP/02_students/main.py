import random


class Student:

    def __init__(self, student_index, surname_name='Иванов Иван', group_number='5A', grades=None):
        self.index = student_index
        self.surname_name = surname_name
        self.group_number = group_number
        self.grades = grades

    def print_info(self):
        print('ФИ студента: {}\nНомер группы: {}\nОценки: {}\nСредний балл: {}\n'.format(
            self.surname_name, self.group_number, self.grades, sum(self.grades) // len(self.grades)
        ))


class Faculty:

    def __init__(self, number):
        self.students = [Student(index) for index in range(1, number + 1)]

    def fill_data(self):
        for index, student in enumerate(self.students):
            surname_and_name = random.choice(surname_list) + ' ' + random.choice(name_list)
            group_number = random.randint(1, 3)
            student_grades = [random.randint(1, 5) for _ in range(5)]

            student.surname_name = surname_and_name
            student.group_number = group_number
            student.grades = student_grades

    def sort_by_average(self):
        students_range = len(self.students)
        for number in range(students_range - 1):
            for index in range(students_range - number - 1):
                curr_average_grade = sum(self.students[index].grades) / len(self.students[index].grades)
                next_average_grade = sum(self.students[index + 1].grades) / len(self.students[index + 1].grades)
                if curr_average_grade > next_average_grade:
                    self.students[index], self.students[index + 1] = self.students[index + 1], self.students[index]

    def print_info(self):
        for student in self.students:
            student.print_info()


name_list = ['Bob', 'Sergey', 'Sam', 'Elena', 'Olga', 'Jogh', 'Kostya',
             'Svetlana', 'Ivan', 'Stepan']
surname_list = ['Ivanov', 'Stepanov', 'Jonson', 'Kuplinov', 'Cox', 'Vinny',
                'Keyisy', 'Kappa', 'Bench', 'Anabel']

print('Список студентов:\n')
add_students = Faculty(10)
add_students.fill_data()
add_students.sort_by_average()
add_students.print_info()
