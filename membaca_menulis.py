class operasifile():
    def __init__self():
        pass

    def baca_File(self, file):
        try:
            with open(file, "r") as membaca:
                return membaca.read()
        except FileNotFoundEror as lost:
            return "File Tidak Ditemukan: {}".format(lost)

    def tulis_File(self, file, isi, metode):
        if metode == 'w':
            try:
                with open(file, "w") as menulis:
                    tulis.write(isi)
                    print('file berhasil ditulis')
            except Exception as e:
                return "Maaf terjadi kesalahan saat menulis file ini {}: {}".format(file, e)
        else:
            try:
                with open(file, "a")as tambah:
                    tambah.write(isi)
                    print('file berhasil ditulis')
            except Exception as e:
                return "Maaf terjadi kesalahan saat menulis file ini {}: {}".format(file,e)

#contoh penggunaan 
objek = operasifile()
objek.tulis_File("membaca_menulis.txt", "\nfile ini tidak ada", 'a')
print(objek.baca_File("membaca_menulis.txt"))

