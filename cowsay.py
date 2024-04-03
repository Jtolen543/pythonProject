import sys
from dragon import Dragon
from heifer_generator import HeiferGenerator


def list_cows(cows):
    print("Cows available: ", end="")
    for names in [cow.name for cow in cows]:
        print(names, end=" ")


def find_cows(name, cows):
    for cow in cows:
        if name == cow.name:
            return cow.image
    else:
        return f"Could not find {name} cow!"


def main():
    cows = HeiferGenerator().get_cows()
    animal_list = [cow.name for cow in cows]
    if len(sys.argv) == 1:
        print("".join(sys.argv[1:]) + "")
        print(find_cows("heifer", cows))
    elif sys.argv[1] == "-l":
        list_cows(cows)
    elif sys.argv[1] == "-n":
        cow_name = find_cows(sys.argv[2], cows)
        if len(sys.argv) > 3 and sys.argv[2] in animal_list:
            print(" ".join(sys.argv[3:]) + "")
        print(cow_name)
        if isinstance(cow_name, Dragon):
            if cow_n
    else:
        print(" ".join(sys.argv[1:]) + "")
        print(find_cows("heifer", cows))


if __name__ == "__main__":
    main()

