# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024

pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

total_chars = pages * lines_per_page * chars_per_line
book_size = total_chars * bytes_per_char

books_on_disk = int(disk_size // book_size)

print("Количество книг, помещающихся на дискету:", books_on_disk)