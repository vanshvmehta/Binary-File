"""
1. To create a binary file
2. Append records
3. Display the file and the number of records
4. Display the file and the number of students living in Fahaheel
5. Display the file and the number of students paying transport fee > 50KD
6. Search for a student on admission number
"""

import pickle


def create():
    with open('student.dat', 'xb') as f:
        pass
    print('File Created')


def append():
    with open('student.dat', 'ab') as f:
        for i in range(11):
            adno = int(input('Enter Admission number: '))
            name = input('Enter name: ')
            sec = input('Enter section: ')
            area = input('Enter area of residence: ')
            busfee = float(input('Enter transport fees: '))
            rec = {'adno': adno, 'name': name, 'sec': sec, 'area': area, 'busfee': busfee}
            pickle.dump(rec, f)

    print('Records Appended')
    print()


def display():
    with open('student.dat', 'rb') as f:
        count = 0
        try:
            while True:
                rec = pickle.load(f)
                print(rec['adno'], rec['name'], rec['sec'], rec['area'], rec['busfee'], sep='\t')
                count += 1
        except:
            pass
        print()
        print(count, 'Records')
        print()


def area():
    with open('student.dat', 'rb') as f:
        count = 0
        try:
            while True:
                rec = pickle.load(f)
                print(rec['adno'], rec['name'], rec['sec'], rec['area'], rec['busfee'], sep='\t')
                if rec['area'] == 'FAHAHEEL':
                    count += 1
        except:
            pass
        print()
        print(count, 'students live in Fahaheel')
        print()


def busfee():
    with open('student.dat', 'rb') as f:
        count = 0
        try:
            while True:
                rec = pickle.load(f)
                print(rec['adno'], rec['name'], rec['sec'], rec['area'], rec['busfee'], sep='\t')
                if rec['busfee'] > 50:
                    count += 1
        except:
            pass
        print()
        print(count, 'pay transport fee greater than 50KD\n')


def search():
    adno = int(input('Enter the admission number: '))
    with open('student.dat', 'rb') as f:
        try:
            while True:
                rec = pickle.load(f)
                if rec['adno'] == adno:
                    print(rec['adno'], rec['name'], rec['sec'], rec['area'], rec['busfee'], sep='\t')
                    break
            else:
                print('Record not found')
        except:
            pass
        print()


print('''
1. To create a binary file
2. Append records
3. Display the file and the number of records
4. Display the file and the number of students living in Fahaheel
5. Display the file and the number of students paying transport fee > 50KD
6. Search for a student on admission number
7. Exit the menu
''')
opt = 0
while opt != 7:
    opt = int(input('Enter your option: '))
    if opt == 1:
        create()
    elif opt == 2:
        append()
    elif opt == 3:
        display()
    elif opt == 4:
        area()
    elif opt == 5:
        busfee()
    elif opt == 6:
        search()


