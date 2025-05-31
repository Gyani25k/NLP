from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import pandas as pd
import spacy
import nltk
from transformers import pipeline

nltk.download('punkt')

app = Flask(__name__)
socketio = SocketIO(app)

# Load NLP models
nlp = spacy.load('en_core_web_sm')

# Transformer pipeline for sentiment analysis
sentiment_pipeline = pipeline('sentiment-analysis')

@app.route('/process-structured', methods=['POST'])
def process_structured():
    json_data = request.json
    df = pd.DataFrame(json_data)
    response = {}  # Perform structured data analysis
    return jsonify(response)

@app.route('/process-unstructured', methods=['POST'])
def process_unstructured():
    text = request.json.get('text')
    doc = nlp(text)
    entities = [{'text': ent.text, 'label_': ent.label_} for ent in doc.ents]
    sentiment_result = sentiment_pipeline(text)
    response = {'entities': entities, 'sentiment': sentiment_result}
    return jsonify(response)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
