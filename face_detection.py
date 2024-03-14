# %%
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret,frame = vid.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
# %%
# We are reading all the image from the vedio
import cv2
import os
video = cv2.VideoCapture('C:\\Users\\Admin\\Data Science\\DL\\Open cv\\Vedio Analysis\\los_angeles.mp4')
try:
    # We are creating a folder from here
    if not os.path.exists('pic data'):
        os.makedirs('pic data')
except OSError:
    print('Error:making directory')
currentframe = 0
while True:
    ret,frame = video.read()
    if ret:
        name = './pic data/from la' + str(currentframe) + '.jpg'
        print('Processing.....'+name)
        cv2.imwrite(name,frame)
        currentframe += 1
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
# %%
import cv2
import os
cam = cv2.VideoCapture('C:\\Users\\Admin\\Data Science\\DL\\Open cv\\Vedio Analysis\\los_angeles.mp4')
try :
    if not os.path.exists('pic data'):
        os.makedirs('pic data')
except OSError:
    print('Error in making directory')

cf = 0
while True:
    ret,frame = cam.read()
    if ret:
        name = './pic data/pics la' + str(cf) +'.jpg'
        print('Processing....',name)
        cv2.imwrite(name,frame)
        cf +=cf + 1
    else:
        break
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
# %%
# Write a text on vedio
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret,frame = vid.read()
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(frame,
                'Heloo Boss',
                (60,60), # Font location in the vedio
                font,
                1, # Font size
                (255,255,255), # Font color
                1, # font thikness
                cv2.LINE_8)
    cv2.imshow('frame',frame)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
# %%
# def main():
#     camera = cv2.VideoCapture(0)
#     output = cv2.VideoWriter('output.mp4',
#                             cv2.VideoWriter_fourcc(*'MPEG'),
#                             30,
#                             (1080*1920))
#     while True:
#         ret,frame = camera.read()
#         if ret:
#             cv2.rectangle(frame,(100,100),(500,500),(0,255,0),3)
#             # writing the new frame in outptu
#             output.write(frame)
#             cv2.imshow('output',frame)
#             if cv2.waitKey(3) & 0xFF == ord('q'):
#                 break
#     cv2.destroyAllWindows()
#     output.release()
#     camera.release()
    
# if __name__ == "__main__":
#     main()
            
# %%
# this below code is only used to built the box is the vedio
import cv2

def main():
    camera = cv2.VideoCapture(0)
    output = cv2.VideoWriter('output.mp4',
                             cv2.VideoWriter_fourcc(*'mp4v'),
                             30,
                             (1080, 1920))  # Corrected dimension tuple
    while True:
        ret, frame = camera.read()
        if ret:
            cv2.rectangle(frame, (100, 100), (50,50), (0, 255, 0), 3)
            # writing the new frame in output
            output.write(frame)
            cv2.imshow('output', frame)
            if cv2.waitKey(3) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()
    output.release()
    camera.release()

if __name__ == "__main__":
    main()
# %%
import cv2

def main():
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    camera = cv2.VideoCapture(0)
    output = cv2.VideoWriter('output.mp4',
                             cv2.VideoWriter_fourcc(*'mp4v'),
                             30,
                             (1080, 1920))
    
    while True:
        ret, frame = camera.read()
        if ret:
            # Convert frame to grayscale for face detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            
            # Writing the new frame to the output video
            output.write(frame)
            
            # Display the frame with detected faces
            cv2.imshow('output', frame)
            
            if cv2.waitKey(3) & 0xFF == ord('q'):
                break
    
    # Release resources
    cv2.destroyAllWindows()
    output.release()
    camera.release()

if __name__ == "__main__":
    main()
# %%
