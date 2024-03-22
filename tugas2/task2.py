"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 2:
In this second part of the first programming assignment, you should write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered in decimal format with two digits after the decimal. For example, if the user enters 5000 10 15 -1 the program should display 5025.00 (Each number will be separated by a carriage return). 
"""

total = 0
while True:
    number = input("Masukkan sebuah angka (or -1 to stop): ")
    if number == "-1":
        break
    total += float(number)
print(f"Total dari semua angka yang dimasukkan: {total:.2f}")
