class UTY(object):
    def __init__(self, status, nama, prodi):
        self.nama = nama
        self.status = status
        self.prodi = prodi

    def Semangat(self):
        print('Indonesia Maju Indonesia Tumbuh UTY Hebat')

    def Info(self):
        print("-- INFORMASI -- ")
        print("Nama " + self.nama)
        print("Status :" + self.status)
        print("Program Studi: " + self.prodi)

class Dosen(UTY):
    def __init__(self, status, nama, prodi, nip):
        self.nip = nip
        super().__init__(status, nama, prodi)

    def SemangatDosen(self):
        self.Semangat() #ambil dari kelas UTY
        print("Dosen bermartabat")

    def InfoDosen(self, detail = False):
        self.Info()
        if detail:
            print("NIP: " + str(self.nip))

class Mahasiswa(UTY):
    def __init__(self,  status, nama, prodi, nim):
        self.nim=nim
        super().__init__(status, nama, prodi)


    def SemangatMahasiswa(self):
        self.Semangat() #ambil dari kelas UTY
        print(" Mahasiswa UTY jaya jaya jaya!! ")

    def InfoMahasiswa(self, detail = False):
        self.Info()
        if detail:
            print("NIM: " + str(self.nim))

dosen = Dosen("Dosen", "Bambang", "Informatika", 7002)
print("Informasi tanpa detail :")
dosen.InfoDosen()
print("\n Informasi dosen dengan detail:")
print(dosen.InfoDosen(detail=True))
dosen.SemangatDosen()

print("_____________======_____________")

mahasiswa = Mahasiswa("Mahasiswa", "Atha Redian Naufal", "Informatika", 5220411061)
print("Informasi tanpa detail :")
mahasiswa.InfoMahasiswa()
print("\n Informasi dosen dengan detail:")
print(dosen.InfoDosen(detail=True))
mahasiswa.SemangatMahasiswa()


