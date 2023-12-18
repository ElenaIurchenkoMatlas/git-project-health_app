first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[-2:]
print(fixed_first_name)

password = "theycallme\"crazy\"91"
print(password)


def password_generator(user_name):
    password = ""
    
    # Iterate through the indices of user_name
    for i in range(len(user_name)):
        # Add the letter at the previous index to password
        password += user_name[i - 1]
    
    return password

# Example usage:
original_username = "AbeSimp"
result = password_generator(original_username)
print(result)

cool_fruit = "watermelon"
print(len(cool_fruit))
print(cool_fruit[len(cool_fruit) - 2])