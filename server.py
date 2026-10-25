from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Route 2: Analyze the user's text
@app.route("/emotionDetector")
def detect_emotion():

    # Get the text from the browser
    text = request.args.get("textToAnalyze")

    # Call your emotion detection function
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    opt = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return opt


# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)