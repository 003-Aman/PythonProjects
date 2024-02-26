"""
pip install qrcode Image (in the terminal)
Install all the libraries needed
Create a function that collects a text and converts it to a quote
Save the QRcode as an image
Run the function
"""
import qrcode #qrcode module is obviously used to generate QRcodes

def generate_qrcode(text): #created a fuction which takes parameter text(text represents the content that will be encoded into the qr code)

    qr = qrcode.QRCode(#initializes a 'QRCode' object using the 'qrcode' module.
        #'qrcode.QRCode': This part of the line accesses the QRCode class from the qrcode module.
        #The 'QRCode' class is responsible for creating and manipulating QR codes.

        
        version =1,#version of the qr code(1-40, indicating lower to lager codes)
        error_correction = qrcode.constants.ERROR_CORRECT_L,#error correction level(_L for low,_M for medium,_Q for high,_H for highest)
        box_size =10, # the size of each box in the qr code
        border =4, # the thickness around the border
    )

    qr.add_data(text)#method used to input text to the qr code
    qr.make(fit = True) #makes the qr code, automatically adjusting the size to fit the content
    img =qr.make_image(fill_color = "black",back_color="white") #elle chai creates image representation of the qr code with specifies fill and background colors
    img.save("qrimg.png")# final image is saved as a Png file named "qrming.png" using the save() method

url = input("Enter your URL: ")
generate_qrcode(url)    


    



