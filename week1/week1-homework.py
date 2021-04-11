from random import randint

# ex:1 Write a python script to print your name and age

my_name = 'Nayana'
print(my_name)

my_age = 34
print(my_age)

my_info = {'name': 'Nayana', 'age': 34}

print(f"My name is {my_info['name']}. I am {my_info['age']} years old")

# ex:2 Create a list of your 5 favorite movies and store it in the variable

My_fav_movies = ['Shrek 2', 'Frozen', 'Shaun The Sheep', "Howl's Moving Castle", 'Spider-Man: Into the Spider-Verse']

# ex:3 Write a Python program to display the first and last colors from the following list.

color_list = ["Red", "Green", "White", "Black"]
print(color_list[0])
print(color_list[-1])

# ex:4 Write a Python script to add a key to a dictionary

sample_dictionary = {0: 10, 1: 20}
sample_dictionary[2] = 30
print(sample_dictionary)


# ex:5 Write a Python program to calculate body mass index.

def calculateBMI(weight, height):
    return weight / height ** 2


print(f"BMI is {calculateBMI(65, 1.56)}")

# Additional Exercises:
# ex:7 Create a tuple with different data types

tuple_diff_type = ('strong', 40, [1, 5, 48], {'country': 'denmark', 'capital': 'copenhagen'})
print(tuple_diff_type)

# ex8:Create a list of 5 city names and convert it into tuples.

city_names_list = ['copenhagen', 'arhus', 'paris', 'belgium', 'london']
print(city_names_list)
print(tuple(city_names_list))

# ex:9 Remove duplicated from the list:
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(f"list with duplicated values{a}")

# a=list(set(a))
# print(f"list with unique values{b}")

dedup = []

for elem in a:
    if elem not in dedup:
        dedup.append(elem)

print(dedup)


# ex:10 Accept a string from user and remove the characters which have odd index values of a given string and print them.
def user(input_string):
    return ''.join(char for index, char in enumerate(input_string) if index % 2 != 0)


print(user('Nayana'))


# ex:6 Guess a number game - between 1 to 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

def number_guess_game():
    random_num = randint(1, 9)
    guess = int(input("Guess a number between 1 to 9: "))

    while (True):
        if random_num == guess:
            print("Well guessed!")
            break
        else:
            guess = int(input("Not quite right, guess again: "))


number_guess_game()
