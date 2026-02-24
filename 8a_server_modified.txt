"""
Flask server module for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page.

    Returns:
        str: The rendered index.html template.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Retrieves input text, calls emotion detection,
    and returns formatted results.

    Returns:
        str: Formatted emotion result.
        tuple: Error message with HTTP 400 status if invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if (
        text_to_analyze is None
        or not text_to_analyze.strip()
    ):
        return "Invalid text! Please try again.", 400

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again.", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
