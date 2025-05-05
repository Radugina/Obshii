from smartphone import Smartphone

catalog = [
Smartphone ("Apple", "Series 15", "+79161111111"),
Smartphone ("Samsung", "Galaxy A35",  "+79162222222"),
Smartphone ("Huawei", "Nova 12 SE",  "+79163333333"),
Smartphone ("LG", "G4", "+79164444444"),
Smartphone ("Honor", "X8b", "+79165555555")
]

for smartphone in catalog:
     print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}.")