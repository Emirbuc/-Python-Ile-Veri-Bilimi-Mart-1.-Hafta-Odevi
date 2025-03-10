class Hayvan:
    def ses_cikar(self):
        print("Ses çıkarılıyor...")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")

kedi = Kedi()
kedi.ses_cikar()  # "Miyav!"
