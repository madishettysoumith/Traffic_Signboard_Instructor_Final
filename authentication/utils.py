import os
import logging
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import UnidentifiedImageError

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variable for the model
model = None

# Class labels for traffic signs
classes = {
        0: 'Speed limit (20km/h)',
        1: 'Speed limit (30km/h)', 
        2: 'Speed limit (50km/h)', 
        3: 'Speed limit (60km/h)', 
        4: 'Speed limit (70km/h)', 
        5: 'Speed limit (80km/h)', 
        6: 'End of speed limit (80km/h)', 
        7: 'Speed limit (100km/h)', 
        8: 'Speed limit (120km/h)', 
        9: 'No passing', 
        10: 'No passing veh over 3.5 tons', 
        11: 'Right-of-way at intersection', 
        12: 'Priority road', 
        13: 'Yield', 
        14: 'Stop', 
        15: 'No vehicles', 
        16: 'Veh > 3.5 tons prohibited', 
        17: 'No entry', 
        18: 'General caution', 
        19: 'Dangerous curve left', 
        20: 'Dangerous curve right', 
        21: 'Double curve', 
        22: 'Bumpy road', 
        23: 'Slippery road', 
        24: 'Road narrows on the right', 
        25: 'Road work', 
        26: 'Traffic signals', 
        27: 'Pedestrians', 
        28: 'Children crossing', 
        29: 'Bicycles crossing', 
        30: 'Beware of ice/snow',
        31: 'Wild animals crossing', 
        32: 'End speed + passing limits', 
        33: 'Turn right ahead', 
        34: 'Turn left ahead', 
        35: 'Ahead only', 
        36: 'Go straight or right', 
        37: 'Go straight or left', 
        38: 'Keep right', 
        39: 'Keep left', 
        40: 'Roundabout mandatory', 
        41: 'End of no passing', 
        42: 'End no passing veh > 3.5 tons'
    }

# Function to load the model
def load_traffic_model():
        global model
        if model is None:
            # Load the uploaded model
            model_path = r"C:\Users\soumith\Desktop\new_model.h5"
            model = load_model(model_path)
            logging.info(f"Model loaded from {model_path}")
        return model

# Prediction function
def predict_traffic_sign(image_path):
        try:
            # Load and preprocess the image
            image = load_img(image_path, target_size=(32, 32))  # Resize to (32, 32)
            image = img_to_array(image) / 255.0  # Normalize pixel values to [0, 1]
            if image.shape[-1] != 1:  # Convert to grayscale if necessary
                image = np.mean(image, axis=-1, keepdims=True)
            image = np.expand_dims(image, axis=0)  # Add batch dimension

            logging.info(f"Preprocessed image shape: {image.shape}")

            # Load the model if not already loaded
            model = load_traffic_model()

            # Predict the traffic sign
            prediction = model.predict(image)
            logging.info(f"Prediction shape: {prediction.shape}")

            # Get the class ID and confidence
            class_id = np.argmax(prediction)
            confidence = prediction[0][class_id]
            return classes[class_id], round(confidence * 100, 2)

        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return "Error", 0.0
