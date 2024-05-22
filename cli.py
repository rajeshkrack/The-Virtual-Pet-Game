# ui/cli.py

from pet.pet import Pet, Dog, Cat  # Import Pet and specialized pet classes

def main():
    print("Welcome to Virtual Pet Game!")

    # Create a virtual pet
    pet_name = input("Enter your pet's name: ")
    pet_species = input("Enter your pet's species (Dog or Cat): ")
    pet_age = int(input("Enter your pet's age: "))

    if pet_species.lower() == "dog":
        pet = Dog(pet_name, pet_age)  # Create Dog instance
    elif pet_species.lower() == "cat":
        pet = Cat(pet_name, pet_age)  # Create Cat instance
    else:
        print("Invalid pet species. Please enter 'Dog' or 'Cat'.")
        return

    # Main game loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Groom")
        print("4. Take to vet")
        print("5. Display pet status")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pet.feed()
            print("You feed your pet.")
        elif choice == "2":
            pet.play()
            print("You play with your pet.")
        elif choice == "3":
            pet.groom()
            print("You groom your pet.")
        elif choice == "4":
            pet.take_to_vet()
            print("You take your pet to the vet.")
        elif choice == "5":
            pet.display_status()
            print(f"{pet.get_name()} says: {pet.speak()}")  # Polymorphism
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
