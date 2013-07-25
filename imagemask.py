##########
# Image Mask Tool v0.3
# copyright 2013, Modular Programming Systems Inc
# released as GPL3
#
##########

import Image
import sys

def check_file_type(old_file):
    img=Image.open(old_file)
    if img.format!="PNG":
        print "Incorrect File Format"
        raise SystemExit
        
    
def create_mask(old_file,new_file):
    mask=[]
    img=Image.open(old_file)
    for item in list(img.getdata()):
        r,g,b,a=item
        if a==0:        #fully transparent
            r=g=b=255
        elif a==255:    #fully visible, 0% transparent
            r=g=b=0
        else:           #create Grey pixels based on partial transparency   
            r=g=b=a
        a=255
        mask.append((r,g,b,a))
    img.putdata(mask)
    img.save(new_file,"PNG")


if __name__=="__main__":
    try:
        old_file=sys.argv[1]
        new_file=sys.argv[2]
    except:
        print "python imagemask.py (old-image) (new-image)\n\n"
        raise SystemExit
    
    check_file_type(old_file)
    create_mask(old_file,new_file)
