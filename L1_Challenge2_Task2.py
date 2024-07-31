#python L1_Challenge2_Task2.py

"""Starting message"""
def greeting():
  return "Welcome to the username creator...Please choose one of the following options: \n 1. Create a username based on a name \n 2. Generate a random username"
print(greeting())

option = input("Enter your choice here: ")


"""Option 1 creates a username by interspersing the user's surname with the user's reversed first name"""
def option_1():
  name = input("What is your first name: ")
  def reverse_name(name):
    return name[::-1]
  forename = reverse_name(name)

  surname = input("What is your surname: ")
  def intersperse_name(forename, surname):
    inter = ""
    i = 0
    while (i < len(forename)) or (i < len(surname)):
      if i < len(forename):
        inter += forename[i]
      if i < len(surname):
        inter += surname[i]
      i += 1
    return inter
  interspersed = intersperse_name(forename, surname)

  def format_name(interspersed):
    new_forename = ""
    new_surname = ""
    half_index = int(len(interspersed)/2)
    new_forname = interspersed[:(half_index)]
    new_surname = interspersed[(half_index):]
    return ("Your username is: {} {}".format(new_forname.title(), new_surname.title()))
  return format_name(interspersed)

"""Task 3 - Generating a random username"""
def option_2():
  import random
  import string
  letters_numbers = string.ascii_lowercase + string.digits

  username = ""
  for i in range(10):
    username += random.choice(letters_numbers)
  return("Your random username is: {} {}".format(username[:5], username[5:]))

"""Choosing option"""
def options():
  if int(option) == 1:
    return(option_1())
  else:
    return(option_2())
print(options())
