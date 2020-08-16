import cv2
import numpy as np
from pyzbar.pyzbar import decode
#img=cv2.imread("qrexpic.png")
#code=decode(img)
cap=cv2.VideoCapture(0)
cap.set(3,700)
cap.set(4,500)
with open('qrlist.txt') as f:
    mydl=f.read().splitlines()
print(mydl)
while(1):
    s,img=cap.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        if((mydata) in mydl):
            op='Authorized'
            myc=(0,255,0)
        else:
            op='unAuthorized'
            myc=(0,0,255)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myc,5)
        pts2=barcode.rect
        cv2.putText(img,op,(pts2[0],pts2[1]),cv2.FONT_ITALIC,0.9,myc,2)
    cv2.imshow('result',img)
    if(cv2.waitKey(20) & 0xFF==ord("q")):
        break
       
cv2.destroyAllWindows()
