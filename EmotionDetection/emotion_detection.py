import requests
import json

def emotion_detector(text_to_analyze):
    """Executes emotion detection for the text given in the function argument"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyze } }

    # sends a post request to Watson NLP library and returns the response    
    response = requests.post(url, json = input_text, headers=headers, timeout = 10)

    # check status code of the response
    if response.status_code == 200:
        # response is correct
        formatted_response=json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        
        # froms the output
        result = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}

        # search for the most dominant emotion
        dominant_score = float(0)
        dominant_emotion = ''
        for emotion, score in result.items():
            if (float(score) >= dominant_score):
                dominant_score = score
                dominant_emotion = emotion
        result.update({'dominant_emotion': dominant_emotion})

    elif response.status_code == 400:
        # response is not correct
        result = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    return result