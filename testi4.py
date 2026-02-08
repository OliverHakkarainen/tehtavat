
leiviska = float(input("Kuinka monta leiviskaa"))
naula = float(input("Kuinka monta naulaa"))
luoti = float(input("Kuinka monta luotia"))

kilo = int(gramma_input // 1000)
gramma = gramma_input%1000
luoti = float(gramma*13,3)
naula = float(luoti*32)
leiviska = float(naula*20)

print(f"{luoti} on {kilo}kg, {gramma}g")
print(f"{naula} on {kilo}kg, {gramma}g ")
print(f"{leiviska} on {kilo}kg, {gramma}g ")

