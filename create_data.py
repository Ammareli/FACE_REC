import cv2
import os
import cvzone

DATA = r"C:\Users\DELL\Documents\Zapya\Video"

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
output_dir = "D:\\Bank FaceRecognization\\data\\images\\"
vedio_dirs = os.listdir(DATA)

# for id,vid in enumerate(vedio_dirs):
#     name = vid.split(".")[0]
#     path = os.path.join(DATA,vid)
#     print(path)

capture = cv2.VideoCapture(0)
counter = 0
    # if not capture.isOpened():
    #     print("Error: Could not open the video file.")
    #     exit()
while True:
    _, frame = capture.read()
    frame = cv2.cvtColor(frame,None ,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(frame,scaleFactor=1.3, minNeighbors=5)
    # resized = cv2.resize(frame,None,fx=0.50,fy=0.50)
    for (x,y,w,h) in faces:
        face_crop = frame[y:y+h, x:x+w]

        
        cv2.imwrite(output_dir + f'face_{"Ammar"}_{"8"}_{counter}.jpg', face_crop)
        counter += 1
        
        bbx = (x ,y ,w ,h)
        cvzone.cornerRect(frame,bbx)


    cv2.imshow("Video",frame)
    if not _:
        break
    if counter > 500:
        break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

