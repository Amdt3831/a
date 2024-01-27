import re
current_menu = 'log in/sign up menu'


class Student:
    def __init__(self, id, name, password, courses=None):
        self.id = id
        self.name = name
        self.password = password
        self.courses = courses if courses is not None else []


class Professor:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password


courses = []


class Course:
    def __init__(self, name, id, capacity, course_students=0):
        self.name = name
        self.id = id
        self.capacity = capacity
        self.course_students = course_students


students = []
professors = []
ids = [s.id for s in students]
passs = [s.password for s in students]
idp = [p.id for p in professors]
passp = [p.password for p in professors]
idc = [c.id for c in courses]


def redescribe(students, professors):
    global ids
    global passs
    global idp
    global passp
    ids = [s.id for s in students]
    passs = [s.password for s in students]
    idp = [p.id for p in professors]
    passp = [p.password for p in professors]

def redescribec(courses):
    global idc
    idc = [c.id for c in courses]

lastlog = []

class Logsign:
    def signup(self, type, id, name, password):
        if type == 'S':
            students.append(Student(id, name, password))
            print('signed up successfully!')
        else:
            professors.append(Professor(id, name, password))
            print('signed up successfully!')
        redescribe(students, professors)


    def login(self, id, password):
        i = 0
        j = 0
        b = 0
        if id in ids and password in passs:
            global current_menu
            current_menu = 'student menu'
            print(f'logged in successfully!\nentered {current_menu}')
            for s in students:
                if s.id == id and s.password == password:
                    lastlog.append(s)
        elif id in idp and password in passp:
            current_menu = 'professor menu'
            print(f'logged in successfully!\nentered {current_menu}')
            for p in professors:
                if p.id==id and p.password==password:
                    lastlog.append(p)
        elif id not in ids:
            i += 1
        elif password not in passs:
            j += 1
        elif password not in passp:
            b += 1
        if i == 1 and id not in idp:
            return print('incorrect id')
        elif j == 1 and id in ids:
            return print('incorrect password')
        elif b == 1 and id in idp:
            return print('incorrect password')


w = 0
while w == 0:
    a = input()
    a = re.sub(r'^ +| +$', '', a)
    if a == 'edu log out edu':
        if current_menu != 'log in/sign up menu':
            current_menu = 'log in/sign up menu'
            print(f'logged out successfully!\nentered {current_menu}')
        else:
            print('invalid command')
    elif a == 'edu current menu edu':
        print(current_menu)
    elif re.search('^edu sign up .+ edu$', a):
        u = a.split(' ')
        if re.search(r'edu sign up -[SP] -i [0-9]+ -n \S+ -p ([\S*.!@$%^&()]){4,} edu', a) and\
                re.search('-p .*[*.!@$%^&()].* edu', a):
            if u[5] in ids or u[5] in idp:
                print('id already exists')
                continue
            if u[3] == '-S':
                a = Logsign()
                a.signup('S', u[5], u[7], u[9])
            elif u[3] == '-P':
                a = Logsign()
                a.signup('P', u[5], u[7], u[9])
        elif not re.search('-P|-S', u[3]):
            print('invalid type')
        elif not re.search('-i \d+ -n', a):
            print('invalid id')
        elif not re.search('-n \S+ -p', a):
            print('invalid name')
        elif not re.search('-p ([\S*.!@$%^&()]){4,} edu', a) or not re.search('-p .*[*.!@$%^&()].* edu', a):
            print('invalid password')

    elif re.search('^edu log in -i .+ -p .+ edu$', a):
        u = a.split(' ')
        a = Logsign()
        a.login(u[4], u[6])
    elif a == 'edu show course list edu':
        if current_menu != 'log in/sign up menu':
            print('course list:')
            for c in courses:
                print(f'{c.id} {c.name} {c.course_students}/{c.capacity}')
        else:
            print('invalid command')
    elif re.search('edu add course -c .* -i .* -n .* edu', a) and current_menu=='professor menu':
        u = a.split(' ')
        if u[6] in idc:
            print('course id already exists')
            continue
        elif not re.search('-c \S+ -i', a):
            print('invalid course name')
            continue
        elif not re.search('-i \d+ -n', a):
            print('invalid course id')
            continue
        elif not re.search('-n \d+ edu', a):
            print('invalid course capacity')
            continue
        else:
            a = Course(u[4], u[6], int(u[8]))
            courses.append(a)
            print('course added successfully!')
            redescribec(courses)
    elif re.search('edu get course -i .+ edu', a) and len(a.split(' '))==6 and current_menu=='student menu':
        if not a.split(' ')[4] in idc:
            print('incorrect course id')
            continue
        elif a.split(' ')[4] in lastlog[-1].courses:
            print('you already have this course')
            continue
        elif a.split(' ')[4] in idc:
            for c in courses:
                if c.id==a.split(' ')[4]:
                    if c.course_students==c.capacity:
                        print('course is full')
                        continue
                    else:
                        lastlog[-1].courses.append(c.id)
                        c.course_students += 1
                        print('course added successfully!')
                        continue
    elif a == 'edu exit edu':
        break
    else:
        print('invalid command')
