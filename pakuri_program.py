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
    print(f"The Pakudex can hold {pak.get_capacity()} species of Pakuri\n")
    while True:
        menu()
        choice = int(input("What would you like to do? "))
        if choice == 1:
            if pak.get_size() == 0:
                print("No Pakuri in Pakudex yet!\n")
            else:
                print("\nPakuri in Pakudex:")
                for i, pakuri in enumerate(pak.pakudex_party):
                    print(f"{i + 1}. {pakuri}")
                print("\t")
        elif choice == 2:
            specie_name = input("Enter the name of the species to display: ")
            if specie_name in pak.pakudex_party:
                details = ["Species", "Attack", "Defense", "Speed"]
                stats = [specie_name] + pak.get_stats(specie_name)
                data = dict(zip(details, stats))
                print('\t')
                for key, value in data.items():
                    print(f"{key}: {value}")
                print('\t')
            elif specie_name not in pak.pakudex_party:
                print("Error: No such Pakuri!\n")
        elif choice == 3:
            if pak.get_size() == pak.get_capacity():
                print("Error: Pakudex is full!\n")
            else:
                pak_add = input("Enter the name of the species to add: ")
                if pak_add in pak.pakudex_party:
                    print("Error: Pakudex already contains this species!\n")
                elif pak.add_pakuri(pak_add):
                    print(f"Pakuri species {pak_add} successfully added!\n")
        elif choice == 4:
            pak_evolve = input("Enter the name of the species to evolve: ")
            if pak.evolve_species(pak_evolve):
                print(f"{pak_evolve} has evolved!\n")
            else:
                print("No such Pakuri!\n")
        elif choice == 5:
            pak.sort_pakuri()
            print("Pakuri have been sorted!\n")
        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            break


main()
