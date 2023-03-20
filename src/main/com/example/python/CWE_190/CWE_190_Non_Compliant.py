def intezer_overflow():
    string1 = 'AB' * 100
    print(string1)


intezer_overflow()

#   If we were to try to create a string with an extremely large number of characters,
#   we could run out of memory and cause an overflow.