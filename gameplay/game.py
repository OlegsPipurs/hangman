#Tiek veidota klase game

class game:
    def __init__(self, play):
        self.play = play


    #Nodifineta play metode, ar dažādiem mainigajiem, uzsakot speli attirita ekranu

    def play(xxx):
        minamais_vards = str(xxx.upper()) 
        uzmietie_burti = set()                  
        neuzminetie_burti = set()
        neuzminetie_vardi = set()
        dzivibas = 6
        win = 0
        print(chr(27) + "[2J")
        print(73*'='+'\nSpēle karātavas. Minamais vārds ir '+str(len(minamais_vards))+' simboli garš. Tev ir sešas dzīvības.\n'+73*'=')


        #Dzīvibu salidzinajums, ievaditā burta pārbaude

        while dzivibas != 0:
            burts = input('Ievadi minēto burtu: ').upper()
            print(chr(27) + "[2J") 
            if burts.isalpha() == False:
                # https://ozzmaker.com/add-colour-to-text-in-python/
                print('\033[0;31;40m Ievadīji nekorektu simbolu' + '\033[0;37;40m')


            #Ievadīto burtu pārbaude, tiek pievienots pie minētajiem burtiem un to izvadi 
              
            elif burts in minamais_vards and len(burts) == 1:                   
                uzmietie_burti.add(burts)                                       
                neuzminetie_burti.add(burts)                                    
                print(neuzminetie_burti)


                #Pārbaude vai atklātais vārds sakrit ar minamo vārdu un izvada spēles paziņojumu

                if ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards) == minamais_vards:
                    win = 1
                    print('\033[0;32;40m Tu atminēji vārdu! Vārds bija: ',minamais_vards  + '\033[0;37;40m')
                    break


            #Tiek veikta parbaude ievadita simbolu garums ir vienads ar minamo varda garumu

            elif len(burts) > 1 and len(burts) != len(minamais_vards):               
                

                #Bonus - Ievadot slepeno vārdu, atklāj katru otro burtu minamajā vārdā

                if burts == 'FITA':
                    print('  '.join(minamais_vards[::2].upper()))
                else:
                    print('\033[0;31;40m Nepareizs vārda garums, mini vēlreiz' + '\033[0;37;40m')


            #Minamā vārda pārbaude, vai sakrīt ar menēto vārdu, ja nesakrit atņem dzīvību  
                   
            elif len(burts) > 1 and len(burts) == len(minamais_vards) and burts != minamais_vards:
                neuzminetie_vardi.add(burts)
                print(neuzminetie_vardi)
                print('\033[0;31;40m Nepareizs vārds, mini vēlreiz!' + '\033[0;37;40m') 
                dzivibas -= 1     
                print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")
            

            #Ja ievadītais burts sakrīt ar minamo vārdu iestata mainīgo win un dzīvības

            elif burts == minamais_vards:
                win = 1
                dzivibas = 0


            #Novērš gadījumus ja lietotājs vienkārši spaida enter taustiņu

            elif burts == '':
                print('Patīk enter spaidīt?')
            else:
                neuzminetie_burti.add(burts)
                print(neuzminetie_burti)
                print('\033[0;31;40m Minētais', burts, 'nav šajā vārdā' + '\033[0;37;40m')
                dzivibas -= 1
                print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")
            
            print('Atminētie burti: ', ''.join(burts if burts in uzmietie_burti else '-' for burts in minamais_vards) + "\033[0;37;40m")
            

            """
            Karātavu vizualizācija, atbilstoši atlikušo dzīvību daudzumam
            Ja ir sešas dzīvības
            """

            if dzivibas == 6: 
                print('        |========  ')
                print('        ||      |  ') 
                print('        ||         ') 
                print('        ||         ')
                print('        ||         ')
                print('        ||         ')
                print('___†††======†††____')
            else:
                #ja ir piecas dzīvības
                if dzivibas == 5: 
                    print('        |========  ')
                    print('        ||      |  ') 
                    print('        ||      o   ') 
                    print('        ||         ')
                    print('        ||         ')
                    print('        ||         ')
                    print('___†††======†††____')
                else:
                    #ja ir četrs dzīvības
                    if dzivibas == 4: 
                        print('        |========  ')
                        print('        ||      |  ') 
                        print('        ||      o  ') 
                        print('        ||      |  ')
                        print('        ||         ')
                        print('        ||         ')
                        print('___†††======†††____')
                    else:
                        #ja ir trīs dzīvības
                        if dzivibas == 3: 
                            print('        |========  ')
                            print('        ||      |  ') 
                            print('        ||      o  ') 
                            print('        ||     -|  ')
                            print('        ||         ')
                            print('        ||         ')
                            print('___†††======†††____')
                        else:
                            #ja ir divas dzīvības
                            if dzivibas == 2: 
                                print('        |========  ')
                                print('        ||      |  ') 
                                print('        ||      o  ') 
                                print('        ||     -|- ')
                                print('        ||         ')
                                print('        ||         ')
                                print('___†††======†††____')
                            else:
                                #ja ir viena dzīvības
                                if dzivibas == 1: 
                                    print('        |========  ')
                                    print('        ||      |  ') 
                                    print('        ||      o  ') 
                                    print('        ||     -|- ')
                                    print('        ||     /   ')
                                    print('        ||         ')
                                    print('___†††======†††____')
                                else:


                                    #apstrādā spēles vārda uzminēšanas gadījumu izvadot uzvaras paziņojumu

                                    if win == 1:                                                            
                                            print('\033[0;32;40m Tu atminēji vārdu! Vārds bija: ',minamais_vards + "\033[0;37;40m")


                                    #vārda neuzminēšanas gadījums kad beigušās dzīvības

                                    else:
                                        print('        |========  ')
                                        print('        ||      |  ') 
                                        print('        ||      o  ') 
                                        print('        ||     -|- ')
                                        print('        ||     / \ ')
                                        print('        ||         ')
                                        print('___†††======†††____')
                                        print('\033[0;31;40m Tu neatminēji vārdu. Vārds bija: ',minamais_vards + "\033[0;37;40m")