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
            array = " ".join([name.get_species() for name in self.pakudex_party])
            return array

    def get_stats(self, species):
        if species not in [name.get_species() for name in self.pakudex_party]:
            return None
        else:
            for specie in self.pakudex_party:
                if specie.get_species() == species:
                    self.stats = [specie.get_attack(), specie.get_defense(), specie.get_speed()]
                    return self.stats

    def sort_pakuri(self):
        self.pakudex_party.sort(key=lambda x: x.get_species())
        return self.pakudex_party

    def add_pakuri(self, species):
        if len(self.pakudex_party) == 20:
            return False
        if len(self.pakudex_party) != 20:
            name = Pakuri(species)
            self.pakudex_party.append(name)
            return True

    def evolve_species(self, species):
        if species not in [name.get_species() for name in self.pakudex_party]:
            return False
        else:
            for specie in self.pakudex_party:
                if specie.get_species() == species:
                    specie.evolve()
                    return True
        return False
