from gameplay.game import game  
from scripts_test.split_difficulity import *

import random
while (visi_vardi):                                           #cikls kurā izspēlē vārdus
    difficulty = input('Izvēlies spēles līmeni, 1 = easy,  2 = medium,  3 = latvietis =], 4 = iziet!!! :')         #Spele izvada pieejamos limenus
    if difficulty == '1':                                                                                          #Parbaude vai speletajs izvelejies pirmo limeni
        print('Tu izvēlējies pirmo spēles limeni "easy"')
        random.shuffle(importetais_vards_easy)
        game.play(importetais_vards_easy_lv_fix.pop())                                                             #
    elif difficulty == '2':                                                                                        #Parbaude vai speletajs izvelejies otro limeni
        print('Tu izvēlējies otro spēles limeni "medium"')  
        random.shuffle(importetais_vards_medium)                                                                   #
        game.play(importetais_vards_medium_lv_fix.pop())                                                           #
    elif difficulty == '3':                                                                                        #Parbaude vai speletajs izvelejies Treso limeni
        print('Tu izvēlējies trešo spēles limeni "latvietis =]"')  
        random.shuffle(importetais_vards_hard)                                                                     #
        game.play(importetais_vards_hard_lv_fix.pop())
    elif difficulty == '4':                                                                                        #Parbaude vai speletajs izvelejies iziet no speles
        print ("Tiksimies nākamreiz!")
        break 
    else:
        print('Izvēlies spēles piedāvātos līmeņus')