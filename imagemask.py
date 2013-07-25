import Image
import sys

def create_mask(old_file,new_file):
    mask=[]
    img=Image.open(old_file)
    for item in list(img.getdata()):
        r,g,b,a=item
        if a!=255:  #partially or fully transparent
            r=g=b=255
        if a==255:  #fully visible, 0% transparent
            r=g=b=0
        a=255
        mask.append((r,g,b,a))
    img.putdata(mask)
    img.save(new_file,"PNG")


if __name__=="__main__":
    try:
        old_file=sys.argv[1]
        new_file=sys.argv[2]
    except:
        print "python imagemask.py (old-image) (new-image)"
    create_mask(old_file,new_file)
