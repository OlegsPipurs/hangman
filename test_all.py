import pytest

from gameplay.game import game

def test_pass():
    assert True 

def test_game_word():
    q = game("Tests")
    assert True

def test_game_life():
    q = game ("6")
    assert True



# def test_Score_attribute_exists():
#     exit = hangman.Exit("word")
#     assert hasattr(hangman.Exit, "word")


# def test_syllables_score():
#     score = Score ("syllables")
#     syll_score =score.syllables_score()
#     assert syll_score == 30

# def test_unique_score():
#     score = Score("unique")
#     uniq_score = score.uniques_score()
#     assert uniq_score == 10
    