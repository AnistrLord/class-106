import cv2

fase_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('4f.jpg')

gray  = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = fase_cascade.detectMultiScale(gray)

for(x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color = img[y :y+h,x:x+w]
    
cv2.imshow("Image",img)
cv2.waitKey(0)