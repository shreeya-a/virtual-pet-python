import random
import os
import time
from inputimeout import inputimeout, TimeoutOccurred


PETS_FILE = "pet-list.txt "

print("Welcome to Virtual Pet")
print("-----------------------")
time.sleep(0.5)


def print_current_status(pet_name, hunger, happiness, energy):
            print(f"Loading {pet_name}'s Vitals:")
            time.sleep(0.3)
            print(f"Hunger: {hunger}")
            time.sleep(0.3)
            print(f"Happiness: {happiness}")
            time.sleep(0.3)
            print(f"Energy: {energy}")
            time.sleep(0.3)
            return

def status_check(pet_name, hunger, happiness, energy):
    print(f"Current Status of {pet_name}:")
    print_current_status(pet_name, hunger, happiness, energy)
    
    # print(f"Hunger: {hunger}")
    # print(f"Happiness: {happiness}")
    # print(f"Energy: {energy}")
    if hunger == 0 or happiness == 0 or energy == 0:
        print(f"Oh no! {pet_name} is sick. Please take care better care  of your future pets.\n")
        time.sleep(0.5)
        return False
    if hunger >= 80 and happiness >= 80 and energy >= 80:
        print(f"Oh wow! {pet_name} has won!! They are super happy and energetic.")
        
    return True

def feed(pet_name, hunger):
    """Feeding the pet to decrease hunger level"""
    food_items = {
        "Dog Biscuit": 5,
        "Fish": 10,
        "Chicken": 10,
        "Carrot": 5,
        "Apple": 5,
        "Pizza Slice": 10,
        "Ice Cream": 5,
        "Peanut Butter": 10,
        "Chocolate Cake": 5,
        "Sweet Potato": 10,
        "Spinach": 5,
        "Cheeseburger": 10,
        "Sushi": 10,
        "Burger Patty": 10,
        "Taco": 10
    }

    print("What would you like to feed your pet?")
    for i, (food, level) in enumerate(food_items.items() , 1):
        print(f"{i}. {food} (Hunger Boost: {level})")
    
    try:
        choice = int(input("Enter your choice number: "))
        food_list = list(food_items.keys())
        if 1 <= choice <= len(food_list):
            food_name = food_list[choice - 1]
            hunger_boost = food_items[food_name]
            
            hunger += hunger_boost   
            if hunger > 100:
                hunger = 100 
            time.sleep(0.2)
            print(f"\nYou fed your pet {food_name}.")
            print("{pet_name} is eating...")
            time.sleep(0.2)
            print(f"Hunger increased by {hunger_boost}.\n")
            time.sleep(0.1)
        else:
            print("Invalid choice! Please select a valid food option.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    
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
    time.sleep(0.5)
    print(event)
    time.sleep(1)
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

def rest(pet_name,energy, hunger):
    """Increases energy, slightly  decreases hunger."""
    print(f"{pet_name} is resting...")
    time.sleep(3)
    print(f"{pet_name} is back with more energy!!!!\n")
    time.sleep(1)
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
        
    # print(f"Current Status of {pet_name}")
    # print(f"Hunger: {hunger}")
    # print(f"Happiness: {happiness}")
    # print(f"Energy: {energy}")
    # print(f"Vitals for {pet_name} updated successfully.\n")


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
            print(f"Here comes {pet_name}!\n")
            # print(f"Loading {pet_name}'s Vitals:")
            # print(f"Hunger={hunger}")
            # print(f"Happiness={happiness}")
            # print(f"Energy={energy}")
            print_current_status(pet_name, hunger, happiness, energy)
            if hunger == 0 or happiness == 0 or energy == 0:
                time.sleep(0.1)
                print(f"{pet_name}'s health is too low. The game is over.")
                print("Start with a new pet.")
                time.sleep(0.1)
                print("Loading Pet Menu...\n")
                time.sleep(2)
                return
            hunger, happiness, energy = pet_actions(pet_name, hunger, happiness, energy)
            # Update the file with new details after playing
            # if hunger > 0 and happiness > 0 and energy > 0:
            #     update_pet_details(pet_name, hunger, happiness, energy, lines)
            #     break
            # else:
            #     break
            update_pet_details(pet_name, hunger, happiness, energy, lines)

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
    
    print(f"Progress for {pet_name} saved successfully.")
    return
    


# Actions choice list
def pet_actions(pet_name, hunger, happiness, energy):
    good_status = True 
    while good_status:
        time.sleep(0.5)
        print("\nWhat would you like to do?")
        time.sleep(0.1)
        print(f"1. Feed {pet_name}.")
        time.sleep(0.1)
        print(f"2. Play with {pet_name}.")
        time.sleep(0.1)
        print(f"3. Rest {pet_name}.")
        time.sleep(0.1)
        print(f"4. Quit and Save your progress.")
        time.sleep(0.1)

        choice = input("Enter your choice: ")
        print("")
        
        if choice == "1":
            hunger = feed(pet_name, hunger)          
        elif choice == "2":
            happiness, energy = play( happiness, energy)
        elif choice == "3":
            energy, hunger = rest(pet_name,energy, hunger)
        elif choice == "4":
            time.sleep(0.5)
            print("\nThanks for playing!!")
            time.sleep(0.3)
            add_to_file(pet_name, hunger, happiness, energy)
            # print(f"Current Status of {pet_name}:")
            # time.sleep(0.6)
            # print(f"Hunger: {hunger}")
            # time.sleep(0.6)
            # print(f"Happiness: {happiness}")
            # time.sleep(0.6)
            # print(f"Energy: {energy}")
            # time.sleep(0.6)
            print_current_status(pet_name, hunger, happiness, energy)
            print("\nLoading Pet Menu...\n")
            time.sleep(1.5)
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
            try:
                pet_name  = inputimeout(prompt="Name your pet: ", timeout=8)
                pet_name = pet_name.capitalize()
                new_pet(pet_name)
            except TimeoutOccurred:
                print("\nOOPS! You took too long! Try again.\n")
                time.sleep(0.5)
            
        elif choice == "2":
            try:
                pet_name  = inputimeout(prompt="Enter the name of existing pet: ", timeout=8)
                pet_name = pet_name.capitalize()
                old_pet(pet_name)
            except TimeoutOccurred:
                print("\n OOPS! You took too long!\n")
                time.sleep(0.5)
        elif choice == "3":
            print("Thank you for playing.")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Choose again.")

if __name__ == "__main__":
    main()