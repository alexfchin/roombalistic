from PIL import Image
import face_recognition
import os

known_image_folder = "./Photos/Known/"
unknown_image = "./Photos/2120.jpg"

directory = os.fsencode(known_image_folder)
known_images = [face_recognition.load_image_file(file)
        for file in os.listdir(directory)]

try:
    unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
    known_image_encodings = [face_recognition.face_encodings(image)[0]
            for image in known_images]
except IndexError:
    print("Could not detect any faces in at least one of the known images.")
    quit()

results = face_recognition.compare(known_image_encodings, unknown_image_encoding)

for result in results
    print(result)
