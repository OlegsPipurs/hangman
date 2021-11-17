# **Laipni lūgti vārdu minēšanas spēlē "Karātavas"!**

## Spēles prasības:

###### Minēšanas spēlē "Karātavas" var tikt spēlēta no komandlīnijas (CommandPrompt)

## Spēlei nepieciešamie faili:

    - Data\words.txt
    - gameplay\game.py
    - scripts_test\split_difficulity.py
    - hangman.py
    - requirements.py

## Spēles gaita:

###### Ievadiet savu iesauku.
###### Izvēlaties spēles grūtības pakāpi vai citu funkciju:

    1: easy grūtības pakāpe,
    2: medium grūtības pakāpe,
    3: latvietis grūtības pakāpe,
    4: aplūkot HIGHSCORES,
    5: iziet no spēles.

###### Jums tiek dotas sešas dzīvības.
###### Sāciet minēt vārdu ievadot vai nu burtu vai visu vārdu atbilstoši vārda garuma paziņojumam.
###### Nekorekti minētu burtu / vārdu gadijumā tiks zīmēta karātava, par katru nekorektu minējumu tiek atņemta dzīvība.           Spēle turpinās līdz beigsies dzīvības un tā tiks pārtraukta.
###### Atminētu burtu gadijumā tiks atklāts vārds pa vienam burtam līdz uzminēsiet visu vārdu
###### Beidzoties spēles partijai atkārtoti izvēlamies spēles grūtības pakāpi vai papildus funkciju.
###### !Spēlē ir pieejams papildus bonus, ievadiet minētā vārda vietā: FITA

## Vārdnīcas vārda formāts

###### Data\words.txt
###### Fails satur minamos vārdus, kas tiek atdalīti ar ( \r\n ).
###### Piemers:
```
BALTISMS
AMBROZIJA
IESALDĒŠANA
LAUKAUGS
BAGIJS  
```