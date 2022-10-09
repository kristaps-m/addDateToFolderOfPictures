# Code to apply operations on all the images 
# present in a folder one by one 
# operations such as rotating, cropping, 
from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import PIL
import datetime,time
import os,os.path

def the_human_create_date(img_name):
    s = time.ctime(os.path.getctime(img_name))
    s=datetime.datetime.strptime(s, '%a %b %d %H:%M:%S %Y')
    s=s.strftime("%d.%m.%y")
    # ~ print("created : %s" % s)
    # ~ print(s);
    return s;



def addDateToOneImage(img, imgname,image_opened):
    #---------------------------------
    #https://stackoverflow.com/questions/23064549/get-date-and-time-when-photo-was-taken-from-exif-data-using-pil
    exif = img.getexif()
    creation_time = exif.get(36867)
    
    try:
        s=datetime.datetime.strptime(creation_time, '%Y:%m:%d %H:%M:%S')
        s=s.strftime("%d.%m.%y") # The end text
    except:
        # yyyy.mm.dd        
        if "IMG" in imgname and "WA" in imgname:
            d,m,y = imgname[10:12],imgname[8:10],imgname[6:8]
            s = d+"."+m+"."+y
        else:
            # if IMG-20201207-WA0011.jpg #This is What'sApp picture
            s = the_human_create_date(image_opened)
        # ~ s = "" # Nothing on pict
        
    #---------------------------------
    # https://stackoverflow.com/questions/18869365/a-watermark-inside-a-rectangle-which-filled-the-certain-color
    draw = ImageDraw.Draw(img)
    PW, PH = img.size # picture width, picture heigt
    font = ImageFont.truetype('courbi.ttf', PW//20) # 160 = for w3500 x h4.5k pic ## //20
    """x & y starts from top left corner
    where you want to date to start"""
    x, y = (PW//35, PH//35) # 50,50
    """botom left"""
    #x, y = (PW//35, PH-(PH//35*3))
    # x, y = 10, 10
    text = s # "copyright"
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill='black')
    draw.text((x, y), text, fill=(250, 250, 250), font=font)
    return img;



# https://www.geeksforgeeks.org/apply-changes-to-all-the-images-in-given-folder-using-python-pil/
def main(): 
    # path of the folder containing the raw images 
    """When testing"""
    #inPath ="C:\\Users\\Kristaps\\Desktop\\Python solutions\\Img edit\\intest"
    inPath ="C:\\Users\\Kristaps\\Desktop\\ATIISTIIT\\01.01.21-10.05.22"
    # ~ inPath = r"C:\Users\Kristaps\Desktop\Python solutions\Img edit\move_im_TO" 
    
    """when testing out path"""
    # path of the folder that will contain the modified image 
    #outPath ="C:\\Users\\Kristaps\\Desktop\\Python solutions\\Img edit\\out_test"
    outPath ="C:\\Users\\Kristaps\\Desktop\\ATIISTIIT\\2022 ar datumiem"

    for imagePath in os.listdir(inPath): 
        # imagePath contains name of the image 
        inputPath = os.path.join(inPath, imagePath) 

        # inputPath contains the full directory name 
        img = Image.open(inputPath) 

        fullOutPath = os.path.join(outPath, 'date_'+imagePath) 
        # fullOutPath contains the path of the output 
        # image that needs to be generated 
        # ~ img.rotate(90).save(fullOutPath) 
        addDateToOneImage(img,imagePath,inputPath).save(fullOutPath)

        print(fullOutPath) 

# Driver Function 
if __name__ == '__main__': 
	main() 

print("Done!")
