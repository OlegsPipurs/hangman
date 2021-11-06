from gameplay.game import game
from scripts_test.split_difficulity import *

import random
import time
import shelve

print('\033[0;32;40m'''' ____  __   _____ __________    _________________________   _________    _________''')
print('''|    |/ _| /  _  \\\______   \  /  _  \__    ___/  _  \   \ /   /  _  \  /   _____/''')
print('''|      <  /  /_\  \|       _/ /  /_\  \|    | /  /_\  \   Y   /  /_\  \ \_____  \ ''')
print("""|    |  \/    |    \    |   \/    |    \    |/    |    \     /    |    \/        \\""")
print("""|____|__ \____|__  /____|_  /\____|__  /____|\____|__  /\___/\____|__  /_______  / \033[0;37;40m""")
print('\n')
nick = input('IEVADI SAVU IESAUKU:')
while (visi_vardi):                                                                                                 #cikls kurā izspēlē vārdus
    difficulty = input('Izvēlies spēles līmeni, 1 = easy,  2 = medium,  3 = latvietis =], 4 = highscore, 5 = iziet!!!:')         #Spele izvada pieejamos limenus
    start_time = time.time()
    if difficulty == '1':
        difftxt = 'easy'                                                                                          #Parbaude vai speletajs izvelejies pirmo limeni
        print('Tu izvēlējies pirmo spēles limeni "easy"')
        random.shuffle(importetais_vards_easy)
        game.play(importetais_vards_easy_lv_fix.pop())                                                             #
    elif difficulty == '2':
        difftxt = 'medium'                                                                                        #Parbaude vai speletajs izvelejies otro limeni
        print('Tu izvēlējies otro spēles limeni "medium"')  
        random.shuffle(importetais_vards_medium)                                                                   #
        game.play(importetais_vards_medium_lv_fix.pop())                                                           #
    elif difficulty == '3':
        difftxt = 'latvietis'                                                                                        #Parbaude vai speletajs izvelejies Treso limeni
        print('Tu izvēlējies trešo spēles limeni "latvietis =]"')  
        random.shuffle(importetais_vards_hard)                                                                     #
        game.play(importetais_vards_hard_lv_fix.pop())
    elif difficulty == '4':                                                                                       #Parbaude vai speletajs izvelejies iziet no speles
        print ("HIGHSCORES")
        print('===========')
        with open('data\score.txt', 'r', encoding='utf-8') as file_read:
            contents = file_read.read()
            print(contents)  
            break
    elif difficulty == '5':                                                                                       #Parbaude vai speletajs izvelejies iziet no speles
        print ("Tiksimies nākamreiz!")
        break 
    else:
        print('Izvēlies spēles piedāvātos līmeņus')
    end_time = time.time()
    speles_laiks = int(end_time - start_time)
    x = str(speles_laiks)
    print("Spele beigusies, laiks ir" , speles_laiks , 'sekundes')
    with open('data\score.txt', 'a') as file:
        file.write(nick + ' | ' + "Speles laiks " + (str(speles_laiks)) + ' | ' + "Speles limenis " + difftxt + '\n')