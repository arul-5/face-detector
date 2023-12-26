import cv2
import os
from PIL import Image
def has_human_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return len(faces) > 0
yes_destination = r'C:\Users\arulk\OneDrive\Desktop\Face detection\yes face'
no_destination = r"C:\Users\arulk\OneDrive\Desktop\Face detection\no face"
for i in range(476):
    path = r'C:\Users\arulk\OneDrive\Desktop\Face detection\chapri\chapri{}.jpeg'.format(i)
    result = has_human_face(path)
    if result == True:
        with Image.open(path) as img:
            final_path  =os.path.join(yes_destination, os.path.basename(path))
            img.save(final_path)
    else:
        with Image.open(path) as img:
            final_path  =os.path.join(no_destination, os.path.basename(path))
            img.save(final_path)

