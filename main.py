print("---Welcome to Virtual Pet---")
print("")


def feed():
    """Feeding the pet to decrease hunger level"""
    pass

def play():
    """Playing with the pet increases happiness and decreases energy"""
    pass

def rest():
    """Increases energy, slightly  decreases hunger."""
    pass

def update_leaderboard():
    pass


    

def name_pet():
    """Naming pet and attribute initialization"""
    print("--Name your pet--")
    pet_name  = input("Name you pet: ")
    hunger = 50
    happiness = 50
    energy = 50    
    
    while True:
        print("What would you like to do?")
        print(f"1. Feed {pet_name}.")
        print(f"2. Play with {pet_name}.")
        print(f"3. Rest {pet_name}.")
        print(f"4. Quit and Save your progress.")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            feed()
        elif choice == "2":
            play()
        elif choice == "3":
            rest()
        elif choice == "4":
            print("Thanks for playing.")
            update_leaderboard(pet_name, hunger, happiness, energy)
            break
        else:
            print("Invalid choice! \n")


def view_leaderboard():
    pass


def main():
    while True:
        print("---Virtual Pet Menu---")
        print("1. Start/Resume Game")
        print("2. View Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name_pet()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            print("Thank you for playing.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Choose again.")


if __name__ == "__main__":
    main()