class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def _str_(self):
        return f"Persegi Panjang {self.panjang} dan lebar {self.lebar}"
    

try:
    panjang_input = float(input("Masukkan panjang (cm): "))
    lebar_input = float(input("Masukkan lebar (cm): "))

    pp = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm^²")

except ValueError:
    print("Input harus berupa angka.")