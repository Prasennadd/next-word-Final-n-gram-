# ============================
# File: app.py
# ============================
from flask import Flask, request, jsonify, render_template
from model.ngram_model import predict_next_all, load_model

app = Flask(__name__)
ngram_model = load_model("model/corpus.txt", n=3)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/suggest')
def suggest():
    # query = request.args.get('q', '')
    # next_word = predict_next_all(ngram_model, query)
    # return jsonify([f"{query} {next_word}" if next_word else query])
    query = request.args.get('q', '')
    next_words = predict_next_all(ngram_model, query)
    return jsonify([f"{query} {word}" for word in next_words]) if next_words else jsonify([query])
if __name__ == '__main__':
    app.run(debug=True)
