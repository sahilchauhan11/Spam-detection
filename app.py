from flask import Flask, request, render_template, jsonify
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
# Load model and vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
app = Flask(__name__)
def transform_text(text):
    # 1️⃣ Lowercase
    text = text.lower()
    
    # 2️⃣ Tokenize
    text = nltk.word_tokenize(text)
    
    # 3️⃣ Keep only alphanumeric tokens
    text = [i for i in text if i.isalnum()]
    
    # 4️⃣ Remove stopwords and punctuation
    text = [i for i in text if i not in stop_words and i not in string.punctuation]
    
    # 5️⃣ Stem
    text = [ps.stem(i) for i in text]
    
    # 6️⃣ Join back to string
    return " ".join(text)
# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['email_text']  
    transformed_message=transform_text(message)
    vector = vectorizer.transform([transformed_message])
    pred = model.predict(vector)[0]
    result = "Spam" if pred == 1 else "Not Spam"
    return render_template('index.html', prediction=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)