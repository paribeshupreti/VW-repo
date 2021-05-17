# Virtual Peoples

# 11/18/20

import time
import random
import copy





class ind:
    total = 0
    all = []

    def __init__(self, first, last, age, sex, race):
        self.first = first
        self.last = last
        self.age = age
        self.sex = sex
        self.race = race

        self.all.append(self)
        ind.total += 1

    def fullname(self):
        x = '{} {}'.format(self.first, self.last)
        print("My name is", x)

    def introduction(self):
        first = '{}'.format(self.first)
        last = '{}'.format(self.last)
        age = '{}'.format(self.age)
        sex = '{}'.format(self.sex)
        race = '{}'.format(self.race)

        print("\nName: ", first, last, "\n"
                                       "\nAge: ", age, "\n"
                                                       "\nSex: ", sex, "\n"
                                                                       "\nRace: ", race, "\n")


activities = [
    'playing basketball', 'eating', 'sleeping', 'cooking', 'playing soccer',
    'traveling'
]
boy_names = ['John', 'Michael']
girl_names = ['Emily', 'Lupita']
all_names = boy_names + girl_names


def run():
    print("Welcome to your Virtual land!\n")
    # time.sleep(1)

    correct = input("Enter security code: ")
    while correct != "123":
        print("\nIncorrect!\n")
        correct = input("Please enter the correct security code:  ")
    else:
        print(run2())


def run2():
    print("\nCorrect! Accessing...\n")
    # time.sleep(1.5)

    print("Currently there are", ind.total,
          "people in file, as listed below: \n")

    counter = 1
    for each in ind.all:
        print(counter, ")", each.first, "\n")
        counter += 1

    ind_question()


names_copy = []


def zoom_in(x):
    boy_names_copy = copy.deepcopy(boy_names)
    girl_names_copy = copy.deepcopy(girl_names)
    all_names_copy = copy.deepcopy(all_names)
    activities_copy = copy.deepcopy(activities)

    random.shuffle(all_names_copy)
    random.shuffle(activities_copy)

    for i in range(0, (len(boy_names_copy) + len(girl_names_copy))):
        name_selection = all_names_copy.pop()

        if x in name_selection and name_selection in boy_names_copy:
            print(x + " is " + activities_copy.pop() + " with " + x.replace(x, "himself"))
            time.sleep(1)
        elif x in name_selection and name_selection in girl_names_copy:
            print(x + " is " + activities_copy.pop() + " with " + x.replace(x, "herself"))
            time.sleep(1)
        else:
            print(x + " is " + activities_copy.pop() + " with " + name_selection)


def ind_question():
    ind_name = input("\nwhose file would you like to access?: ")

    if ind_name == "john" or ind_name == "John":
        john_file()

    elif ind_name == "michael" or ind_name == "Michael":
        michael_file()

    elif ind_name == "emily" or ind_name == "Emily":
        emily_file()

    elif ind_name == "Lupita" or ind_name == "lupita":
        lupita_file()
    else:
        print("\nName not found, try again...")
        time.sleep(0.5)
        ind_question()


def john_file():
    x = input(
        "\nWhat would you like to do next?: "
        "\n1) View john's info: "
        "\n2) see what he's doing:"
        " \n3) Go back to name selection: "
    )

    if x == '1':
        john.introduction()
        time.sleep(1)
        john_file()

    elif x == '2':
        zoom_in('John')
        time.sleep(1)
        john_file()

    elif x == '3':
        ind_question()

    else:
        print("\nInvalid, try again...")
        time.sleep(0.5)
        john_file()


def emily_file():
    x = input(
        "\nWhat would you like to do next?: "
        "\n1) View emily's info: "
        "\n2) see what she's doing: "
        "\n3) Go back to name selection: "
    )

    if x == '1':

        emily.introduction()
        time.sleep(1)
        emily_file()

    elif x == '2':
        zoom_in('Emily')
        time.sleep(1)
        emily_file()

    elif x == '3':
        ind_question()

    else:
        print("\nInvalid, try again...")
        time.sleep(0.5)
        emily_file()


def michael_file():
    x = input(
        "\nWhat would you like to do next?: "
        "\n1) View michael's info: "
        "\n2) see what he's doing: "
        "\n3) Go back to name selection: "
    )

    if x == '1':

        michael.introduction()
        time.sleep(1)
        michael_file()

    elif x == '2':
        zoom_in('Michael')
        time.sleep(1)
        michael_file()

    elif x == '3':
        ind_question()

    else:
        print("\nInvalid, try again...")
        time.sleep(0.5)
        michael_file()


def lupita_file():
    x = input(
        "\nWhat would you like to do next?: "
        "\n1) View Lupita's info: "
        "\n2) see what she's doing: "
        "\n3) Go back to name selection: "
    )

    if x == '1':

        lupita.introduction()
        time.sleep(1)
        lupita_file()

    elif x == '2':
        zoom_in('Lupita')
        time.sleep(1)
        lupita_file()

    elif x == '3':
        ind_question()

    else:
        print("\nInvalid, try again...")
        time.sleep(0.5)
        lupita_file()


john = ind("John", "A", 30, "Male", "white")
michael = ind("Michael", "A", 23, "Male", "white")
emily = ind("Emily", "A", 27, "Female", "white")
lupita = ind("Lupita", "G", 21, "Female", "Hispanic")

print(run())

# to do
# make two list for activities, one with one's self, loop the two
# fix the "see what their doing"
# tkinter
