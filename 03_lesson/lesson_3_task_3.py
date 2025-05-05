from address import Address
from mailing import Mailing

to_address = Address ("141260", "Пушкино", "Тургенева", "12", "2")
from_address = Address ("141000", "Москва", "Мира", "334", "67")

mailing = Mailing (to_address, from_address, 604, "TR345678")

print(mailing)