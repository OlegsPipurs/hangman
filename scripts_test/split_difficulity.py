import random

with open('data\words.txt', 'r', encoding='utf-8') as file:     # Atver vārdu failu
    visi_vardi = file.read().splitlines()                       # Uzjautāt kas tur ar \r\n ?workaround? wordtokenize? readlines() nedarbojas
    list(visi_vardi)                                            # Konvertē uz list
    random.shuffle(visi_vardi)                                  # Samaisa sarakstu
    
    importetais_vards_easy = [x for x in visi_vardi if len(x) <= 6]     # Parbauda vārda garumu
    importetais_vards_easy_lv_fix = [ x for x in importetais_vards_easy if "Ā" not in x and "Č" not in x and "Ē" not in x and "Ģ" not in x and "Ī" not in x and "Ķ" not in x and "Ļ" not in x and "Ņ" not in x and "Š" not in x and "Ū" not in x and "Ž" not in x]
    with open('data\easy_words.txt', 'w') as file_handler:
        for item in importetais_vards_easy_lv_fix:
            file_handler.write("{}\n".format(item))            

    importetais_vards_medium = [x for x in visi_vardi if len(x)>=7 and len(x)<=25]  # Parbauda vārda garumu
    importetais_vards_medium_lv_fix = [ x for x in importetais_vards_medium if "Ā" not in x and "Č" not in x and "Ē" not in x and "Ģ" not in x and "Ī" not in x and "Ķ" not in x and "Ļ" not in x and "Ņ" not in x and "Š" not in x and "Ū" not in x and "Ž" not in x]
    with open('data\medium_words.txt', 'w') as file_handler:
        for item in importetais_vards_medium_lv_fix:
            file_handler.write("{}\n".format(item))

    importetais_vards_hard = [x for x in visi_vardi if len(x) >= 4]      # Parbauda vārda garumu
    importetais_vards_hard_lv_fix = [ x for x in importetais_vards_hard if "Ā" in x or "Č" in x or "Ē" in x or "Ģ" in x or "Ī" in x or "Ķ" in x or "Ļ" in x or "Ņ" in x or "Š" in x or "Ū" in x or "Ž" in x]
    #list(importetais_vards_hard_lv_fix)
    with open('data\hard_words.txt', 'w') as file_handler:
        for item in importetais_vards_hard_lv_fix:
            file_handler.write("{}\n".format(item))    
