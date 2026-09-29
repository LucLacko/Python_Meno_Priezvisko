#1.	Vypíšte čísla od 1 do 10.
for cislo in range(1, 11):
    print(cislo)
#2.	Vypíšte párne čísla od 1 do 20.
for cislo in range(2, 21, 2):
    print(cislo)
#3.	Pri číslach od 1 do 20 vypíšte, či sú párne alebo nepárne.
for cislo in range(1, 21):
    if cislo % 2 == 0:
        print(cislo, "je párne číslo.")
    else:
        print(cislo, "je nepárne číslo.")
#4.	Vypíšte všetky čísla od 1 do 30, ktoré sú deliteľné tromi.
for cislo in range(1, 31):
    if cislo % 3 == 0:
        print(cislo)
#5.	Nech používateľ zadá číslo. Vypíšte jeho násobky od 1-násobku po 10-násobok.
cislo = int(input("Zadajte číslo: "))

for nasobok in range(1, 11):
    print(nasobok, "×", cislo, "=", nasobok * cislo)
#Ak používateľ zadá číslo 5, program vypíše:
#1 × 5 = 5
#2 × 5 = 10
#3 × 5 = 15
#...
#10 × 5 = 50
