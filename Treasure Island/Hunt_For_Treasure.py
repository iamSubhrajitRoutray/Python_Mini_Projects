import Island_Art

def gameover(reason):
    print(f"\n💀 GAME OVER!")
    print(reason)
    
def playgame():

    print("🏝️ Welcome to Treasure Island. 🏝️")

    print("Your mission is to find the treasure. 🪎\n")


    firstchoice = input("You are at a crossroad.\nWhere do you want to go?\nType 'left' or 'right' : ").lower().strip()

    if firstchoice != "left":
        gameover("🕳️ You fell into a hole! 🕳️")
        return


    print("🌊 You have come to a lake.\nThere is an island in the middle of the lake. 🏝️")
    
    lakechoice = input("Type 'wait' for a boat or 'swim' across : ").lower().strip()
    
    if lakechoice != "wait":
        print("You got attacked by the trout!")
        return
        
        
    print("🏠 You have arrived at the island unharmed.\nThere is a house with 3 doors:\n🔴 Red\n🔵 Blue\n🟡 Yellow\n Which color do you choose? ")
    
    doorchoice = input("Choose a door (red/blue/yellow): ").lower().strip()
    
    if doorchoice == "red":
        
        print("🔥 You got burned by the fire. 🔥")
    
    elif doorchoice == "blue":
        
        print("🐉 You got eaten by the beasts. 🐉")
    
    elif doorchoice == "yellow":
        print("\n🏆 Congratulations! ")
        print("🪎 You found the treasure! 🪎")
        print("YOU WIN!")
    else:
        gameover("❌ That door does not exist. ❌")


while True:
    
    playgame()
    
    playagain = input("Do you want to play again? (yes/no) : ").lower()
    
    if playagain != "yes":
        print("Thanks for playing!")
        break

