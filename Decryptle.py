# Decryptle (Decryption Game)
#
# Short Test script to demonstrate arithmetic, logical, and unary operators
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-28
#

import random as rnd
from texttable import Texttable

TARGET_WORDS_LIST = open('./target_words.txt')
TARGET_WORDS = (TARGET_WORDS_LIST.read()).split()
TARGET_WORDS_LIST.close()
DEBUG_LIST = ["abcde", "zyxwv", "lmnop"]
ref_table = Texttable()
ref_dict = {str(x + 1): chr((ord("a")+x)) for x in range(0, 26)}
ref_table.add_rows([(list(ref_dict.keys())[0:13]), (list(ref_dict.values())[0:13])], False)
ref_table.add_rows([(list(ref_dict.keys())[13:26]), (list(ref_dict.values()))[13:26]], False)

def encrypt(unencrypted_word, cypher_index):
    output = ""
    for character in unencrypted_word:
        if character.isalpha():
            cypher_letter = ord(character) + cypher_index
            if cypher_letter > ord('z'):
                # cypher_letter = ord('a') + (cypher_letter - ord('z'))
                cypher_letter = cypher_letter - 26
            elif cypher_letter < ord('a'):
                # cypher_letter = ord('z') - (ord('a') - cypher_letter)
                cypher_letter = cypher_letter + 26
            output += chr(cypher_letter)

        else:
            output += character

    return output

def get_random_hints(number_of_hints):
    hint_words = [None] * number_of_hints
    for i in range(0, number_of_hints):
        hint = rnd.choice(TARGET_WORDS).lower()
        if hint not in hint_words:
            hint_words[i] = hint
        else:
            i -= 1
    return hint_words

def get_encrypted_hints():
    difficulty = input("How many hints would you like?: ")
    if difficulty == "debug":
        print("///   DEBUG MODE   ////")
        cypher_key = int(input("Enter cypher index: "))
        hints = dict.fromkeys(DEBUG_LIST)
    else:
        try:
            difficulty = int(difficulty)
        except ValueError:
            print("Invalid number of hints. Defaulting to 3")
            difficulty = 3
        cypher_key = rnd.randrange(1, 26)
        hints = dict.fromkeys(get_random_hints(difficulty))
    for word in hints.keys():
        hints[word] = encrypt(word, cypher_key)
    cypher = [cypher_key, hints]
    return cypher

def play():
    encrypted_cypher = get_encrypted_hints()
    while True:
        print(ref_table.draw())
        print()
        for hint in list(encrypted_cypher[1].values()):
            print(hint)
        print()
        guess_key = int(input("What is the cypher key? "))
        if guess_key == encrypted_cypher[0]:
            for decrypted_word in encrypted_cypher[1].keys():
                print(f"{encrypted_cypher[1][decrypted_word]} : {encrypt(encrypted_cypher[1][decrypted_word], (0 - guess_key))}")
            print("\nCorrect!! You Win!")
            input("\npress enter to quit.... ")
            quit()
        elif guess_key == 500: # debug code
            print(f"key = {encrypted_cypher[0]}")
            for answer in list(encrypted_cypher[1].items()):
                print(answer)
            print()
        else:
            for guess_decryption in list(encrypted_cypher[1].values()):
                print(encrypt(guess_decryption, (0 - guess_key)))
            print("\nincorrect cypher key. Try again")
