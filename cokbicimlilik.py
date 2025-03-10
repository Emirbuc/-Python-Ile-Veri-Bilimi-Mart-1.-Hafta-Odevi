class Geometri:
    def alan(self):
        pass

class Kare(Geometri):
    def __init__(self, kenar):
        self.kenar = kenar
    def alan(self):
        return self.kenar ** 2

class Daire(Geometri):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    def alan(self):
        return 3.14 * self.yaricap ** 2

sekil1 = Kare(4)
print(sekil1.alan())  # 16
sekil2 = Daire(3)
print(sekil2.alan())  # 28.26
