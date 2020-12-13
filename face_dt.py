import cv2,glob

gimg=glob.glob("*.jpg")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for gim in gimg:
    img=cv2.imread(gim)
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gimg,scaleFactor=1.25,minNeighbors=5)

    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Face Detection",img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()