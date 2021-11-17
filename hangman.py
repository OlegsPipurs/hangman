#importē visu nepieciešamo spēles darbībai.

from gameplay.game import game
from scripts_test.split_difficulity import *

import random
import time
import shelve


#Uzzīmējam spēles logo.

print('\033[0;32;40m'''' ____  __   _____ __________    _________________________   _________    _________''')
print('''|    |/ _| /  _  \\\______   \  /  _  \__    ___/  _  \   \ /   /  _  \  /   _____/''')
print('''|      <  /  /_\  \|       _/ /  /_\  \|    | /  /_\  \   Y   /  /_\  \ \_____  \ ''')
print("""|    |  \/    |    \    |   \/    |    \    |/    |    \     /    |    \/        \\""")
print("""|____|__ \____|__  /____|_  /\____|__  /____|\____|__  /\___/\____|__  /_______  / \033[0;37;40m""")
print('\n')


#Prasa lietotājam ievadīt savu iesauku kas tiks izmantota iekš HIGHSCORES.

nick = input('IEVADI SAVU IESAUKU:')


#While cikls kur lietotajs izvēlas grūtības pakapi, spēles rezultātus vai vēlas beigt spēli.

while True:
    try:
        while (visi_vardi):
            difficulty = input('Izvēlies spēles līmeni, 1 = easy,  2 = medium,  3 = latvietis =], 4 = highscore, 5 = iziet!!!:')
            start_time = time.time()


            #Pirmais grūtības pakāpes līmenis, atbilsoši līmenim paņem no faila 'split_difficulity.py' definetos vardus un izsauc speles klasi Game.

            if difficulty == '1':
                difftxt = 'easy'                                                                                         
                print('Tu izvēlējies pirmo spēles limeni "easy"')
                random.shuffle(importetais_vards_easy)
                game.play(importetais_vards_easy_lv_fix.pop())
            

            #Otrais grūtības līmenis.
            
            elif difficulty == '2':
                difftxt = 'medium' 
                print('Tu izvēlējies otro spēles limeni "medium"')  
                random.shuffle(importetais_vards_medium)                                                                   
                game.play(importetais_vards_medium_lv_fix.pop())                                                           
            

            #Trešais grūtības līmenis.
            
            elif difficulty == '3':
                difftxt = 'latvietis'
                print('Tu izvēlējies trešo spēles limeni "latvietis =]"')  
                random.shuffle(importetais_vards_hard)
                game.play(importetais_vards_hard_lv_fix.pop())
                
            
            #HIGHSCORE izvēle.
            
            elif difficulty == '4':
                print ("HIGHSCORES")
                print('===========')
                with open('data\score.txt', 'r', encoding='utf-8') as file_read:
                    contents = file_read.read()
                    print(contents)  
                    break
            
            
            #Aizver spēli ar atvadu paziņojumu.
            
            elif difficulty == '5':
                print ("Tiksimies nākamreiz!")
                break
            
            
            #Gadijumā ja izvēlējies nekorekti izvada brīdinājumu.
            
            else:
                print('Izvēlies spēles piedāvātos līmeņus')
            
            
            #Aprēķina spēles laiku un saglabā failā.
            
            end_time = time.time()
            speles_laiks = int(end_time - start_time)
            x = str(speles_laiks)
            print("Spele beigusies, laiks ir" , speles_laiks , 'sekundes')
            with open('data\score.txt', 'a') as file:
                file.write(nick + ' | ' + "Speles laiks " + (str(speles_laiks)) + ' | ' + "Speles limenis " + difftxt + '\n')
    
    
    #Dažādu kļūdu apstrāde.

    except IndexError:
        print('Izvēletajā failā spēles līmenī nav minēto vārdu')
    except NameError:
        print('Iztrukst fails words.txt')
        input('Nospied ENTER pogu lai izietu...')
    break