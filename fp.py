for i in range (1,11):
    print (i)
input()
#parne cisla od 1 po 20
for k in range (1,11):
    print (k*2)
input()
#druha moznost
for c in range (0,21, 2):
    print (c)
input()

#pr cislach od 1 po 20 vypisat ci su parne alebo neparne
for l in range (0,21):
    if l % 2 ==0:
        print ("párne")
    else:
        print ("nepárne")
input()

#cisla od 1 do 30 delitelne tromi
for b in range (0,31):
    if b % 3 ==0:
        print (b)
input()
#alebo
for c in range (3,31,3):
    print (c)
input()

#pouzivatel ma napisat cislo, vypiste jeho nasobky od 1 po 10krat
p=int(input("napis cislo:"))
for z in range(1,11):
    print(p*z)







