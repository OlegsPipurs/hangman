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
        print(chr(27) + "[2J")    
        print(73*'='+'\nSpēle karātavas. Minamais vārds ir '+str(len(minamais_vards))+' simboli garš. Tev ir sešas dzīvības.\n'+73*'=') # Izvada speles pazinojumu ar ,ima,o vardu garumu + Speles vizualizacija atdalijums ar "=" 

        while dzivibas != 0:                                                    # While cikla sakums definējums dzivibas nav= ar 0
            burts = input('Ievadi minēto burtu: ').upper()                      # Ievaditais burts tiek parveidots uz lielo burtu
            print(chr(27) + "[2J") 
            if burts.isalpha() == False:                                        # Parbauda vai simbols ir alfabetisks
                # https://ozzmaker.com/add-colour-to-text-in-python/
                print('\033[0;31;40m Ievadīji nekorektu simbolu' + '\033[0;37;40m')                     # Izvada pazinojumu, nekorektu simbolu ievadi
            elif burts in minamais_vards and len(burts) == 1:                   # Tiek veikts parbaudijums uz ievadito burtu, vai ir alfabetisks un garums ir vienads ar 1
                uzmietie_burti.add(burts)                                       # Pievieno sarakstam uzminamie burti
                neuzminetie_burti.add(burts)                                    # Pievieno sarakstam neminamie burti
                print(neuzminetie_burti)                                        # Izvada neuzminetos burtus
                if ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards) == minamais_vards:          # Pārbauda vai vārds ir pa burtiem atminēts tb vai atmaskotais vārds sakrīt ar minamo vārdu
                    win = 1
                    print('\033[0;32;40m Tu atminēji vārdu! Vārds bija: ',minamais_vards  + '\033[0;37;40m')         # Izdrukā paziņojumu par vārda atminēšanu                                                                                                   # Speles gaita mainas karodzina vērtiba
                    break
            elif len(burts) > 1 and len(burts) != len(minamais_vards):           # Tiek veikta parbaude ievadita simbolu garums ir vienads ar minamo varda garumu    
                if burts == 'FITA':                                              # easter egg čīterime atminoties klasiku!!! =] doom ftw \m/
                    print('  '.join(minamais_vards[::2].upper()))                # Izvada katru otro burtu !BONUS
                else:
                    print('\033[0;31;40m Nepareizs vārda garums, mini vēlreiz' + '\033[0;37;40m')
            elif len(burts) > 1 and len(burts) == len(minamais_vards) and burts != minamais_vards:  #Tiek veikta parbaude minamais vards tika uzminets
                neuzminetie_vardi.add(burts)
                print(neuzminetie_vardi)
                print('\033[0;31;40m Nepareizs vārds, mini vēlreiz!' + '\033[0;37;40m') 
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
                print('\033[0;31;40m Minētais', burts, 'nav šajā vārdā' + '\033[0;37;40m')                      # Izdrukā paziņojumu, ka spēlētāja ievadītāis burts nav minamajā vārdā
                dzivibas -= 1                                                   # Atņem vienu dzīvību par nepareizu atbildi
                print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")       # Izdrukā paziņojumu ar atlikušo dzīvību skaitu
            
            print('Atminētie burti: ', ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards) + "\033[0;37;40m") # Veic parbaudi par uzmineto burtu minamaja varda, ja tas nav uzminets atstaj "-" 
            
            if dzivibas == 6: 
                print('        |========  ')
                print('        ||      |  ') 
                print('        ||         ') 
                print('        ||         ')
                print('        ||         ')
                print('        ||         ')
                print('___†††======†††____')
            else:
                if dzivibas == 5: 
                    print('        |========  ')
                    print('        ||      |  ') 
                    print('        ||      o   ') 
                    print('        ||         ')
                    print('        ||         ')
                    print('        ||         ')
                    print('___†††======†††____')
                else:
                    if dzivibas == 4: 
                        print('        |========  ')
                        print('        ||      |  ') 
                        print('        ||      o  ') 
                        print('        ||      |  ')
                        print('        ||         ')
                        print('        ||         ')
                        print('___†††======†††____')
                    else:
                        if dzivibas == 3: 
                            print('        |========  ')
                            print('        ||      |  ') 
                            print('        ||      o  ') 
                            print('        ||     -|  ')
                            print('        ||         ')
                            print('        ||         ')
                            print('___†††======†††____')
                        else:
                            if dzivibas == 2: 
                                print('        |========  ')
                                print('        ||      |  ') 
                                print('        ||      o  ') 
                                print('        ||     -|- ')
                                print('        ||         ')
                                print('        ||         ')
                                print('___†††======†††____')
                            else:
                                if dzivibas == 1: 
                                    print('        |========  ')
                                    print('        ||      |  ') 
                                    print('        ||      o  ') 
                                    print('        ||     -|- ')
                                    print('        ||     /   ')
                                    print('        ||         ')
                                    print('___†††======†††____')
                                else:
                                    if win == 1:                                                            # Ja spēlēs karodziņa vērtība ir "True"
                                            print('\033[0;32;40m Tu atminēji vārdu! Vārds bija: ',minamais_vards + "\033[0;37;40m")         # Izdrukā paziņojumu par vārda atminēšanu
                                    else:
                                        print('        |========  ')
                                        print('        ||      |  ') 
                                        print('        ||      o  ') 
                                        print('        ||     -|- ')
                                        print('        ||     / \ ')
                                        print('        ||         ')
                                        print('___†††======†††____')
                                        print('\033[0;31;40m Tu neatminēji vārdu. Vārds bija: ',minamais_vards + "\033[0;37;40m")       # Izdrukā paziņojumu par vārda neuzminēšanu