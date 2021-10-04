print("===============")
print("Spēle karātavas")
print("===============")
dzivibas = 6                                             #Dzivibu sakotnejais daudzums
minetieburt = []                                         #Mineto Burtu cikls
minetievardi = []                  #<<<<<<<<<<< new shit mineeto vaardu saraksts......
vards = ("abols".upper())                                #Minetais vards
x1 = list(vards.upper())                                 #Maina type uz list, lai salidzinatu pret progresu
progress = ['-','-','-','-','-']                         #Tiek demonstrets aizklatais vards ar "-" zimem
#uzminets = False                                #Sakotnejais mineto definejums  - False
while dzivibas > 0 and x1 != progress:                          #Kamer dzivibas vairak par nulli
    print(progress)                                             #Izvada progresu
    user_input =str(input("Ievadiet burtu vai visu vārdu: ").upper())          #Jaievada minetais burts
    if user_input.isalpha() == True:
        if list(user_input) == x1:
                print('Tu atminēji vārdu! Spēle beigusies' + str(x1))
                exit()
        else:
                        minetievardi.append(user_input) 
                        print('Nepareizs minējums. Mēģini vēlreiz!')
        if len(user_input) != len(x1):
                                print("Nepareiza vārda garums")

    else:
            print('Ievadīji nekorektu simbolu')             #Izvada pazinojumu, nekorektu simbolu ievadi
            continue                                           #Funkcija tiek aptureta un izpildas nakamie nosacijumi
    minetieburt.append(user_input)                          #Burti tiek parveidoti par lieliem
    a=user_input                                            #A mainigais lietotaja ievade
    b=vards[0]                                              #B mainigais pirmajam varda burtam "A"
    c=vards[1]                                              #C mainigais pirmajam varda burtam "B"
    d=vards[2]                                              #D mainigais pirmajam varda burtam "0"1
    e=vards[3]                                              #E mainigais pirmajam varda burtam "L"
    f=vards[4]                                              #F mainigais pirmajam varda burtam "S"
    if a==b:                                                #Parbauda pirmo ievadito burtu ar varda pirmo burtu
            print("Uzmineji burtu")                         #Izvada ja ir pareizs minejums
            progress[0] = 'A'
            print(minetieburt)
    elif a==c:
            print("Uzmineji burtu")
            progress[1] = 'B'
            print(minetieburt)
    elif a==d:
            print("Uzmineji burtu")
            progress[2] = 'O'
            print(minetieburt)
    elif a==e:
            print("Uzmineji burtu")
            progress[3] = 'L'
            print(minetieburt)
    elif a==f:
            print("uzmineji burtu")
            progress[4] = 'S'
            print(minetieburt)
    else:
            print("Neuzminēji burtu")
            dzivibas -= 1
            print('Atlikušās dzīvības: ' + dzivibas * "\u2764\uFE0F")
            print(minetieburt) 
else:
    if x1 == progress:                                      #pārbaude vai progress un minamais vārdssakrīt
        print("Tu atminēji vārdu: " + str(x1))                          #ja sakrīt paziņo par uzvaru
        exit()                                              #iziet no spēles
    else:
        print("Spēle beigusies Tu zaudēji, veiksmi nākamajā reizē!")               #GAME OVER!!!
        exit()                                              #iziet no spēles
