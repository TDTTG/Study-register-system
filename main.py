print('You may select one of the following:\n\t\t\t\t1) Add student\n\t\t\t\t2) Search student\n\t\t\t\t3) Search course\n\t\t\t\t4) Add course completion\n\t\t\t\t5) Show student record\n\t\t\t\t0) Exit')
a = input('What is your selection?\n')
def add_student():
    print('Names should contain only letters and start with capital letters.')
    first = input('Enter the first name of the student:\n')
    last = input('Enter the last name of the student:\n')
    warn = 'Names should contain only letters and start with capital letters.'
    while first[0].islower() or last[0].islower() or not first.isalpha() or not last.isalpha():
        print(warn)
        first = input('Enter the first name of the student\n')
        last = input('Enter the last name of the student\n')
    def add_major():
        student_info = open('students.txt', mode='a')
        print('Select student\'s major:\n\tCE: Computational Engineering\n\tEE: Electrical Engineering\n\tET: Energy Technology\n\tME: Mechanical Engineering\n\tSE: Software Engineering')
        major = input('What is your selection?\n')
        existing_student_codes = set()
        with open('students.txt', mode='r') as student_file:
            for line in student_file:
                parts = line.strip().split(',')
                if len(parts) >= 1:
                    existing_student_codes.add(parts[0])
        import random
        while True:
            student_code = random.randint(10000, 99999)
            student_code_str = str(student_code)

            if student_code_str not in existing_student_codes:
                break
        email = f"{first.lower()}.{last.lower()}@lut.fi"
        import datetime
        year = datetime.datetime.now().year
        student_info.write(f'{student_code},{first},{last},{year},{major},{email}\n')
    add_major()
def find_student():
    name = input('Give at least 3 characters of students first or last name:\n')
    while len(name) < 3:
        name = input('Give at least 3 characters of students first or last name:\n')
    student = open('students.txt', mode= 'r')
    while True:
        line = student.readline()
        if name in line:
            list_info = line.strip().split(',')
            print(f'Matching students:\nID: {list_info[0]}, First name: {list_info[1]}, Last name: {list_info[2]}')
        elif line == '': break
def search_course():
    search = input('Give at least 3 characters of the name of the course or the teacher:\n')
    while len(search) < 3:
        search = input('Give at least 3 characters of the name of the course or the teacher:\n')
    edu = open('courses.txt', mode = 'r')
    while True:
        line = edu.readline()
        if search in line:
            list_info = line.strip().split(',')
            print(f'ID: {list_info[0]}, Name: {list_info[1]},', end=' ')
            if len(list_info) == 4:
                print(f'{list_info[3]}')
            elif len(list_info) == 5:
                print(f'{list_info[3]},{list_info[4]}')
            elif len(list_info) == 6:
                print(f'{list_info[3]},{list_info[4]},{list_info[5]}')
            elif len(list_info) == 7:
                print(f'{list_info[3]},{list_info[4]},{list_info[5]},{list_info[6]}')
            elif len(list_info) == 8:
                print(f'{list_info[3]},{list_info[4]},{list_info[5]},{list_info[6]},{list_info[7]}')
        elif line == '': break
def add_course_completetion():
    import datetime
    while True:
        course_id = input('Give the course ID:\n')
        if len(course_id) == 5: break
    while True:
        student_id = input('Give the student ID:\n')
        if len(student_id) == 5: break
    grade = int(input('Give the grade:\n'))
    if grade > 5: print('Grade is not a correct grade')
    else:
        x = 0
        file = open('passed.txt', mode='r')
        while True:
            course = file.readline()
            x += 1
            if course_id in course and student_id in course:
                break
            elif course == '':
                break
        list = course.strip().split(',')
        if int(list[3]) >= grade:
            print(f'Student has passed this course earlier with grade {list[3]}')
        else:
            date = input('Enter a date (DD/MM/YYYY):\n')
            try:
                a = datetime.datetime.strptime(date, '%d/%m/%Y')
            except ValueError:
                print('Invalid date format. Use DD/MM/YYYY. Try again!')
            else:
                now = datetime.datetime.now()
                old_date = datetime.datetime.strptime(list[2], '%d/%m/%Y')
                delta = now - a
                if a > now:
                    print('Input date is later than today. Try again!')
                elif delta.days > 30:
                    print('Input date is older than 30 days. Contact "opinto".')
                else:
                    print('Input date is valid.\nRecord added!')
                    with open('passed.txt', mode='r') as update:
                        new_course = f'{list[0]},{list[1]},{date},{grade}\n'
                        create_file = update.readlines()
                        with open('passed.txt', mode= 'w') as update:
                            for i, line in enumerate(create_file, start= 1):
                                if i == x: continue
                                update.write(line)
                    with open('passed.txt', mode= 'a') as update:
                        update.write(new_course)

def show_student_reocrd():
    student_id = input('Give student ID:\n')
    with open('students.txt', mode = 'r') as file1:
        while True:
            line = file1.readline()
            if student_id in line:
                list = line.strip().split(',')
                print(f'Student ID: {list[0]}\nName: {list[2]}, {list[1]}\nStarting year: {list[3]}')
                if list[4] == 'CE': print('Major: Computational Engineering')
                elif list[4] == 'EE': print('Major: Electrical Engineering')
                elif list[4] == 'ET': print('Major: Energy Technology')
                elif list[4] == 'ME': print('Major: Mechanical Engineering')
                elif list[4] == 'SE': print('Major: Software Engineering')
                print(f'Email: {list[5]}\n')
                break
            elif line == '':
                print('Student ID do not exist. Please try again.')
                file1.seek(0)
                student_id = input('Give student ID:\n')
    credit = 0
    ave_grade = 0
    divide_by = 0
    with open('passed.txt', mode= 'r') as file2, open('courses.txt', mode = 'r') as file3:
        print('Passed courses:\n')
        for student_info in file2:
            if student_id in student_info:
                student_data = student_info.strip().split(',')
                file3.seek(0)
                for course_info in file3:
                    if student_data[0] in course_info:
                        course_data = course_info.strip().split(',')
                        print(f'Course ID: {student_data[0]}, Name: {course_data[1]}, Credits: {course_data[2]}\nDate: {student_data[2]}, Teacher(s): {course_data[3]}, Grade: {student_data[3]}\n')
                        credit += int(course_data[2])
                        ave_grade = ((int(student_data[3])) + ave_grade)
                        divide_by += 1
        if ave_grade == 0: print('This student have no passed courses.')
        else: print(f'Total credits: {credit}, average grade: {round(ave_grade/divide_by,1)}')

while a != 0:
    if a == '1':
        add_student()
        print('Student added successfully!')
    elif a == '2':
        find_student()
    elif a == '3':
        search_course()
    elif a == '4':
        add_course_completetion()
    elif a == '5':
        show_student_reocrd()
    elif a == '0':
        print('Program finished. Good bye!')
        break
    else:
        print('Wrong selection. Please try again!')
    a = input('\n\nWhat is your next selection?\n')