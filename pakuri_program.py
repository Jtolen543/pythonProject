from pakudex import Pakudex


def menu():
    print("Pakudex Main Menu")
    print("-" * 17)
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        capacity = input("Enter max capacity of the Pakudex: ")
        if capacity.isdigit():
            pak = Pakudex(int(capacity))
            break
        else:
            print("Please enter a valid size.")
            continue
    print(f"The Pakudex can hold {pak.get_capacity()} species of Pakuri.\n")
    while True:
        menu()
        choice = input("What would you like to do? ")
        if choice.isdigit() is False or int(choice) not in range(1, 7):
            print("Unrecognized menu selection!\n")
        elif int(choice) == 1:
            if pak.get_size() == 0:
                print("No Pakuri in Pakudex yet!\n")
            else:
                print("\nPakuri In Pakudex:")
                for i, pakuri in enumerate(pak.get_species_array()):
                    print(f"{i + 1}. {pakuri}")
                print("\t")
        elif int(choice) == 2:
            specie_name = input("Enter the name of the species to display: ")
            if pak.get_size() != 0 and specie_name in pak.get_species_array():
                details = ["Species", "Attack", "Defense", "Speed"]
                stats = [specie_name] + pak.get_stats(specie_name)
                data = dict(zip(details, stats))
                print('\t')
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("\t")
            else:
                print("Error: No such Pakuri!\n")
        elif int(choice) == 3:
            if pak.get_size() == pak.get_capacity():
                print("Error: Pakudex is full!\n")
            else:
                pak_add = input("Enter the name of the species to add: ")
                if pak.add_pakuri(pak_add):
                    print(f"Pakuri species {pak_add} successfully added!\n")
                else:
                    print("Error: Pakudex already contains this species!\n")
        elif int(choice) == 4:
            pak_evolve = input("Enter the name of the species to evolve: ")
            if pak.evolve_species(pak_evolve):
                print(f"{pak_evolve} has evolved!\n")
            else:
                print("Error: No such Pakuri!\n")
        elif int(choice) == 5:
            pak.sort_pakuri()
            print("Pakuri have been sorted!\n")
        elif int(choice) == 6:
            print("Thanks for using Pakudex! Bye!")
            break


if __name__ == "__main__":
    main()
