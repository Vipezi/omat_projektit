#! /usr/bin/python3

# Kuinka kirjoitta konsoliin

print("Moikka, mä oon Ville. Oon toisen vuoden koodari opiskelija!")
print("#######################\n")

def plussaa(numero1, numero2):
    vastaus = numero1 + numero2
    return vastaus

# Tässä konsoli kysyy sinulta kaksi numeroa. Ensimmäinen kirjoittama numero tallentuu "numero1"
# toinen numero tallentuu numerolla kaksi 
#
numero1, numero2 = input("Mitkä numerot haluat minun plussaavan? ").split()
numero1=int(numero1)
numero2=int(numero2)
vastaus = plussaa(numero1, numero2)

print(vastaus)