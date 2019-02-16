import face_recognition

image = face_recognition.load_image_file("/home/yang28/Pictures/roombalistic/2120.jpg");

face_locations = face_recognition.face_locations(image)

print("Number of faces: {}".format(len(face_locations)))

for location in face_locations:
	print(location)
	top, right, bottom, left = face_location
	
	# do stuff
