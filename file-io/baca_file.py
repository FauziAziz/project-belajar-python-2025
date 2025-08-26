import uuid
import time

#time module
second = time.time()
local_time = time.ctime(second)

# Membuat ID unik
unique_id = str(uuid.uuid4())
print(f"ID Unik: {unique_id}")

#format text
size_in_byte = 1024
text = f"id :{unique_id} time :{local_time} epoch : {second} * {size_in_byte}"

# Menampilkan karakter Null (NUL)
null_char = '\x00'
# print(repr(null_char))  # Menampilkan representasi karakter


#buka file 
file_text = open("test.txt", "w")

#tulis isi
file_text.write(text)


#tutup file
file_text.close()
