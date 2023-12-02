from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
import os.path

# calls directory location
directory = input("enter directory: ")
keyWord = input("enter key word: ")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#iterates through files
for fileName in os.listdir(directory):
    try:
        fileName = directory + "\\" + fileName
        if fileName.endswith(".pdf"):
            # Store Pdf with convert_from_path function
            images = convert_from_path(fileName)
            
            # Save pages as images in the pdf
            images[0].save(fileName + "image" +'.jpg', 'JPEG')
            
            image = Image.open((fileName + "image" +'.jpg'))
            
            #puts text into a string named text
            text = pytesseract.image_to_string(image)
            if keyWord in text:
                num = text.find(keyWord) + 15
                name  = text[num: text.find(' ', num)]
                name = name[0:10]
                file = directory + "\\" + name
                if not os.path.isdir(file):
                   os.makedirs(file)
                print("found: " + name)
                count = 1
                if os.path.isfile(file + "\\" + name + ".pdf"):
                    name = name + "-" + str(count)
                    while os.path.isfile(file + "\\" + name + ".pdf"):
                        count+= 1
                        name = name[0:11] + str(count)
                os.rename(fileName, (file + "\\" + name + ".pdf"))
                os.remove(fileName + "image" +'.jpg')
            else:
               print("not found")
    except PermissionError:
        print(fileName + " is open")
        pass
print("done!")