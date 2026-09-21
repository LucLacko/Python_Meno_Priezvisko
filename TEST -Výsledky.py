#1. Premenné a dátové typy – 4 b
#a) int, b) float, c) str, d) bool. Za každú správnu odpoveď 1 bod.
#2. Premenné a výstup – 3 b
#Výstup je 12 (1 b). Úprava: print(a * b) (2 b).
#3. Vstup od používateľa – 4 b
meno = input("Zadaj svoje meno: ") #vstup od použivateľa = input
print("Ahoj,", meno + "!")
input()
#Vstup 1 b, uloženie do premennej 1 b, správny výstup 2 b.
#4. Podmienky – 4 b
cislo = int(input("Zadaj celé číslo: "))
if cislo > 0:
    print("Číslo je kladné.")
elif cislo < 0:
    print("Číslo je záporné.")
else:
    print("Číslo je nula.")
input()
#Načítanie a prevod 1 b, vetvenie a podmienky 2 b, správne výstupy 1 b.
#5. Čo vypíše program? – 3 b
#Číslo je väčšie ako 5. Hodnota 8 spĺňa podmienku x > 5, preto sa vykoná vetva if. Výstup 2 b, vysvetlenie 1 b.
#6. Cyklus for a range() – 4 b
#Program vypíše 1, 2, 3, 4, 5 – každé číslo na nový riadok. Cyklus sa vykoná päťkrát. Hodnoty 3 b, počet opakovaní 1 b.
#7. Vytvor cyklus – 3 b
for i in range(2, 11, 2):
    print(i)
#•  2 – prvé vypísané číslo,
#  11 – horná hranica; číslo 11 sa už nevypíše,
#  2 – krok, teda čísla sa zvyšujú vždy o 2.
#Správny rozsah 2 b, správny výpis 1 b.
input()
#8. Samostatná programátorská úloha – 5 b
a = int(input("Zadaj prvé číslo: "))
b = int(input("Zadaj druhé číslo: "))
sucet = a + b
if sucet > 10:
    print("Súčet je väčší ako 10.")
elif sucet == 10:
    print("Súčet je rovný 10.")
else:
    print("Súčet je menší ako 10.")
input()
#Bodovanie: načítanie 1 b, súčet 1 b, podmienky 2 b, výstup 1 b.

#9. Cyklus while – 4 b
i = 1
while i <= 5:
    print(i)
    i += 1
#Bodovanie: inicializácia 1 b, správna podmienka 1 b, výpis 1 b, zmena hodnoty premennej 1 b.
input()
#10. Zoznamy – 4 b
cisla = [4, 7, 2, 9, 3]
print(max(cisla))
print(sum(cisla) / len(cisla))
input()
#Výstup: 9 a 5.0. Maximum 2 b, priemer 2 b.
#11. Nájdi a oprav chybu – 4 b
for i in range(1, 4):
    print(i)
#Výstup: 1, 2, 3 – každé číslo na nový riadok. Dvojbodka 1 b, odsadenie 1 b, správny kód 1 b, výstup 1 b.
