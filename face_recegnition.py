import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces
e
    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

    def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding