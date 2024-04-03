from dragon import Dragon


class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)
        self.image = image

    def can_breathe_fire(self):
        return False
