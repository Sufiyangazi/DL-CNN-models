# %%
import cv2
import matplotlib.pyplot as plt
# %%
img = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\3bb76543b9b5865f6aae5d25a81bb471.jpg',
                 cv2.COLOR_BGR2GRAY)
strat_window =(5,5)
end_window = (200,200)
color = (255,0,255)
thikness =5
rec_image = cv2.rectangle(img,
                          strat_window,
                          end_window,
                          color,
                          thikness)
cv2.imshow('image',rec_image)
cv2.waitKey()

# %%
import cv2
img = cv2.imread('C:\\Users\\Admin\\OneDrive\\Pictures\\3bb76543b9b5865f6aae5d25a81bb471.jpg')
face_cascade = cv2.CascadeClassifier('haarcascade_frontal1face_default.xml')
faces = face_cascade.detectMultiScale(img,1.1,4)
print(faces)
for (x,y,w,h) in faces :
    print(x,y)
    print(w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while cap.is0opend():
    has_frame,frame = cap.read()
    imag = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imag,1.1,4)
    for (x,y,w,h) in faces :
        cv2.rectangle(imag,(x,y),(x+h,y+w),(255,0,0),3)
        
        
        cv2.imshow('image')
        
# %%
import cv2
cap = cv2.VideoCapture(0)
while True:
    has_frame,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        
        
# %%
