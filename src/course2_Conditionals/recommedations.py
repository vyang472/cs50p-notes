print("Answer follow questions and I can recommand games for you^^")
def main():

    difficulty = input("Difficult or Casual?")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Please enter a valid difficulty^^")
        return
    
    players = input("Single or Multiple?")
    if not (players == "Single" or players == "multiple"):
        print("please enter a valid number of players(^*^)")
        return
    
    if difficulty == "Difficult" and players == "Single":
        recommand("Clash Royale")
    
    elif difficulty == "Difficult" and players == "multiple":
        recommand("Brawl Stars")

    elif difficulty == "Casual" and players == "Single":
        recommand("Minecraft")
    
    elif difficulty == "Casual" and players == "multiple":
        recommand("Poker")

    '''difficulty = input("Difficult or Casual? ")
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
'''
    


def recommand(game):
    print("You might like the game: ", game)

main()