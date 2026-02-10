print("tehtava_1")
name = input("Anna nimesi")
print("hello",  name)


print("tehtava_2")
import math
ympyran_sade = int(input("Anna sade"))
pinta_ala = math.pi *(ympyran_sade**2)
print(f"ympyran sade on {ympyran_sade}: ja pinta-ala on {pinta_ala: .2f}")


print("tehtava_3")
kanta = float(input("Anna kanta"))
korkeus = float(input("Anna korkeus"))
suorakulmion_pinta_ala = (kanta*korkeus)
suorakulmion_piiri = 2 *(kanta+korkeus)
print(f"suorakulmion pinta-ala on {suorakulmion_pinta_ala: .2f}")
print(f"suorakulmion piiri on {suorakulmion_piiri: .2f}")


print("tehtava_4")
kokonaisluku1 = int(input("Anna kokonaisluku1"))
kokonaisluku2 = int(input("Anna kokonaisluku2"))
kokonaisluku3 = int(input("Anna kokonaisluku3"))
kl_summa = (kokonaisluku1+kokonaisluku2+kokonaisluku3)
kl_tulo = (kokonaisluku1*kokonaisluku2*kokonaisluku3)
kl_keskiarvo = (kokonaisluku1+kokonaisluku2+kokonaisluku3)/3
print(f"kl_summa on {kl_summa: .2f}")
print(f"kl_tulo on {kl_tulo: .2f}")
print(f"kl_keskiarvo on {kl_keskiarvo: .2f}")


print("tehtava_5")
leiviska = float((input("anna leiviskat")))
naula = float((input("anna naulat")))
luoti = float((input("anna luodit")))
leiviska_luoti = leiviska * 20 * 32
naula_luoti = naula * 32
yhteensa_luoti = luoti + naula_luoti + leiviska_luoti
yhteensa_gramma = yhteensa_luoti * 13.3
kilogramma = int(yhteensa_gramma /1000)
gramma = yhteensa_gramma - (kilogramma * 1000)
print("massa nykymittojen mukaan:")
print(f"{kilogramma} kilogrammaa ja {gramma: .2f} grammaa")

print("tehtava_6")
import random
koodi1 = "".join([str(random.randint(0, 9)) for _ in range(3)])
koodi2 = "".join([str(random.randint(1, 6)) for _ in range(4)])
print(f"Koodi 1 (3 numeroa, 0-9): {koodi1}")
print(f"Koodi 2 (4 numeroa, 1-6): {koodi2}")
