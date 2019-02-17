import os
import os.path

import gcp_storage
import vision
import recognition

if __name__ == "__main__":
	bucket = "roombalistic-vcm"

	# Get latest from from GCP storage bucket
	storage_frame = "lastsnap.jpg"
	vm_frame = "./temp/image.jpg"
	gcp_storage.download_blob(bucket, storage_frame, vm_frame)

	# Detect and crop faces
	vision.extract_faces(filename, 4)

	# Identify the faces
	images = [pic for pic in os.listdir("./temp/") if os.path.isfile(os.path.join("./temp/", pic))]
	del images[0] # remove the temp image.jpg
	print(images)
	identities = recognition.recognition(images)
	print(identities)

	# Send identity information to GCP storage bucket
	vm_id = "./temp/id.txt"
	storage_id = "id.txt"
	gcp_storage.upload_blob(bucket, vm_id, storage_id)
