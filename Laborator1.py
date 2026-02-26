def a_la_b_mod_c(a, b, c):
    p = 1
    a = a % c
    while b:
        if b % 2 == 1:
            p = (p * a) % c
        a = (a * a) % c
        b //= 2
    return p


print(a_la_b_mod_c(2, 40, 105))


def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8") as f:
        alfabet = f.read().strip()
    alfabet = tuple(alfabet)
    return alfabet


def transforma_in_baza_10(numar, alfabet):
    rezultat = 0
    N = len(alfabet)
    for letter in numar:
        rezultat = rezultat * N + alfabet.index(letter)
    return rezultat



#Acesta este exercitiul din tema
def transforma_din_baza_n(numar, baza):
    if numar == 0:
        return "0"

    caractere = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rezultat = ""

    while numar > 0:
        rest = numar % baza
        rezultat = caractere[rest] + rezultat
        numar //= baza
    return rezultat[::-1]

def calcule(nr1_string, nr2_string, baza, operatie):
    n1_10 = int(nr1_string,baza)
    n2_10 = int(nr2_string,baza)

    if operatie == "+":
        rezultat_10 = n1_10 + n2_10
    elif operatie == "*":
        rezultat_10 = n1_10 * n2_10
    else:
        return "Operatie necunoscuta"

    return transforma_din_baza_n(rezultat_10, baza)

print (f"A+B in baza 16: {calcule('A', 'B', 16, '+')}")
print(f"13 * 7 in baza 10: {calcule('13', '7', 10, '*')}")

# alfabet = citeste_alfabet("alfabet.txt")
# n = transforma_in_baza_10("ZECE", alfabet)
# print(n)
# print(alfabet)


