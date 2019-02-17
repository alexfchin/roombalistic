import face_recognition
import os

import face_recognition_knn

known_images_dir = "./Photos/Known"
unknown_image = "./Photos/2120.jpg"
knn_model = "./trained_knn_model.clf"

def recognition(cropped_images):
    face_recognition_knn.train(known_images_dir, model_save_path=knn_model, verbose=True)

    identities = [face_recognition_knn.predict(image, model_path=knn_model)
            for image in cropped_images]

    return identities

# For debugging purposes
if __name__ == "__main__":
    predictions = recognition([unknown_image])
    face_recognition_knn.show_prediction_labels_on_image(unknown_image, predictions)
    print(predictions)
