import gcp_storage
import laser
import time

# global constants
bucket = 'roombalistic-vcm'

gcp_frame = 'lastsnap.jpg'
local_frame = '/home/pi/Documents/hack@CEWIT19/imgs/lastsnap.jpg'

gcp_id = 'id.txt'
local_id = '/home/pi/Documents/hack@CEWIT19/roombalistic/id.txt'

# casual global variable for cyclic event-handling
isProcessing = False

def frame_upload():
    isProcessing = True
    print(event)
    gcp_storage.upload_blob(bucket, local_frame, gcp_frame)

    try:
        time.sleep(1)
        gcp_storage.download_blob(bucket, local_id, gcp_id)
    except KeyboardInterrupt:
        id_observer.stop()

    id_observer.stop()

def id_download():
    with open(local_id, "r") as id_file:
        identifiers = id_file.read()
    print(identifiers)
    if "Unknown" not in identifiers:
        laser.ready_laser(True)
    isProcessing = False
    print(event)

if __name__ == "__main__":

    while True:
        # Upload the video frame to the GCP storage bucket
        # and updates id file
        frame_upload()

        while isProcessing:
            time.sleep(0.1)