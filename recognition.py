import face_recognition

image = face_recognition.load_image("./frame.jpg");

face_locations = face_recognition(image)

print("Number of faces: ".format(len(face_locations)))

for location in face_locations
	# do stuff
