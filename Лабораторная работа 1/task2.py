# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages = 100
page_str = 50
str_sym = 25
sym_byte = 4
MBITE_BYTE = 1024 ** 2
disk_size_byte = disk_size * MBITE_BYTE
book_size = pages * page_str * str_sym * sym_byte
amount = disk_size_byte // book_size
print("Количество книг, помещающихся на дискету:", int(amount))
