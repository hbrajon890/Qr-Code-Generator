import qrcode        #make(data)==>qrcode, save (file name) ==>file save korbve

# text = input("Enter the text to convert in the qr code:") 
# filename = input("Enter the filename to save the qr code:")
#  test


def generate_qr_code(filepath):

    with open(filepath,'r') as file:
        lines = file.readlines()   #line by line ...1st ,2nd amn vabe

    text = lines[0].strip()     #strip age piser space remove kore    
    filename = lines[1].strip() 


    #make qrcode  make method iya korbo
    image_qrcode = qrcode.make(text)


    #save ther image
    image_qrcode.save(filename)



generate_qr_code('input.txt')   #file kaj na korle ...copy relatate path nilew hobe but forwar slas kore nite hobe

