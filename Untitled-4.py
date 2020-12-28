student1 = {'name': 'Иван', 'cities':['Москва', 'Лондон']}
student2 = {'name': 'Мария', 'cities':['Париж', 'Нью-Йорк']}
student3 = {'name': 'Петр', 'cities':['Пекин', 'Токио']}

students = [student1, student2, student3]

for s in students:
    print(s['name'])
    print(s['cities'])