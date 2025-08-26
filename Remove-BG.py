# Importing Required Modules 
from rembg import remove 
from PIL import Image 

#this my style
print("Remove Background By Fauzi_Aziz")
  
# masukin bang !!!
masuk_path =  'export.png' 
  
# Keluar jir !!
keluar_path = 'hasil.png' 
  
# BRO SEDANG MEMASAK
input = Image.open(masuk_path) 
  
# Remove Backgroundnya
output = remove(input) 
  
#Cr*t !!
output.save(keluar_path) 