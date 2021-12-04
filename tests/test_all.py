import pytest
from hangman import Exit

def test_Score_attribute_exists():
    exit = Exit("word")
    assert hasattr(Exit, "word")

"""
def test_syllables_score():
    score = Score ("syllables")
    syll_score =score.syllables_score()
    assert syll_score == 30

def test_unique_score():
    score = Score("unique")
    uniq_score = score.uniques_score()
    assert uniq_score == 10
    """