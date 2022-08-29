import barcode
from barcode.writer import ImageWriter

#Define content of the barcode as a string
number = input("Enter the code to generate barcode :")

#get required baarcode formate
barcode_formate = barcode.get_barcode_class('upc')

#generate barcode and render as image
my_barcode = barcode_formate(number,writer=ImageWriter())

#save as png
my_barcode.save('generated_barcode')

#open and show barcode
from PIL import Image
Image.open('generated_barcode.png')
