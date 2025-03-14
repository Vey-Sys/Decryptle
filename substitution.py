import random
from texttable import Texttable

MESSAGE = "the quick brown fox jumps over the lazy dog"
user_table = Texttable()


def shuffle_letters(unshuffled):
    shuffled = unshuffled
    random.shuffle(shuffled)
    return shuffled

def get_encrypted_alphabet():
    alphabet = []
    encrypted_alphabet = []
    for position in list(range(0, 26)):
        alphabet.append(chr(ord('a') + position))
        encrypted_alphabet.append(chr(ord('a') + position))
    encrypted_alphabet = shuffle_letters(encrypted_alphabet)
    print(alphabet)
    print(encrypted_alphabet)
    substitution_cipher = dict(zip(alphabet, encrypted_alphabet))
    substitution_cipher[" "] = " "
    print(substitution_cipher)
    return substitution_cipher

def init_user_alphabet(origin_dict):
    user_keys = list(origin_dict.values())
    user_starting_values = user_keys
    user_starting_dict = dict(zip(user_keys, user_starting_values))
    return user_starting_dict

def print_table(user_dict):
    keys = [letter for letter in list(user_dict.keys())]
    keys.sort()
    values = [user_dict[key] for key in keys]
    user_table.reset()
    user_table.add_rows([keys[1:14], values[1:14]], False)
    user_table.add_row(([" "] * 13))
    user_table.add_rows([keys[14:27], values[14:27]], False)
    print(user_table.draw())
    print()
    return

def encrypt_message(message, cipher_key):
    encrypted_message = ''
    for letter in message:
        encrypted_message = encrypted_message + cipher_key[letter]
    print(encrypted_message)
    return encrypted_message

def get_guess(current_keys):
    user_guess = input("pick a letter to substitute: ").lower()
    substitution = user_guess.strip().split('=')
    current_keys[substitution[0]] = substitution[1]
    return current_keys

def check_guess(original, guess_message):
    if guess_message == original:
        print("You Win!")
        return True
    return False

def play():
    substitution_keys = get_encrypted_alphabet()
    cipher_message = encrypt_message(MESSAGE, substitution_keys)
    guess_keys = init_user_alphabet(substitution_keys)
    while True:
        guess_keys = get_guess(guess_keys)
        print_table(guess_keys)
        current_message = encrypt_message(cipher_message, guess_keys)
        if check_guess(MESSAGE, current_message):
            input("Press enter to quit...  ")
            quit()

play()
# # test = ['a', 'b', 'c', 'd', 'e']
#
# print(get_encrypted_alphabet())