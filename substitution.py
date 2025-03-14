import random

MESSAGE = "the quick brown fox jumps over the lazy dog"

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
    guess_keys = dict.fromkeys(list(substitution_keys.values()))

    while True:
        guess_keys = get_guess(guess_keys)
        current_message = encrypt_message(cipher_message, guess_keys)
        if check_guess(MESSAGE, current_message):
            input("Press enter to quit...  ")
            quit()

play()
# # test = ['a', 'b', 'c', 'd', 'e']
#
# print(get_encrypted_alphabet())