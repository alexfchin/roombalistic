from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
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

class Frame_Event(FileSystemEventHandler):
	def __init__(self, observer, filename):
		self.observer = observer
		self.filename = filename

	def on_modified(self, event):
		frame_upload(event)

class ID_Event(FileSystemEventHandler):
	def __init__(self, observer, filename):
		self.observer = observer
		self.filename = filename

	def on_modified(self, event):
		id_download(event)

def frame_upload(event):
	isProcessing = True
	print(event)
	id_observer = Observer()
	id_event_handler = ID_Event(id_observer, local_id)
	id_observer.schedule(id_event_handler, local_id)
	id_observer.start()
	gcp_storage.upload_blob(bucket, local_frame, gcp_frame)

	try:
		while isProcessing:
			gcp_storage.download_blob(bucket, local_id, gcp_id)
			time.sleep(1)
	except KeyboardInterrupt:
		id_observer.stop()

	id_observer.stop()

def id_download(event):
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
		observer = Observer()
		frame_event_handler = Frame_Event(observer, local_frame)
		observer.schedule(frame_event_handler, local_frame)
		observer.start()

		try:
			while not isProcessing:
				time.sleep(1)
		except KeyboardInterrupt:
			observer.stop()

		observer.join()
