import pytest
from main import count_vowels

# Проверка строк, содержащих только гласные
def test_all_vowels():
   assert count_vowels("aeiou") == 5
   assert count_vowels("AEIOU") == 5
   assert count_vowels("ау") == 2
   assert count_vowels("АУ") == 2

# Проверка строк не содержащих гласные
def test_no_vowels():
   assert count_vowels("bcdfg") == 0
   assert count_vowels("BCDFG") == 0
   assert count_vowels("") == 0
   assert count_vowels("бвгджз") == 0
   assert count_vowels("БВГДЖЗ") == 0

# Проверка смешанных строк
def test_mixed_strings():
   assert count_vowels("Hello World") == 3
   assert count_vowels("PyThOn") == 1
   assert count_vowels("aEiOu") == 5

   assert count_vowels("Аист") == 2
   assert count_vowels("Привет") == 2
   assert count_vowels("бВгД") == 0

   assert count_vowels("Аист Bird") == 3
   assert count_vowels("Привет Hi") == 3
   assert count_vowels("бвгд bvgd") == 0