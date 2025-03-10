class BankaHesabi:
    def __init__(self, bakiye):
        self.__bakiye = bakiye  # Private değişken

    def bakiye_goster(self):
        return self.__bakiye

hesap = BankaHesabi(1000)
print(hesap.bakiye_goster())  # 1000
