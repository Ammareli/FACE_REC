import cv2
import tensorflow as tf
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input
import keras.backend as K
import numpy as np
import cvzone
from threading import Thread
from queue import Queue

global NAME
global CONF
NAME = ""
CONF = ""


person_rep = {
                0: 'Aftab',
                1: 'Ammar',
                2: 'Atiqa',
                3: 'Gulam',
                4: 'Ibrahim',
                5: 'makdoom',
                6: 'Maria',
                7: 'Mohsin',
                8: 'shahzad'}

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


class FaceRecognition:
    def __init__(self,classifier_model_path, input_queue, output_queue):

        self.classifier_model = tf.keras.models.load_model(classifier_model_path)


        self.input_queue = input_queue
        self.output_queue = output_queue

        self.stopped = False

    def start(self):
        Thread(target=self.recognize_faces, args=()).start()
        return self

    def stop_recognition(self):
        self.stopped = True



    def recognize_faces(self):
        while not self.stopped:
            if not self.input_queue.empty():
                frame = self.input_queue.get()

                # Preprocess the input image
                input_im = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_LINEAR)
                input_im = input_im / 255.
                input_im = input_im.reshape(1,224,224,3) 

                # Get Prediction
                res = self.classifier_model.predict(input_im, 1, verbose = 0)

                # Put results in the output queue
                self.output_queue.put(res)

input_queue = Queue()
output_queue = Queue()

classifier_model_path = r'data\Model\face_classifier.h5'
face_recognition = FaceRecognition(classifier_model_path, input_queue, output_queue).start()

capture = cv2.VideoCapture(0)
while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)
    
    for (x, y, w, h) in faces:
        bbx = (x, y, w, h)
        face_crop = frame[y:y+h, x:x+w]
        
        
        input_queue.put(face_crop)
        if not output_queue.empty():

                classifier_output = output_queue.get()
                # print(len(output_queue.queue))
                # print(classifier_output)
                NAME = person_rep[np.argmax(classifier_output)]
                CONF = str(np.max(classifier_output))
                print(NAME)
        cvzone.cornerRect(frame,bbx)
        # if float(CONF) >= 0.95:
        #     print("True")
            
        cvzone.putTextRect(frame,NAME,(x-10,y),1,1)
        cvzone.putTextRect(frame,CONF,((x+w)-30,y),1,1)
        # if NAME != 
        # NAME = ""
        # CONF = ""
        
    cv2.imshow("rec",frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        face_recognition.stop_recognition()
        capture.release()
        break

cv2.destroyAllWindows()