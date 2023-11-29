class Hewan:
  def bersuara(self):
    return "Hewan Bersuara"
  
class Kucing:
  def bersuara(self):
    return "Meow!"
  
class Anjing:
  def bersuara(self):
    return "Woof!"

class Tikus(Hewan):
  pass #tikus tidak meng override metode bersuara, akan menggunakan metode dari kelas

#membuat objek dari masing masing kelas
hewan_umum= Hewan()
kucing = Kucing()
anjing = Anjing()
tikus = Tikus()

print(hewan_umum.bersuara())
print(kucing.bersuara())
print(anjing.bersuara())
print(tikus.bersuara())


class Karyawan:
  def __init__(self,nama,idkaryawan,gaji):
    self.nama = nama
    self.idkaryawan = idkaryawan
    self.gaji = gaji

  def tampilkan_info(self):
    print(f"ID: {self.idkaryawan}, Nama: {self.nama}, Gaji: Rp.{self.gaji:,.2f}")


class Manajer(Karyawan):
    def __init__(self, nama, idkaryawan, gaji, departemen):
        super().__init__(nama, idkaryawan, gaji)
        self.departmen= departemen
        self.bawahan = []

    def tambah_bawahan(self,karyawan):
       self.bawahan.append(karyawan)

    def tampilkan_info(self):
       return super().tampilkan_info()