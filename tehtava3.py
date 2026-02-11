print("tehtava1")
kuhan_mitta = float(input("anna kuhan mitta"))

if kuhan_mitta <= 37:
    print(f"kuhasi on {37 - kuhan_mitta} cm alimittainen, laske kuha jarveen")
else:
    print("kuhaa ei tarvitse laskea jarveen")

print("tehtava2")
hytti= input("anna hyttiluokkasi")
if hytti == "LUX":
    print("hyttisi on: parvekkeellinen hytti yläkannella")
elif hytti == "A":
    print("hyttisi on: ikkunallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("hyttisi on: ikkunaton hytti autokannen yläpuolella")
elif hytti == "C":
    print("hyttisi on: ikkunaton hytti autokannen alapuolella")
else:
    print("anna oikea hyttiluokka")

print("tehtava3")
sukupuoli = input("anna sukupuolsesi")
hemoglobiini = float(input("anna hemoglobiini arvosi"))
if sukupuoli == "nainen":
    if hemoglobiini >= 117:
        print("hemoglobiinisi on alhainen")
    elif 117 <= hemoglobiini  < 175:
        print("hemoglobiinisi on normaali")
    elif 175 <= hemoglobiini:
        print("hemoglobiinisi on korkea")
elif sukupuoli == "mies":
    if hemoglobiini >= 134:
        print("hemoglobiinisi on alhainen")
    elif 134 <= hemoglobiini < 195:
        print("hemoglobiinisi on normaali")
    elif 195 <= hemoglobiini:
        print("hemoglobiinisi on korkea")

print("tehtava4")
vuosiluku = int(input("anna vuosiluku"))
if vuosiluku % 4 == 0:
    print("annettu vuosi on karkausvuosi")
elif vuosiluku % 100 == 400:
    print("annettu vuosi on karkausvuosi")
else:
    print("annettu vuosi ei ole karkausvuosi")
