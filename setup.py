import os
import os.path

import file_transfer
import vision
import recognition

if __name__ == "__main__":
	# Connect to raspberry pi ftp server and get latest frame
	ftp = file_transfer.connect()
	filename = "./temp/image.jpg"
	file_transfer.retrieve_frame(ftp, filename)

	# Detect and crop faces
	vision.extract_faces(filename, 4)

	# Identify the faces
	images = [pic for pic in os.listdir("./temp/") if os.path.isfile(os.path.join("./temp/", pic)]
	del images[0] # remove the temp image.jpg
	print(images)
