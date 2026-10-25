"""Flask web server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the homepage."""
    return render_template('index.html')

# Route 2: Analyze the user's text
@app.route("/emotionDetector")
def detect_emotion():
    """run function"""

    # Get the text from the browser
    text = request.args.get("textToAnalyze")

    # Call your emotion detection function
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    opt = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return opt


# Start the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
