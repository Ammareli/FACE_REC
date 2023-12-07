import cv2
import pickle
import os
import cvzone


from CONSTANTS import EMPLOYESS, EMPLOYESS_IMAGES,DEFAULT_PATH_IMAGE

def face_rec(ID):
    ID = int(ID)
    image_path = DEFAULT_PATH_IMAGE
    name = EMPLOYESS[ID][0]
    des = EMPLOYESS[ID][1]
    time = "time"
    status = "True"
    for i in os.listdir(EMPLOYESS_IMAGES):
        image_name_id = i.split(".")[0]
        # name = image_name_id.split("_")[0]
        id = image_name_id.split("_")[1]
        # print(id)
        if int(ID) == int(id):
            image_path = os.path.join(EMPLOYESS_IMAGES,i)
    return [name, des, image_path,time,status]


def cheak(num):
    pass
    
# print(EMPLOYESS[0][1])

# print(face_rec(8))