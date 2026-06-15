import requests, json



def emotion_detector(text_to_analyze):

    # URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input json: { "raw_document": { "text": text_to_analyze } }

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input = {
        "raw_document": { "text": text_to_analyze } 
    }
    response = requests.post("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict", headers= headers, json= input )
    output = response.json()
    filteredOutput = output['emotionPredictions'][0]['emotion']
    high_score = max(filteredOutput, key=filteredOutput.get)

    filteredOutput['dominant_emotion']= high_score


    # print(json.dumps(filteredOutput, indent=2))

    return  filteredOutput
    

    