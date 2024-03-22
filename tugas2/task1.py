"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 1:
Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.
"""

from datetime import datetime, timedelta

def print_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(future_date.strftime("%A, %B %d, %Y"))

days = int(input("Enter number of days from now: "))
print_future_date(days)
