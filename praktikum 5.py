# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:37:15 2020

@author: Asus
"""

print("====================================")
print("======>  program Input Data  <======")
print("====================================")
data = {}
while True:
    print("")
    m = input("===>> (L)ihat, (T)ambah, (U)bah, (H)apus, (c)ari, (k)eluar <<=== : ")
    print("========================================================")
    print("| No | | Nama | Nim | Tugas | Uts | Uas | Akhir | ")
    print("========================================================")
    print(">>>>>>>>>>>>>>>>> Tidak Ada Data <<<<<<<<<<<<<<<<<<<<<<<<")
    if m.lower() == 'K' :
        break
    
    elif m.lower() == 'l' :
        print("DAFTAR NIALI")
        print("=======================================================")
        print(" NO |  NAMA  |  NIM  |  TUGAS  |  UTS  |  UAS | AKHIR |")
        print("=======================================================")
        i = 0
        for x in data.items():
            i += 1
            print(" 1 | {0:9} | {1:9} | {2:9} | {3:9} | {4:9} | {5:9} |" .format(
                x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4],))
            
        else:
            print("Tidak Ada Data")
            
    elif m.lower() == 't':
           print("Tambah Data")
           nama = input ("Nama      : ")
           nim =input ("Nim     : ")
           tugas = float (input ("masukan nilai tugas : "))
           uts = float (input ("Masukan Nilai UTS : "))
           uas = float (input ("Masukan Nilai UAS : "))
           akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
           data[nama] = nim, tugas, uts, uas, akhir
           
    elif m.lower() == 'u':
        print("Ubah Data Mahasiswa")
        nama = input ("Nama     : ")
        if nama in data.keys():
            nim = input ("Nim  : ")
            tugas = float(input("masukan nilai tugas : "))
            uts = float (input ("masukan nilai uts : "))
            uas = float (input ("masukan nilai uas : "))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir 
            
        else:
          print("Tidak Ada data")
        
        
    elif m.lower() == 'h':          
          print("Hapus Data Mahasiswa")
          nama = input("nama : ")
          if nama in data.keys():
                print("Datanya", nama, "adalah {0}". format (data [nama]))
          else:
                print("Tidak ada data")
    
    else:
        print("pilih menu yang tersedia")
            
        

                
            
               