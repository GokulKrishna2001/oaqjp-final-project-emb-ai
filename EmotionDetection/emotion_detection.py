import json
import requests

def emotion_detector(text_to_analyse):

    #url given in the question
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #expected format
    myobj = {"raw_document": {"text": text_to_analyse}}

    #specified header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #sending a POST response
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    #extracting the required emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    #returning the required
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
