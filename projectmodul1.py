##data collection
Nama = []
Nim = []
Kelas = []
Jurusan = []
Nilaiuts = []
Nilaiuks = []


def Tambah() :
    Name = input ('Masukkan Nama :')
    Nama.append(Name)
    Nm = input ('Masukkan Nim :')
    Nim.append(Nm)
    Kls = input ('Masukkan Kelas :')
    Kelas.append(Kls)
    Jrsn = input ('Masukkan Jurusan :')
    Jurusan.append (Jrsn)
    Nliuts = input ('Masukkan NilaiUts :')
    Nilaiuts.append (Nliuts)
    Nliuks = input ('Masukkan NilaiUks :')
    Nilaiuks.append (Nliuks)
    
    print('Data Tersimpan')
    Menu()



def Baca():
    print('==================================================')
    print('Nim\t| Nama\t| Jurusan| Kelas| Nilaiuts| Nilaiuks|')
    for i in range(len(Nim)):
        print('{}\t| {}\t| {}\t | {}\t| {}\t | {}\t |'. format(Nim[i],Nama[i], Jurusan[i], Kelas[i], Nilaiuts[i], Nilaiuks[i]))
    
    Menu()


def Ubah():
    n = input(('Inputkan Nim :'))
    if n in Nim :
        i = Nim.index(n)
        nama = input('Nama: ')
        Nama[i] = nama
        jurusan = input('Jurusan: ')
        Jurusan[i] = jurusan
        Kls = input('Kelas')
        Kelas[i] = ('Kls')
        nilaiuts = input('Nilaiuts: ')
        Nilaiuts[i] = nilaiuts
        nilaiuks = input('Nilaiuks: ')
        Nilaiuks[i] = nilaiuks
    else:
        print('Nim Tidak Ada')
        Menu()

    
def Hapus():
    n = input(('Masukkan Nim :'))
    if n in Nim:
        Nim.remove(Nim[n])
        Nama.remove(Nama[n])
        Jurusan.remove(Jurusan[n])
        Kelas.remove(Kelas[n])
        Nilaiuts.remove(Nilaiuts[n])
        Nilaiuks.remove(Nilaiuks[n])
    else:
        print('Nim tidak ada')
        Menu()

def Selesai():
    Menu()

def Menu():
    print('========================================')
    print('input Data Nilai Mahasiswa')
    print('=========================================')
    print('| 1. Tambah Data                        |')
    print('| 2. Lihat Data Mahasiswa               |') 
    print('| 3. Ubah Data Mahasiswa                |')
    print('| 4. Hapus Data Mahasiswa               |')
    print('| 5. Selesai                            |')
    print('=========================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        Tambah()
    elif pilih2 == '2' :
        Baca()
    elif pilih2 == '3' :
        Ubah()
    elif pilih2 == '4' :
        Hapus()
    elif pilih2 == '5' :
        Selesai()
    else:
        tidak = input ('Menu Tidak Ada ')
        Menu()



Menu()