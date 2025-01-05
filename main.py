import random
import os
import time
from inputimeout import inputimeout, TimeoutOccurred


PETS_FILE = "pet-list.txt "

print("---Welcome to Virtual Pet---")
print("")

def status_check(pet_name, hunger, happiness, energy):
    print(f"Current Status of {pet_name}")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Energy: {energy}")
    if hunger == 0 or happiness == 0 or energy == 0:
        print(f"Oh no! {pet_name} is sick. Please take care better care  of your future pets.")
        return False
    if hunger >= 80 and happiness >= 80 and energy >= 80:
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
    happiness_boost = random.choice([5, 10])
    return happiness_boost
    


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
    


def update_pet_details(pet_name, hunger, happiness, energy, lines):
    """Update the file for the old pet."""
    updated_lines = []
    for line in lines:
        name, attributes = line.split(":")
        if name.strip().lower() == pet_name.lower():
            # Update the line with new attributes
            updated_lines.append(f"{pet_name}: {hunger} {happiness} {energy}\n")
        else:
            updated_lines.append(line)

    with open(PETS_FILE.strip(), "w") as file:
        file.writelines(updated_lines)
        
    print(f"Current Status of {pet_name}")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Energy: {energy}")
    print(f"Progress for {pet_name} updated successfully.\n")


def old_pet(pet_name):
    """Load an existing pet's details."""
    if not os.path.exists(PETS_FILE.strip()):
        print("No saved pets found. Create a new one!.\n")
        return

    with open(PETS_FILE.strip(), "r") as file:
        lines = file.readlines()

    pet_found = False
    for line in lines:
        name, attributes = line.split(":")
        if name.strip().lower() == pet_name.lower():
            hunger, happiness, energy = map(int, attributes.split())
            pet_found = True
            time.sleep(2)
            print(f"Here's {pet_name}!")
            print(f"Loading {pet_name}'s Vitals:")
            print(f"Hunger={hunger}")
            print(f"Happiness={happiness}")
            print(f"Energy={energy}")
            hunger, happiness, energy = pet_actions(pet_name, hunger, happiness, energy)
            # Update the file with new details after playing
            if hunger > 0 and happiness > 0 and energy > 0:
                update_pet_details(pet_name, hunger, happiness, energy, lines)
                break
            else:
                break

    if not pet_found:
        print(f"No old pet found with the name {pet_name}.")
        return
   
# Defining attributes of new pet
def new_pet(pet_name):
    """Naming pet and attribute initialization"""
    # print("--Name your pet--")
    # pet_name  = input("Name: ").capitalize()
    hunger = 50
    happiness = 50
    energy = 50  
    hunger, happiness, energy = pet_actions(pet_name, hunger, happiness, energy)
    
    
 
# Add new pet to file
def add_to_file(pet_name, hunger, happiness, energy):
    """Saves the pet's attributes to the pet file."""
    with open(PETS_FILE.strip(), "a") as file:  
        file.write(f"{pet_name}: {hunger} {happiness} {energy}\n")
    
    print(f"Current Status of {pet_name}")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Energy: {energy}")
    print(f"Progress for {pet_name} saved successfully.")
    print("----------------------------------------\n")

# Actions choice list
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
            add_to_file(pet_name, hunger, happiness, energy)
            return hunger, happiness, energy
        else:
            print("Invalid choice! \n")
        
        good_status =  status_check(pet_name, hunger, happiness, energy)
        
        if not good_status:  # If the status check returns False, exit the loop
            return hunger, happiness, energy
    

        



def main():

    while True:
        print("---Virtual Pet Menu---")
        print("1. Create a new pet")
        print("2. Resume with older pet")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            print("\n--Name your pet--")
            try:
                pet_name  = inputimeout(prompt="Name: ", timeout=8)
                pet_name = pet_name.capitalize()
                new_pet(pet_name)
            except TimeoutOccurred:
                print("\n OOPS! You took too long!")
            
        elif choice == "2":
            try:
                pet_name  = inputimeout(prompt="Enter the name of existing pet: ", timeout=8)
                pet_name = pet_name.capitalize()
                old_pet(pet_name)
            except TimeoutOccurred:
                print("\n OOPS! You took too long!")
        elif choice == "3":
            print("Thank you for playing.")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Choose again.")



if __name__ == "__main__":
    main()