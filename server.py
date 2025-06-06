""" Web server for emotion_detector """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Retrieve the text to analyze from the request arguments"""
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        # Response is not correct
        return "Invalid text! Please try again!"

    # Response is correct
    # Returns a formatted string
    return f"For the given statement, the system response is \
        'anger': {response['anger']}, \
        'disgust': {response['disgust']}, \
        'fear': {response['fear']}, \
        'joy': {response['joy']} and \
        'sadness': {response['sadness']}. \
        The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """Initiates the rendering of the main application"""
    return render_template("index.html")

if __name__ == "__main__":
    # Executes the flask app and deploys it on localhost:5000
    app.run(host="localhost", port=5000)
