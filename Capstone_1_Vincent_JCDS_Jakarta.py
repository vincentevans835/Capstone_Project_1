import string
import random
from datetime import date

kalimat = """
---------------------------------------
Selamat Datang di Rumah Sakit Anak Muda

List Menu:
1.Menampilkan Daftar Pasien
2.Menambah Data Pasien
3.Menghapus Data Pasien
4.Mengubah Data Pasien
5.Exit Progam
"""



def Unik():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res
def my_print():
    print("Daftar Pasien")
    print("\nID\t\t|Nama")
    for i in pasien:
        print(f'{i["ID"]}\t\t|{i["Nama"]}')
def mencari(key,value):
    i = 0
    for j in range(len(pasien)):
        if pasien[j][key] == value:
            break
        else:
            i+=1
    return i
def jenis_penyakit():
    sakit=""
    print("Jenis Penyakit:")
    noKe = 1
    for i in Dokter:
        print(f'{noKe}.{i}')
        noKe+=1
    a = int(input("Masukkan Angka : "))

    noKe = 1
    for i in Dokter:
        if a == noKe:
            sakit+=i
            break
        noKe+=1

    return sakit
def masuk_tgl():
    while(True):
        x, y, z = input("Masukkan Tanggal Lahir (Hari Bulan Tahun)  :").split()
        if x.isdigit()==False or y.isdigit()==False or z.isdigit()==False:
             print("Silahkan Input Tanggal dengan Benar")
        else:
            break
    return x,y,z
def masuk_data(ID):
    today = date.today()
    nama = input("Masukkan Nama Pasien : ")
    x,y,z = masuk_tgl()
    tgl_lahir = "{}/{}/{}".format(x,y,z)
    tmpt_lahir = input("Masukkan Tempat Lahir :")
    H_1 = today.strftime("%d/%m/%Y")
    sakit=jenis_penyakit()

    t = {
            "ID" : ID,
            "Nama":nama.capitalize(),
            "Tanggal Lahir":tgl_lahir,
            "Tempat Lahir":tmpt_lahir.capitalize(),
            "Hari Pertama":H_1,
            "Riwayat Sakit":[sakit]
        }
    pasien.append(t)
    my_print()
def print_pasien(i):
    print("--------------------------------------")
    for x,y in pasien[i].items():
        if x=="Riwayat Sakit":
            print(f'{x}\t: ')
            for sakit in y:
                print(f'\tPenyakit: {sakit}')
                print(f'\tDokter\t: {Dokter[sakit]["Nama Dokter"]}')
                print(f'\tRuang\t: {Dokter[sakit]["Ruang"]}')
                print("")
        else:
            print(f'{x}\t: {y}')

Dokter={
    'Hidung Mampet':{
        'Nama Dokter':'Dr.Achmad',
        'Ruang':'100'
    },
    'Demam':{
        'Nama Dokter':'Dr.Reza',
        'Ruang':'101'
    },
    'Batuk':{
        'Nama Dokter':'Dr.Deo',
        'Ruang':'102'
    }
}

Pasien1 = {
    "ID" : Unik(),
    "Nama":"Vincent",
    "Tanggal Lahir":"5/1/2001",
    "Tempat Lahir":"Medan",
    "Hari Pertama":"5/7/2022",
    "Riwayat Sakit":["Hidung Mampet","Batuk"]
}
pasien = []
pasien.append(Pasien1)

while(True):
    print(kalimat)
    menu = int(input())
 #--------------------------------------------------------------------------------------------- 
 # Menu 1 Selesai Di Check    
    if menu==1:
        while(True):
            print("--------------------------------------")
            my_print()
            print("\nPilih Menu")
            print("1.Lihat Detail Pasien")
            print("2.Kembali Ke Menu Utama")
            a = input("Masukkan Imput : ")
            if a=="1":
                ID = input("Masukkan Nama ID : ").upper()
                i = mencari("ID",ID)
                if i<len(pasien):
                    print_pasien(i)
                else:
                    print("--------------------------------------")
                    print("Pasien Tidak Ditemukan")
            elif a=="2":
                break
            else:
                print("Masukkan Imput Yang Benar")
 #---------------------------------------------------------------------------------------------   
 # Menu 2 Selesai Di Check        
    elif menu==2:
        print("--------------------------------------")
        print("Menu Menambah Data Pasien")
        ID = Unik()
        masuk_data(ID)
 #---------------------------------------------------------------------------------------------  
 # Menu 3 Selesai Di Check     
    elif menu==3:
        print("--------------------------------------")
        print("Menu Menghapus Data Pasien")
        my_print()
        ID = input("Masukkan ID Pasien : ").upper()
        for i in pasien:
            if i['ID'] == ID:
                alamat = pasien.index(i)
                del pasien[alamat]
                print
        my_print()
 #---------------------------------------------------------------------------------------------       
    elif menu==4:
        while(True):
            print("--------------------------------------")
            print("Menu Merubah Data Pasien")
            my_print()
            ID = input("\nMasukkan Nama (Enter Untuk Kembali Ke Menu Utama) : ").upper()
            if ID=="":
                break
            while(True):
                print("--------------------------------------")
                print("Pilih Data Yang Ingin Dirubah")
                print("1.Tambah/Menghapus Penyakit")
                print("2.Nama")
                print("3.Tgl Lahir")
                print("4.Tempat Lahir")
                print("5.Rubah Total")
                print("6.Kembali Ke Menu\n")
                i = mencari("ID",ID)
                print(f'Nama Pasien : {pasien[i]['Nama']}')
                inpt = input("Masukkan Angka : ")
                if inpt=="1":
                    n = input("Tambah/Menghapus : ").capitalize()
                    if n=="Tambah":
                        noKe = 1
                        for k in pasien[i]["Riwayat Sakit"]:
                            print("--------------------------------------")
                            print(f'{noKe}. {k}')
                            noKe+=1
                        sakit = jenis_penyakit()
                        if sakit in pasien[i]["Riwayat Sakit"]:
                            print("Data Sudah Ada")
                        else:
                            pasien[i]["Riwayat Sakit"].append(sakit)
                        print_pasien(i)

                    elif n=="Menghapus":
                        noKe = 1
                        for k in pasien[i]["Riwayat Sakit"]:
                            print(f'{noKe}. {k}')
                            noKe+=1
                        a = int(input("Masukkan Angka : "))
                        del pasien[i]["Riwayat Sakit"][a-1]
                        print_pasien(i)
                    else :
                        print("Imput anda Salah")                        
                elif inpt=="2":                   
                    n = input("Masukkan Nama Yang Baru: ").capitalize()
                    pasien[i]['Nama'] = n
                    nama = n
                    print_pasien(i)
                elif inpt=="3":
                    x,y,z = masuk_tgl()
                    tgl_lahir = "{}/{}/{}".format(x,y,z)
                    pasien[i]['Tanggal Lahir'] = tgl_lahir
                    print_pasien(i)
                elif inpt=="4":
                    n = input("Masukkan Tempat Lahir Yang Baru : ")
                    pasien[i]['Tempat Lahir'] = n
                    print_pasien(i)
                elif inpt=="5":
                    ID = pasien[i]['ID']
                    del pasien[i]
                    masuk_data(ID)
                    i = mencari("ID",ID)
                    print_pasien(i)
                elif inpt=="6":
                    break
                else:
                    print("Masukkan Imput yang benar")
 #---------------------------------------------------------------------------------------------     
    elif menu==5:
        break