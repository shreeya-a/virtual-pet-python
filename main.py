import random
import os

PETS_FILE = "./Task-1/Virtual-pet/pet-list.txt "

print("---Welcome to Virtual Pet---")
print("")

def status_check(pet_name, hunger, happiness, energy):
    print(f"Current Status of {pet_name}")
    print(f"hunger: {hunger}")
    print(f"happiness: {happiness}")
    print(f"energy: {energy}")
    if hunger == 0 or happiness == 0 or energy == 0:
        print(f"Oh no! {pet_name} is sick. Please take care of your pet.")
        return False
    if hunger >= 80 or happiness >= 80 or energy >= 80:
        print(f"Oh wow! {pet_name} has won!! They are super happy and energetic.")
        
    return True

def feed(hunger):
    """Feeding the pet to decrease hunger level"""
    if hunger > 0 and  hunger < 100:
        hunger += 10   
        if hunger > 100:
            hunger = 100 
    return hunger
    

def random_event():
    # List of random events that can increase a pet's happiness level
    happiness_boost_events = [
    "The pet finds a toy and happily plays with it.",
    "The owner gives the pet a surprise treat.",
    "The pet enjoys a refreshing bath.",
    "The pet meets a new furry friend and plays together.",
    "The pet gets a belly rub or head scratches.",
    "The owner takes the pet on a longer-than-usual walk.",
    "The pet explores a new area full of interesting smells.",
    "The owner spends extra time playing with the pet.",
    "The pet successfully learns a new trick and is rewarded.",
    "The pet discovers a sunny spot to nap in.",
    "The pet receives a special new toy.",
    "The owner returns home earlier than usual, surprising the pet.",
    "The pet experiences a gentle rain and enjoys the fresh smell.",
    "The owner praises the pet with an enthusiastic tone.",
    "The pet chases a butterfly or a bird outside.",
    "The pet has a peaceful cuddle session with the owner.",
    "The owner sets up a fun obstacle course for the pet.",
    "The pet gets to play in a puddle or shallow water.",
    "The owner shares a small piece of their food (safe for the pet).",
    "The pet finds an unexpected stash of its favorite toy or item."
    ]
    event = random.choice(happiness_boost_events)
    print(event)
    return 10
    


def play(happiness, energy):
    """Playing with the pet increases happiness and hunger, decreases energy"""
    happiness += random_event()
    if  happiness > 100:
        happiness = 100
    if energy > 0:
        energy -= 10
    return  happiness, energy

def rest(energy, hunger):
    """Increases energy, slightly  decreases hunger."""
    energy += 10
    if energy > 100:
        energy = 100
    if hunger > 0:
        hunger -= 5
    return energy, hunger
    

def update_file(pet_name, hunger, happiness, energy):
    pass

def old_pet():
    pass
    

def new_pet():
    """Naming pet and attribute initialization"""
    print("--Name your pet--")
    pet_name  = input("Name: ").capitalize()
    hunger = 50
    happiness = 50
    energy = 50  
    hunger, happiness, energy = pet_actions(pet_name, hunger, happiness, energy)
    print (pet_name, hunger, happiness, energy)
    
    # Load inventory if it exists
    # if os.path.exists(PETS_FILE):
    #     print("\nResuming your adventure...")
    # else:
    #     print("\nStarting a new adventure...")
    #     # Create an empty  file
    #     with open(PETS_FILE, "w") as file: 
    #         file.write(f"{pet_name}: {hunger} {happiness} {energy}" + "\n")
    
    
 
    
def pet_actions(pet_name, hunger, happiness, energy):
    good_status = True 
    while good_status:
        print("What would you like to do?")
        print(f"1. Feed {pet_name}.")
        print(f"2. Play with {pet_name}.")
        print(f"3. Rest {pet_name}.")
        print(f"4. Quit and Save your progress.")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hunger = feed(hunger)          
        elif choice == "2":
            happiness, energy = play( happiness, energy)
        elif choice == "3":
            energy, hunger = rest(energy, hunger)
        elif choice == "4":
            print("Thanks for playing.")
            # update_file(pet_name, hunger, happiness, energy)
            return hunger, happiness, energy
        else:
            print("Invalid choice! \n")
        
        good_status =  status_check(pet_name, hunger, happiness, energy)
        



def main():
    is_game = True
    while is_game:
        print("---Virtual Pet Menu---")
        print("1. Create a new pet")
        print("2. Resume with older pet")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_pet()
        elif choice == "2":
            old_pet()
        elif choice == "3":
            print("Thank you for playing.")
            print("Goodbye!")
            is_game = False
            break
        else:
            print("Invalid choice! Choose again.")



if __name__ == "__main__":
    main()