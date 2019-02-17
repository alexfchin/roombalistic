import face_recognition
import sys
import os

import face_recognition_knn

known_images_dir = "./Photos/Known/"
unknown_image = "./Photos/2120.jpg"
knn_model = "./trained_knn_models/model.clf"

def recognition(cropped_images):
    face_recognition_knn.train(known_images_dir, model_save_path=knn_model, verbose=True)

    identities = [face_recognition_knn.predict(image, model_path=knn_model)
            for image in cropped_images]

    return identities

def visualize_recognition(image):
	face_recognition_knn.train(known_images_dir, model_save_path=knn_model)

	results = face_recognition_knn.predict(image, model_path=knn_model)

	face_recognition_knn.show_prediction_labels_on_image(image, results)

	return results

# For debugging purposes
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 2:
        print("usage: python recognition.py <file paths>")
        exit()
    else:
        del sys.argv[0] # Remove "recognition.py" from list of arguments
        predictions = recognition(sys.argv)
        for i in range(0,len(sys.argv)):
            print(predictions[i])
            face_recognition_knn.show_prediction_labels_on_image(sys.argv[i], predictions[i])
