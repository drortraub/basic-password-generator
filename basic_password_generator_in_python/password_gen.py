import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','@', '^','-']
list_of_characters = (letters + numbers + symbols)

password_list = []

#function to generate semi-random password
def semi_rendome_generate_password(nr_letters, nr_symbols, nr_numbers):
    for i in range(nr_letters):
        password_list.append(random.choice(letters))
    for i in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for i in range(nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = ''.join(password_list)
    print("your password is: ",password)

#function to generate fully rendom password
def fully_random_generate_password(list_of_characters, leng_of_password):
    for i in range(leng_of_password):
        password_list.append(random.choice(list_of_characters))
    random.shuffle(password_list)
    password = ''.join(password_list)
    print("your password is: ",password)
