import os
import os.path

import gcp_storage
import vision
import recognition

# global constants
bucket = "roombalistic-vcm"
storage_frame = "lastsnap.jpg"
vm_frame = "./temp/image.jpg"
vm_id = "./temp/id.txt"
storage_id = "id.txt"

if __name__ == "__main__":
	while True:
		# Get latest from from GCP storage bucket
		gcp_storage.download_blob(bucket, storage_frame, vm_frame)

		# Detect and crop faces
		vision.extract_faces(vm_frame, 4)

		# Identify the faces
		images = []
		for pic in os.listdir("./temp/"):
			pic_path = os.path.join("./temp/", pic)
			if os.path.isfile(pic_path) and pic.endswith(".jpg"):
				images.append(pic_path)

		del images[0] # remove the temp image.jpg
		print(images)
		identities = recognition.recognition(images)
		print(identities)
		identities_string = "\n".join(map(str, identities))
		print(identities_string)

		# Write id info to file
		id_file = open(vm_id, "w")
		id_file.write(identities_string)
		id_file.close()

		# Send identity information to GCP storage bucket
		gcp_storage.upload_blob(bucket, vm_id, storage_id)
