import sys
sys.path.append(r"..")
from programs.living_time import to_words
from programs.living_time import ChanngingSec

def test_to_words_check():
    assert to_words(0) == "Zero"
    assert to_words(5) == "Five"
    assert to_words(29) == "Twenty-nine"
    assert to_words(164) == "One hundred sixty-four"
    assert to_words(1764) == "One thousand, seven hundred sixty-four"
    assert to_words(2012) == "Two thousand twelve"
    assert to_words(17465) == "Seventeen thousand, four hundred sixty-five"
    assert to_words(23456789876) == "Twenty-three billion, four hundred fifty-six million, seven hundred eighty-nine thousand, eight hundred seventy-six"

def test_cls_prompt():
    assert ChanngingSec.prompt("1999-05-23") == (1999, 5, 23)
    assert ChanngingSec.prompt("1869-12-09") == (1869, 12, 9)
    assert ChanngingSec.prompt("2009-12-12") == (2009, 12, 12)
    assert ChanngingSec.prompt("2012-01-09") == (2012, 1, 9)
