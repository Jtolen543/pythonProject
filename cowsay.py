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
            return cow
    else:
        return None


def main():
    cows = HeiferGenerator().get_cows()
    animal_list = [cow.name for cow in cows]
    if len(sys.argv) == 1:
        print("".join(sys.argv[1:]) + "")
        print(find_cows("heifer", cows))
    elif sys.argv[1] == "-l":
        list_cows(cows)
    elif sys.argv[1] == "-n":
        obj = find_cows(sys.argv[2], cows)
        if len(sys.argv) > 3 and sys.argv[2] in animal_list:
            print(" ".join(sys.argv[3:]) + "")
            print(obj.image)
        else:
            print(f"Could not find {sys.argv[2]} cow!")
        if isinstance(obj, Dragon):
            if obj.can_breathe_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")
    else:
        print(" ".join(sys.argv[1:]) + "")
        print(find_cows("heifer", cows))


if __name__ == "__main__":
    main()
