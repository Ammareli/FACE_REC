from attendace import load_pickle,encoder,load_images


person_id,img_list = load_images("DEMO\photos")




encoder(image_list=img_list,ids=person_id,path_save=r"D:\Bank FaceRecognization\encodings")

# encoding_of_known_faces,ids = load_pickle(path_of_encodeing=r"encodings\ImageEncodeings.p",path_of_ids=r"D:\Bank FaceRecognization\encodings\IDs.p")

# print(encoding_of_known_faces,ids)