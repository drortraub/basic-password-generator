#!/usr/bin/env python3

password_list = []

for char in range(1, nr_letters+1): 
  password_list += random.choice(letters)
  
for char in range(1, nr_letters+1): 
  password_list += random.choice(symbols)
  
for char in range(1, nr_letters+1): 
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"your password is: {password}")