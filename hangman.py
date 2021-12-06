#importē visu nepieciešamo spēles darbībai.

from gameplay.game import game
from scripts_test.split_difficulity import *
from scripts_test.split_difficulity import Difficulty

import time
import requests


#Uzzīmējam spēles logo.

print('\033[0;32;40m'''' ____  __   _____ __________    _________________________   _________    _________''')
print('''|    |/ _| /  _  \\\______   \  /  _  \__    ___/  _  \   \ /   /  _  \  /   _____/''')
print('''|      <  /  /_\  \|       _/ /  /_\  \|    | /  /_\  \   Y   /  /_\  \ \_____  \ ''')
print("""|    |  \/    |    \    |   \/    |    \    |/    |    \     /    |    \/        \\""")
print("""|____|__ \____|__  /____|_  /\____|__  /____|\____|__  /\___/\____|__  /_______  / \033[0;37;40m""")
print('\n')


#Prasa lietotājam ievadīt savu iesauku kas tiks izmantota iekš HIGHSCORES.

nick = input('IEVADI SAVU IESAUKU:')


#While cikls kur lietotajs izvēlas grūtības pakapi, 
#spēles rezultātus vai vēlas beigt spēli.
                
while True:
    try:
        while (Difficulty.read_words):
            difficulty = input('\033[0;32;40mIzvēlies spēles līmeni: ' 
            + '\033[0;37;40m \n1 = Easy ' 
            + '\n2 = Medium ' 
            + '\n3 = Latvietis =] ' 
            + '\n4 = Angļu vārdi no API ' 
            + '\n5 = Highscore ' 
            + '\n6 = Quit \n'
            )
            start_time = time.time()


            #Pirmais grūtības pakāpes līmenis, atbilsoši līmenim 
            # paņem no faila 'split_difficulity.py' definetos vardus un 
            # izsauc speles klasi Game.

            if difficulty == '1':
                difftxt = 'easy'                                                                                         
                print('Tu izvēlējies pirmo spēles limeni "Easy"')
                difi = Difficulty()
                difi.easy()
                game.play(difi.importetais_vards_easy_lv_fix.pop())
            

            #Otrais grūtības līmenis.
            
            elif difficulty == '2':
                difftxt = 'medium' 
                print('Tu izvēlējies otro spēles limeni "Medium"')  
                dif = Difficulty()
                dif.medium()                                                                   
                game.play(dif.importetais_vards_medium_lv_fix.pop())                                                           
            

            #Trešais grūtības līmenis.
            
            elif difficulty == '3':
                difftxt = 'latvietis'
                print('Tu izvēlējies trešo spēles limeni "Latvietis =]"')  
                difo = Difficulty()
                difo.hard()       
                game.play(difo.importetais_vards_hard_lv_fix.pop())
                
                
            #API grūtības pakāpe
            
            elif difficulty == '4':
                
                print("Vārda izvēle no randomword api")
                url = 'https://random-word-api.herokuapp.com/word?number=1'
                response = requests.get(url)
                difftxt = 'API'
                fix_api_word = (str(response.json())[2:-2])
                game.play(fix_api_word)      
            
            
            #HIGHSCORE izvēle.

            elif difficulty == '5':
                class Score:
                    def __init__(self):
                        self.score = "HIGHSCORES"
                        self.lines = "=========="
                        with open('data\score.txt', 'r', encoding='utf-8') as file_read:
                            self.contents = file_read.read()     
                x_score = Score()
                print(x_score.lines)
                print(x_score.score)
                print(x_score.lines)
                print(x_score.contents)
                break
    
    
            #Aizver spēli ar atvadu paziņojumu.

            elif difficulty == '6':
                class Exit:
                    def __init__(self, x):
                        self.x = "word"
                        self.good_by_msg = "Tiksimies nākamreiz"
                x_exit = Exit()
                print(x_exit.good_by_msg)
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
                file.write(nick 
                + ' | ' 
                + "Speles laiks " 
                + (str(speles_laiks)) 
                + ' | ' 
                + "Speles limenis " 
                + difftxt + '\n'
                )
    
    
    #Dažādu kļūdu apstrāde.

    except IndexError:
        print('Izvēletajā failā spēles līmenī nav minēto vārdu')
    except NameError:
        print('Iztrukst fails words.txt')
        input('Nospied ENTER pogu lai izietu...')
    break