import sys
sys.path.append(r"..")

from programs.check_massachusetts_registration import is_valid



def test_punctuations():
  assert is_valid("PI.3.14") == False
  assert is_valid("CS50/") == False
  assert is_valid("Sz?y!!") == False

def test_last_letter():
  assert is_valid("CS50P") == False

def test_correct():
  assert is_valid("CS50") == True
  assert is_valid("szymon") == True
  assert is_valid("szym23") == True

def test_incorrect():
  assert is_valid("CS05") == False
  assert is_valid("CSszymon50") == False
  assert is_valid("CS50P2") == False
  assert is_valid("S") == False
  assert is_valid("0CS50") == False
  assert is_valid("23") == False
