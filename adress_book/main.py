from handler import *

"""
    Phone number must begin only : '063', '073', '093', '091', '044', '050', '066', '095', '099', '039', '067', '068', '096', '097', '098'
    Phone number must be consist only 10 numbers
"""
x = '******************************************************************************'

book = AddressBook()

#  1 : test creating Record object
rec_1 = Record("John")
rec_2 = Record("Anna")
print(x)
#  2 : test adding object to the list
test2_1 = rec_1.add_phone('0930001100')
test2_2 = rec_2.add_phone('0449993300')
print(test2_1)
print(test2_2)
print(x)
#  3 : test editing phone number
test3_1 = rec_1.edit_phone('0930001100', '0995553322')
test3_2 = rec_2.edit_phone('0449993300', '0630009900')
print(test3_1)
print(test3_2)
print(x)
#  4 : test finding phone number
test4_1 = rec_1.find_phone("0995553322") # -> Record
test4_2 = rec_1.find_phone("0995556677") # None
print(test4_1)
print(test4_2)
print(x)
#  5 : test removing phone number
test5 = rec_1.remove_phone("0995553322")
print(test5)
print(x)
#  6 : add object to adress book -> Record obj
test6 = book.add_record(rec_2)
print(test6)
rec_3 = Record('Bob')
rec_4 = Record('Jim')
rec_3.add_phone('0632220099')
rec_4.add_phone('0730001122')
test6_3 = book.add_record(rec_3)
test6_4 = book.add_record(rec_4)
print(x)
#  7 : find number in adress book
test7_1 = book.find('Anna')
test7_2 = book.find('Jim')
print(test7_1)
print(test7_2)
print(x)
print('- Before del')
print(book)
print(x)
#  8 : delete contact from adress book
test8_1 = book.delete_record('Anna')
test8_2 = book.delete_record('Bob')
print(test8_1)
print(test8_2)
print(x)
print('- After del')
print(book)