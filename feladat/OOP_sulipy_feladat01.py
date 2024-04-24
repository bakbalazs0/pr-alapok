class Negyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerület(self):
        return 4 * self.oldal_hossz
    
    def terület(self):
        return self.oldal_hossz ** 2