import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    emotion = response.json()['emotionPredictions'][0]['emotion']
    max_emotion = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = max_emotion
    return emotion