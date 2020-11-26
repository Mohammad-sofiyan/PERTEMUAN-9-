# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:04:23 2020

@author: Asus
"""

n = 0
nm = []
nim = []
tugas = []
uts = []
uas = []
akhir = []

while True:
    nama = input ("nama     :")
    nm.append(nama)
    Nim = input ("nim   :")
    nim.append(Nim)
    Tugas = input ("tugas   :")
    tugas.append(Tugas)
    Uts = input ("uts   :")
    uts.append(Uts)
    Uas = input ("uas   :")
    uas.append(Uas)
    Akhir = (int(Tugas) * .30 ) + (int(Uts) * .35) + (int(Uas) * .35)
    akhir.append(Akhir)
    
    data = ' '
    while data != 'Y' and data != 'T' :
        data = input("Tambah data [Y/T] ?")
        
    n += 1
    if data == 'T':
       break 
   
        
print("=======================================================")
print("NO   | NAMA  | NIM   | TUGAS | UTS | UAS | AKHIR ")
print("=======================================================")

for a in range(n):
    print(" ", a+1, "|", nm[a], "|", nim[a], "|", tugas[a], "|", uts[a], "|", uas[a], "|", akhir[a], "|",)