from flask import Flask, render_template, Response
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# pre-trained CNN model
model = tf.keras.models.load_model('model_path')

# Function to preprocess frames
def preprocess_frame(frame):
    # Preprocess the frame (e.g., resize, normalize, etc.)
    # Return the preprocessed frame
    pass

# Function to perform inference using the CNN model
def perform_inference(frame):
    # Preprocess the frame
    preprocessed_frame = preprocess_frame(frame)

    # Convert the frame to the appropriate input format for your CNN model
    input_data = np.expand_dims(preprocessed_frame, axis=0)

    # Perform inference using the CNN model
    predictions = model.predict(input_data)

    # Process the predictions as needed
    # (e.g., perform further analysis, make decisions, etc.)
    return predictions

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Function to generate video frames
def generate_frames():
    # Open the live stream or video file
    stream = cv2.VideoCapture('your_stream_path')

    while True:
        # Read the next frame from the stream
        ret, frame = stream.read()

        # Check if the stream has ended
        if not ret:
            break

        # Perform inference using your CNN model
        predictions = perform_inference(frame)

        # Display the frame or perform any other operations as needed
        # (e.g., draw bounding boxes, annotate predictions, etc.)

        # Convert the frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame as an HTTP response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the stream
    stream.release()

# Route for the video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)