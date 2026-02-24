from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():

    #getting the text as input
    text_to_analyze = request.args.get('textToAnalyze')

    #calling the function
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again."

    #getting the values
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    #the required output
    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
