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
	vision.extract_faces(vm_frame, 4)

	# Identify the faces
	images = [pic for pic in os.listdir("./temp/") if os.path.isfile(os.path.join("./temp/", pic)) and pic.endswith(".jpg")]
	del images[0] # remove the temp image.jpg
	print(images)
	identities = recognition.recognition(images)
	print(identities)

	# Write id info to file
	vm_id = "./temp/id.txt"
	id_file = open("./temp/id.txt", "w")
	id_file.write("\n".join(identities))
	id_file.close()

	# Send identity information to GCP storage bucket
	storage_id = "id.txt"
	gcp_storage.upload_blob(bucket, vm_id, storage_id)
