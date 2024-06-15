import os
from flask import Flask, render_template, request, jsonify
import numpy as np
import cv2
from tensorflow import keras
from keras.models import load_model
from flask import send_from_directory
import os
import tensorflow as tf
app = Flask(__name__)

pretrained_model_path = './LRCN_model.h5'
LRCN_model = load_model(pretrained_model_path)
IMAGE_HEIGHT = 71
IMAGE_WIDTH = 71
SEQUENCE_LENGTH = 20

def preprocess_video(uploaded_file, SEQUENCE_LENGTH=20):
    temp_path = './deepfake' 
    video_path = os.path.join(temp_path, 'uploaded_video.mp4')
    uploaded_file.save(video_path)
    

    video_reader = cv2.VideoCapture(video_path)


    frame_list = []

    # Iterate through the video and store frames in the frames list
    while True:
        # Read the frame
        ok, frame = video_reader.read()

        # Break the loop if the frame is not read properly
        if not ok:
            break

        # Resize the frame to fixed dimensions
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

        # Normalize the resized frame
        normalized_frame = resized_frame / 255.0

        # Append the normalized frame to the frames list
        frame_list.append(normalized_frame)

        # Break the loop if the frames list reaches the desired sequence length
        if len(frame_list) == SEQUENCE_LENGTH:
            break

    # Release the videocapture object
    video_reader.release()

    # Optionally, you can remove the temporary video file after processing
    os.remove(video_path)

    return frame_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        # Render the prediction form
        return render_template('predict.html', prediction_result=None)

    elif request.method == 'POST':
        try:
            # Get the uploaded video file
            uploaded_file = request.files['video']

            # Preprocess the video frames
            video_frames = preprocess_video(uploaded_file)

            # Convert frames to numpy array
            video_frames = np.array(video_frames)

            # Make predictions
            predictions = LRCN_model.predict(np.expand_dims(video_frames, axis=0))

            # Get the predicted class index
            predicted_class_index = np.argmax(predictions[0])

            # Get the class labels
            classes = ["real", "fake"]

            # Get the predicted class name
            predicted_class_name = classes[predicted_class_index]

            result = {
                "predicted_class": predicted_class_name,
                "confidence": round(float(predictions[0][predicted_class_index]),3)
            }

            # return render_template('predict.html', video_path=uploaded_file.filename, prediction_result=result)
            return result

        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/static/uploaded_videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('static/uploaded_videos', filename)

if __name__ == '__main__':
    app.run(debug=True)
