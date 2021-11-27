#Importē iebūvēto Random bibliotēku

import random


    #Tiek veiktas darbibas ar "words.txt"

with open('data\words.txt', 'r', encoding='utf-8') as file:
    visi_vardi = file.read().splitlines()
    list(visi_vardi)
    random.shuffle(visi_vardi)
    

    #Atlasa easy vārdus pēc konkrētiem kritērijiem
        
    importetais_vards_easy = [
        x for x in visi_vardi if
        len(x) <= 6
        ]
    importetais_vards_easy_lv_fix = [
        x for x in importetais_vards_easy if
        "Ā" not in x and 
        "Č" not in x and 
        "Ē" not in x and 
        "Ģ" not in x and 
        "Ī" not in x and 
        "Ķ" not in x and 
        "Ļ" not in x and 
        "Ņ" not in x and 
        "Š" not in x and 
        "Ū" not in x and 
        "Ž" not in x
        ]
    
    with open('data\easy_words.txt', 'w') as file_handler:
        for item in importetais_vards_easy_lv_fix:
            file_handler.write("{}\n".format(item))          
    
        
    #Atlasa medium vārdus pēc konkrētiem kritērijiem

    importetais_vards_medium = [
        x for x in visi_vardi if
         len(x) >= 7 
         and
         len(x) <= 25
         ]
    importetais_vards_medium_lv_fix = [
        x for x in importetais_vards_medium if
        "Ā" not in x and 
        "Č" not in x and 
        "Ē" not in x and 
        "Ģ" not in x and 
        "Ī" not in x and 
        "Ķ" not in x and 
        "Ļ" not in x and 
        "Ņ" not in x and 
        "Š" not in x and 
        "Ū" not in x and 
        "Ž" not in x
        ]
    
    with open('data\medium_words.txt', 'w') as file_handler:
        for item in importetais_vards_medium_lv_fix:
            file_handler.write("{}\n".format(item))
    

    #Atlasa hard vārdus pēc konkrētiem kritērijiem
    
    importetais_vards_hard = [
        x for x in visi_vardi if
         len(x) >= 4
         ]
    importetais_vards_hard_lv_fix = [
        x for x in importetais_vards_hard if
        "Ā" in x or
        "Č" in x or
        "Ē" in x or
        "Ģ" in x or
        "Ī" in x or
        "Ķ" in x or
        "Ļ" in x or
        "Ņ" in x or
        "Š" in x or
        "Ū" in x or
        "Ž" in x
        ]
    with open('data\hard_words.txt', 'w') as file_handler:
        for item in importetais_vards_hard_lv_fix:
            file_handler.write("{}\n".format(item))  

  