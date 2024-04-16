from flask import Flask, render_template, jsonify, request
import subprocess
from gtts import gTTS
import os

app = Flask(__name__)

def speak_text(text):
    # Save text to speech as temporary audio file
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")

    # Play the audio file
    os.system("mpg321 temp.mp3")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api', methods=['GET'])
def api():
    query = request.args.get('query', '')
    prompt = f"I will give you a prompt. response in less than 300 words, and act like medical, health chatbot and if I ask anything other than health / medical, just say something like sorry I am health bot... now here is the prompt - {query}"

    command = f"tgpt -q '{prompt}'"

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        result = {'query': query, 'output': output.strip()}
        speak_text(output)
        return jsonify(result)

    except subprocess.CalledProcessError as e:
        error_message = f"Error running command 'tgpt': {e}"
        return jsonify({'error': error_message})

if __name__=="__main__":
    app.run(debug=True)






