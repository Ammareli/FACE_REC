import cv2
import os
import numpy as np

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    counter = 0
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        Image = cv2.imread(imagePath,0)
        img = cv2.resize(Image, (100,100), interpolation=cv2.INTER_CUBIC)
        # Now we are converting the PIL image into numpy array
        # imageNp = np.array(Image, 'uint8')
        # getting the Id from the image
        Id = int(imagePath.split("_")[2])
        # grey = cv2.cvtColor(Image,None,cv2.COLOR_BGR2GRAY)

        # extract the face from the training image sample
        


        faceSamples.append(img)
        Ids.append(Id)
        counter += 1

    print(counter)

    return np.array(faceSamples), np.array(Ids)




def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
  
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("D:\Bank FaceRecognization\data\images")
    except Exception as e:
        print('please make "dataset" folder & put Images', e)

    print("Training Model")
    recognizer.train(faces,Id) 
    try:
        print("Saveing Model")
        recognizer.save(r"data\Model\trained_model2.yml")
    except Exception as e:
        q='Please make "model" folder'


    print("model_trained")


training()
# images, labels  = getImagesAndLabels("D:\Bank FaceRecognization\data\images")
# print(images, labels)

