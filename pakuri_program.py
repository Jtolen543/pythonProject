from pakudex import Pakudex


def menu():
    print("Pakudex Main Menu")
    print("-" * 17)
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    print("Enter max capacity of the Pakudex: 30")
    print("The Pakudex can hold 30 species of Pakuri\n")
    while True:
        menu()
        choice = int(input("What would you like to do? "))
        if choice == 1:
            if Pakudex.get_size == 0:
                print("No Pakuri in Pakudex yet!")
            else:
                for i, pakuri in enumerate(Pakudex().pakudex_party):
                    print(f"{i + 1}. {pakuri}")
                print("\n")
        if choice == 2:
            specie_name = input("Enter the name of the species to display: ")
            if specie_name in Pakudex().pakudex_party:
                details = ["Species", "Attack", "Defense", "Speed"]
                stats = [specie_name] + Pakudex().get_stats(specie_name)
                for detail, stat in details, stats:
                    print(f"{detail}: {stat}")
                print("\n")
            elif specie_name not in Pakudex().pakudex_party:
                print("Error: No such Pakuri!\n")


main()
