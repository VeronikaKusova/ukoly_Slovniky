# ukol 00 -> fce, která vrací slovník, kde klíče jsou čísla od jedné do n a hodnoty jsou jejich druhé mocniny
def vratSlovnik(n):
    slovnik = {}
    for prvek in range(n):
        slovnik[prvek+1]= (prvek+1)**2
    return slovnik
print(vratSlovnik(5))

# ukol 01 -> fce, která vrací sumu všech klíčů a sumu všech hodnot ve slovníku
def sumy(vstupniSlovnik):
    sumaKlicu = 0
    sumaHodnot = 0
    for prvek in vstupniSlovnik:
        sumaHodnot = sumaHodnot + vstupniSlovnik[prvek]
        sumaKlicu = sumaKlicu + prvek
    return sumaKlicu, sumaHodnot
print(sumy(vratSlovnik(5)))

# ukol 02 -> fce, která dostane řetězec a vrátí slovník, ve kterém jsou klíče jednotlivé znaky řetězce a hodnoty počty výskytů těchto znaků
def retezecSlovnik(retezec):
    slovnikZnaku = {}
    for znak in retezec:
        if znak in slovnikZnaku:
            slovnikZnaku[znak] = slovnikZnaku[znak] + 1
        else:
            slovnikZnaku[znak] = 1
    return slovnikZnaku
print(retezecSlovnik('jelen'))

# ukol 03 -> vypiše obsah slovniku na jednotlivé řádky
def vypis_slovnik(slovnik):
    for polozka in slovnik.items():
        print(polozka)
vypis_slovnik(retezecSlovnik('jelenovi pivo nelej'))
