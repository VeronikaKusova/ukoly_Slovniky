from random import choice

seznamOtazek = ['Kdo?', 'S kým?','Co dělali?','Kde?','Kdy?']

#fce pro vlastní dotazování
def dotazovani(seznamOtazek):
    otazky_odpovedi = {}
    for otazka in seznamOtazek:
        odpovedi = [] # seznam odpovědí pro jednu otázku
        odpovedi.append(input(otazka))
        otazky_odpovedi[otazka] = odpovedi
        while True: #dokud neřekne NE (chce přejít na další otázku) + na každou otázku se ale zeptá minimálně jednou
            stejnaOtazka = input('Chcete znova odpovědět na tu samou otázku? [ano/ne]')
            if stejnaOtazka == 'ne': #chci přejít na další otázku
                break
            elif stejnaOtazka == 'ano': #stejná otázka znovu
                    odpovedi.append(input(otazka))
                    otazky_odpovedi[otazka] = odpovedi
            else:
                print('Je nutné zadat ''ano'' nebo ''ne''!!!')
    return otazky_odpovedi

# fce pro náhodný výběr odpovědi
def vyberOdpovedi(otazky_odpovedi):
    vybraneOdpovedi = []
    for polozka in otazky_odpovedi:
        vyber = choice(otazky_odpovedi[polozka])
        vybraneOdpovedi.append(vyber)
    return vybraneOdpovedi

# fce pro sestavení věty
def vypis_vety(vybraneOdpovedi):
    print('Vysledna věta je:')
    for slovo in vybraneOdpovedi:
        print(slovo, end=' ')

vypis_vety(vyberOdpovedi(dotazovani(seznamOtazek)))
