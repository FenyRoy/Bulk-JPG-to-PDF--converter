import os
import img2pdf
for i in os.listdir('.'):
    if i.endswith(".jpg"):
        name=i.replace(".jpg","")+".pdf"
        with open(name,"wb") as f:
            f.write(img2pdf.convert(i))
