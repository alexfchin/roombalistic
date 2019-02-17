import gcp_storage

if __name__ == "__main__":
	bucket = 'roombalistic-vcm'

	# Upload the video frame to the GCP storage bucket
	gcp_frame = 'lastsnap.jpg'
	local_frame = '/home/pi/Documents/hack@CEWIT19/imgs/lastsnap.jpg'
	gcp_storage.upload_blob(bucket, local, gcp_frame)

	# Updates id file
	gcp_id = 'id.txt'
	local_id = '/home/pi/Documents/hack@Cewit19/id.txt'
	gcp_storage.download_blob(bucket, local_id, gcp_id)
