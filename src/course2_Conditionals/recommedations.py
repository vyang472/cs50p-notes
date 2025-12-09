print("Answer follow questions and I can recommand games for you^^")
def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Single or Multiple? ")

    if difficulty == "Difficult":
        if players == "Single":
            recommand("Clash Royale")
        elif players == "Multiple":
            recommand("Brawl Stars")
        else:
            print("Enter a valid number of players^>^")
        
    elif difficulty == "Casual":
        if players == "Single":
            recommand("Minecraft")
        elif players == "Mutipal":
            recommand("Poker")
        else:
            print("Enter a valid number of players^>^")
   
    else:
        print("Please choose one difficulty from top^.^")
    


def recommand(game):
    print("You might like the game: ", game)

main()