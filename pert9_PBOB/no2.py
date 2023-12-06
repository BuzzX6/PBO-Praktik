class Komputer(object):
    def __init__(self, nama, pabrikan, harga, jenis):
        self.nama = nama
        self.pabrikan = pabrikan
        self.harga = harga
        self.jenis = jenis

    def Semangat(self):
        print('Komputer GO GO!')

    def Info(self):
        print("-- INFORMASI -- ")
        print("Nama: " + self.nama)
        print("Pabrikan:" + self.pabrikan)
        print(f"Harga: Rp. {self.harga:,.2f}")
        print("jenis: " + self.jenis)


class Processor(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, jumlah_core):
        self.jumlah_core = jumlah_core
        super().__init__(nama, pabrikan, harga, jenis)

    def SemangatProcessor(self):
        self.Semangat()
        print("Processor cepat")

    def InfoProcessor(self, detail = False):
        self.Info()
        if detail:
            print("Jumlah Core: " + str(self.jumlah_core))

class RAM(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, frekuensi):
        self.frekuensi=frekuensi
        super().__init__(nama, pabrikan, harga, jenis)


    def SemangatRAM(self):
        self.Semangat() 
        print(" Ram Ajibb ")

    def InfoRAM(self, detail = False):
        self.Info()
        if detail:
            print(f"Jumlah Core: {self.frekuensi} MHZ")



class Hardisk(Komputer):
    def __init__(self, nama, pabrikan, harga, jenis, kapasitas):
        self.kapasitas=kapasitas
        super().__init__(nama, pabrikan, harga, jenis)


    def SemangatHardisk(self):
        self.Semangat() 
        print(" HDD Terbaikk! ")

    def InfoHardisk(self, detail = False):
        self.Info()
        print(f"Kapasitas: {self.kapasitas} Tera")


processor = Processor("Intel I7", "Intel", 5000000, "12500H", 12)
print("Informasi tanpa detail :")
processor.InfoProcessor()
print("\n Informasi dosen dengan detail:")
print(processor.InfoProcessor(detail=True))
processor.SemangatProcessor()

print("_____________======_____________")

ram = RAM("Kingston", "Kingston Technology Corporation", 1700000, "Fury Beast 32GB KIT 3200", 3200)
print("Informasi tanpa detail :")
ram.InfoRAM()
print("\n Informasi dosen dengan detail:")
print(ram.InfoRAM(detail=True))
ram.SemangatRAM()

print("_____________======_____________")

hardisk = Hardisk("WD", "Western Digital Corporation", 850000, "Caviar Blue", 1)
print("Informasi tanpa detail :")
hardisk.InfoHardisk()
print("\n Informasi dosen dengan detail:")
print(hardisk.InfoHardisk(detail=True))
hardisk.SemangatHardisk()