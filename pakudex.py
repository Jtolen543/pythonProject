from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.stats = None
        self.capacity = capacity
        self.pakudex_party = []

    def get_size(self):
        return len(self.pakudex_party)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.pakudex_party) == 0:
            return None
        else:
            self.pakudex_party = " ".join(self.pakudex_party)
            return self.pakudex_party

    def get_stats(self, species):
        if species not in self.pakudex_party:
            return None
        else:
            self.stats = []
            return self.stats

    def sort_pakuri(self):
        self.pakudex_party = sorted(self.pakudex_party)
        return self.pakudex_party

    def add_pakuri(self, species):
        if len(self.pakudex_party) == 20:
            return False
        if len(self.pakudex_party) != 20:
            name = Pakuri(species)
            print(name)
            self.pakudex_party.append(name)
            return True

    def evolve_species(self, species):
        if species not in self.pakudex_party:
            return False
        elif species in self.pakudex_party:

            return True

test = Pakudex()
test.add_pakuri("Pikachu")
test.add_pakuri("Charazard")
test.add_pakuri("Blastoise")
test.add_pakuri("Venusaur")
print(test.)


