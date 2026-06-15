"""
This module runs the Flask server for the emotion detection application.
It handles routes for processing text and returning emotion scores.
"""

from flask import Flask, request, render_template
from final_project import emotion_detector



app = Flask(__name__)

@app.route('/')
def home():
    """
    This route loads the intial page so the user can load the text to analyze
    """

    return render_template( 'index.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    """
    This route analyzes the user submitted text by calling teh emotion_detector function
    """

    phrase = request.args.get('textToAnalyze')

    result= emotion_detector(phrase)

    if result['dominant_emotion'] == 'None':
        system_response= '<strong>Invalid text! Please try again!</strong>'
        return system_response

    system_response='For the given statement, the system response is '

    for key, value in result.items():
        if key != 'dominant_emotion':
            system_response += f"'{key}' : {value}, "
    system_response= system_response.removesuffix(", ")
    last_half = system_response.rsplit(",", 1)
    system_response = " and ".join(last_half)
    system_response= (
        system_response + '. The dominant emotion is <strong>'
        + result['dominant_emotion'] + '</strong>.'
    )

    return system_response

if __name__ == "__main__":

    app.run(debug=True)
