import vision as vi
import os
import time

# [START vision_face_detection_tutorial_run_application]
# def main(input_folder):

start = time.time()
imgFolder = os.listdir("images")
for img in imgFolder:
    imgUrl = 'images/'+img
    vi.main(imgUrl, 'out.jpg', 5)
    end = time.time()
    print('Time: ' + str(end - start))
