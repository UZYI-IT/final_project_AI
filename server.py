from flask import Flask, redirect, request, render_template, url_for
from final_project import emotion_detector



app = Flask(__name__)

@app.route('/')
def home():

    return render_template( 'index.html')

@app.route('/emotionDetector')
def emotion_analyzer():

    phrase = request.args.get('textToAnalyze')

    if phrase:
        result= emotion_detector(phrase)

    system_response='For the given statement, the system response is '

    for key, value in result.items():
        if key != 'dominant_emotion':
            system_response += f"'{key}' : {value}, "
    
    system_response= system_response.removesuffix(", ")
    lastHalf = system_response.rsplit(",", 1)
    system_response = " and ".join(lastHalf)
    system_response= system_response + '. The dominant emotion is <strong>' + result['dominant_emotion'] + '</strong>.'

    return system_response
    
    








if __name__ == "__main__":
    app.run(debug=True)