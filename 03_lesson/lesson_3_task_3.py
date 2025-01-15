from address import Address
from mailing import Mailing

to_address = Address(123456, 'Москва', 'Южная', 12, 70)
from_address = Address(125636, 'Белгород', 'Клубничная', 45, 43)

mailing = Mailing(to_address, from_address, 5000, 'CD123456789JH')

print(mailing)
