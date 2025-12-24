import random
import sys

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    
    return password

# 2. Add this block to handle execution from n8n
if __name__ == "__main__":
    # Check if arguments are provided, otherwise default to 0
    # sys.argv[0] is the script name, so we start at 1
    arg_letters = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    arg_symbols = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    arg_numbers = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    result = generate_password(arg_letters, arg_symbols, arg_numbers)
    print(result)