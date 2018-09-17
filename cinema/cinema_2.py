from cinema import Hall, Human, Cashbox, Pub

# students = Student.import_from_file('students.txt')
# [print(el) for el in students]

watcher = Human.import_from_file('human.txt')
cashbox = Cashbox.import_from_file('film.txt')
hall = Hall.import_from_file('hall.txt')
pub = Pub.import_from_file('pub.txt')


[print(el) for el in watcher]
[print(el) for el in cashbox]
[print(el) for el in hall]
[print(el) for el in pub]


# group_23.add_students(students_23)
# [print(el, el.group) for el in students_23]

# print('*' *25)
# students_33 = Student.import_from_file('33_group.txt')
# group_33 = Group('33', 'Прикладная информатика 09.02.05')
# group_33.add_students(students_33)
# [print(el, el.group) for el in students_33]