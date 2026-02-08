print("tehtävä_1")
name = input("Anna nimesi")
print("hello",  name)


print("tehtävä_2")
import math
ympyran_sade = int(input("Anna sade"))
pinta_ala = math.pi *(ympyran_sade**2)
print(f"ympyran sade on {ympyran_sade}: ja pinta-ala on {pinta_ala: .2f}")


print("tehtävä_3")
kanta = float(input("Anna kanta"))
korkeus = float(input("Anna korkeus"))
suorakulmion_pinta_ala = (kanta*korkeus)
suorakulmion_piiri = 2 *(kanta+korkeus)
print(f"suorakulmion pinta-ala on {suorakulmion_pinta_ala: .2f}")
print(f"suorakulmion piiri on {suorakulmion_piiri: .2f}")


print("tehtävä_4")
kokonaisluku1 = int(input("Anna kokonaisluku1"))
kokonaisluku2 = int(input("Anna kokonaisluku2"))
kokonaisluku3 = int(input("Anna kokonaisluku3"))
kl_summa = (kokonaisluku1+kokonaisluku2+kokonaisluku3)
kl_tulo = (kokonaisluku1*kokonaisluku2*kokonaisluku3)
kl_keskiarvo = (kokonaisluku1+kokonaisluku2+kokonaisluku3)/3
print(f"kl_summa on {kl_summa: .2f}")
print(f"kl_tulo on {kl_tulo: .2f}")
print(f"kl_keskiarvo on {kl_keskiarvo: .2f}")


print("tehtävä_5")
