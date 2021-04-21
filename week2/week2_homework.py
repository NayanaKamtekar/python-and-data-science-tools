# Q1

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0 :
        return "FizzBuzz"
    elif num % 3 == 0 :
        return "Fizz"
    elif num % 5 == 0 :
        return "Buzz"
    else : 
        return num

print(fizz_buzz(65))

# Q2

lst= [5, 10, 20]

def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'The index is out of range.'

print(get_item(lst, 2))
print(get_item(lst, 4))

# Q3

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def jet_info(self):
        return f'{self.name} {self.country}'


jet1 = Jet("Lufthansa", "Germany")
print(jet1.jet_info())

# Q5

sample_dic = {'name': 'Nayana', 'surname': 'Kamtekar', 'email': 'abc@gmail.com'}

def is_key_exist(key) :
    if key in sample_dic :
        return "The key exist in a dictionary"
    else :
        return "The key doesn't exist in a dictionary"

print(is_key_exist('email'))
print(is_key_exist('address'))


# Additional Exercises:

# Q6

def showNumbers(limit):
    for i in range(limit+1):
        print(f'{i} {"EVEN" if i%2 == 0 else "ODD"}')

showNumbers(10)

# Q8

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        return f'{self.firstname} {self.lastname}'

person1 = Person('Nayana', 'Kamtekar')

print(person1.print_name())

# Q9

def enter_number():
    try:
        x = input("Enter number: ")
        y = int(x)
        y = y ** 2
        print(y)
    except ValueError:
        print("Invalid input")

enter_number()


# Q10

class Student:
    pass

class Marks:
    pass

student1 = Student()
mark1 = Marks()

print(isinstance(student1, Student))
print(isinstance(mark1, Marks))

print(isinstance(student1, Marks))
print(isinstance(mark1, Student))