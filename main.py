import Decryptle
import substitution

if __name__ == "__main__":
    print("Welcome to Decryptle!\n")
    print("Please choose a game mode.")
    game_mode = input("Caesar Cipher (1)       Substitution Cipher (2) : ")
    match game_mode:
        case "1":
            print(Decryptle.play())
        case "2":
            print(substitution.play_substitution())
        case _:
            print("Invalid Gamemode")