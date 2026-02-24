import json
import requests
def emotion_detector(text_to_analyse):
	
    #url given in the question
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

	#for the expected format given in the question
	myobj = { "raw_document": { "text": text_to_analyse } }

	#specified header
	header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

	#sending a POST response
	response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    #extracting the required emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)

    #returning the required
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

>>> from emotion_detection import emotion_detector
>>> emotion_detector("I am so happy I am doing this")
{'anger': 0.0043079085, 'disgust': 0.00041127237, 'fear': 0.0037504788, 'joy': 0.9918804, 'sadness': 0.014091322, 'dominant_emotion': 'joy'}
