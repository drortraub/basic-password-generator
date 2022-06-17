import password_gen
import random

def manu():
    print("Welcome to the Password Generator!")
    print("Please select the type of password you want to generate:")
    print("1. Semi-random password")
    print("2. Fully random password")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        nr_letters = int(input("How many letters do you want in your password? "))
        nr_symbols = int(input("How many symbols do you want in your password? "))
        nr_numbers = int(input("How many numbers do you want in your password? "))
        password_gen.semi_rendome_generate_password(nr_letters, nr_symbols, nr_numbers)
    elif choice == "2":
        leng_of_password = int(input("How long do you want your password to be? "))
        password_gen.fully_random_generate_password(password_gen.list_of_characters, leng_of_password)
    elif choice == "3":
        print("Goodbye!")
        exit()


manu()