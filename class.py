class PersegiPanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return self.panjang * self.lebar

    def _str_(self):
        return f"persegi Panjang, Panjang {self.panjang} cm, dan lebar {self.lebar} cm"


try:
    panjang_input = int(input("Masukan panjang (cm):"))
    lebar_input = int(input("Masukan lebar (cm):"))
    
    pp = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm^²")

except ValueError:
    print("Input harus berupa angka.")