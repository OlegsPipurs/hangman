class game:
    def __init__(self, play):
        self.play = play
    def play(xxx):
        minamais_vards = str(xxx.upper())       # Mainiga varda virknes un lielo burtu definejums
        uzmietie_burti = set()                  
        neuzminetie_burti = set()
        neuzminetie_vardi = set()
        dzivibas = 6
        win = 0          # Speles karodzina definejums izmantots 1 un 0    
        print(73*'='+'\nSpēle karātavas. Minamais vārds ir '+str(len(minamais_vards))+' simboli garš. Tev ir sešas dzīvības.\n'+73*'=') # Izvada speles pazinojumu ar ,ima,o vardu garumu + Speles vizualizacija atdalijums ar "=" 

        while dzivibas != 0:                                                    # While cikla sakums definējums dzivibas nav= ar 0
            burts = input('Ievadi minēto burtu: ').upper()                      # Ievaditais burts tiek parveidots uz lielo burtu
            if burts.isalpha() == False:                                        # Parbauda vai simbols ir alfabetisks
                print('Ievadīji nekorektu simbolu')                             # Izvada pazinojumu, nekorektu simbolu ievadi
            elif burts in minamais_vards and len(burts) == 1:                   # Tiek veikts parbaudijums uz ievadito burtu, vai ir alfabetisks un garums ir vienads ar 1
                uzmietie_burti.add(burts)                                       # Pievieno sarakstam uzminamie burti
                neuzminetie_burti.add(burts)                                    # Pievieno sarakstam neminamie burti
                print(neuzminetie_burti)                                        # Izvada neuzminetos burtus
                print('Atminētie burti: ', ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards))    # Veic parbaudi par uzmineto burtu minamaja varda, ja tas nav uzminets atstaj "-" 
                if ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards) == minamais_vards:          # Pārbauda vai vārds ir pa burtiem atminēts tb vai atmaskotais vārds sakrīt ar minamo vārdu
                    win = 1                                                                                                   # Speles gaita mainas karodzina vērtiba
                    break
            elif len(burts) > 1 and len(burts) != len(minamais_vards):           # Tiek veikta parbaude ievadita simbolu garums ir vienads ar minamo varda garumu    
                if burts == 'IDDQD':                                             # easter egg čīterime atminoties klasiku!!! =] doom ftw \m/
                    print('  '.join(minamais_vards[::2].upper()))                 #Izvada katru otro burtu !BONUS
                else:
                    print('Nepareizs vārda garums, mini vēlreiz')
            elif len(burts) > 1 and len(burts) == len(minamais_vards) and burts != minamais_vards:  #Tiek veikta parbaude minamais vards tika uzminets
                neuzminetie_vardi.add(burts)
                print(neuzminetie_vardi)
                print('Nepareizs vārds, mini vēlreiz!') 
                dzivibas -= 1                                                    # Nepareiza minejuma gaidjuma atņem dzivibu
                print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")        # Izvada atlikuso dzivu skaitu
            elif burts == minamais_vards:                                        #Vards tika uzminets pa burtiem, tiek mainits karodzina veriba uz Win "True"
                win = 1
                dzivibas = 0
            elif burts == '':                                                   # Spēlētājs nav ievadījis burtu vai vārdu un nospiedis Enter
                print('Patīk enter spaidīt?')                                   # Izdrukā paziņojumu, ka spēlētājs nav ievadījis burtu vai visu vārdu
            else:
                neuzminetie_burti.add(burts)                                    # Papildina spēlētāja ievadīto burtu neuzminēto burtu sarakstā
                print(neuzminetie_burti)                                        # Izdrukā neuzminēto burtu sarakstu
                print('Minētais', burts, 'nav šajā vārdā')                      # Izdrukā paziņojumu, ka spēlētāja ievadītāis burts nav minamajā vārdā
                dzivibas -= 1                                                   # Atņem vienu dzīvību par nepareizu atbildi
                print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")       # Izdrukā paziņojumu ar atlikušo dzīvību skaitu
        if win == 1:                                                            # Ja spēlēs karodziņa vērtība ir "True"
                print('Tu atminēji vārdu! Vārds bija: ',minamais_vards)         # Izdrukā paziņojumu par vārda atminēšanu
        else:
                print('Tu neatminēji vārdu. Vārds bija: ',minamais_vards)       # Izdrukā paziņojumu par vārda neuzminēšanu