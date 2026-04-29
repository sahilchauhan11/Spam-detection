# 📩 Email SpamShield: Machine Learning Detection

An end-to-end **Machine Learning web application** designed to classify emails as **Spam** or **Ham (Not Spam)**. This project leverages **Natural Language Processing (NLP)** for text preprocessing and a high-accuracy **Multinomial Naive Bayes classifier** for prediction.

---

## 🚀 Features

* **Complete NLP Pipeline:** Performs text preprocessing including tokenization, stopword removal, and stemming using NLTK.
* **High-Performance Model:** Implements Multinomial Naive Bayes, achieving **98%+ accuracy** on benchmark datasets.
* **Interactive Web Interface:** Flask-based web app for real-time spam detection from user input.
* **Responsive UI:** Clean and modern interface built using HTML5 and CSS3.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Machine Learning:** Scikit-learn
* **NLP:** NLTK (Natural Language Toolkit)
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3

---

## 📂 Project Structure

```text
Spam-detection/
│
├── app.py              # Flask backend logic and routing
├── vectorizer.pkl      # Pre-trained TF-IDF vectorizer (serialized)
├── model.pkl           # Trained MultinomialNB model (serialized)
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sahilchauhan11/Spam-detection.git
cd Spam-detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

* **Mac/Linux:**

```bash
source venv/bin/activate
```

* **Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The app will be available at:
👉 http://127.0.0.1:5000/

---

## 🧠 How It Works

The system follows a structured pipeline:

### 1. Preprocessing

* Converts text to lowercase
* Removes punctuation and numbers
* Eliminates stopwords
* Applies stemming using Porter Stemmer

### 2. Feature Extraction

* Uses **TF-IDF (Term Frequency–Inverse Document Frequency)**
* Converts text into numerical vectors
* Assigns higher importance to rare but meaningful words

### 3. Classification

* Uses **Multinomial Naive Bayes**
* Calculates probabilities of the email belonging to Spam or Ham
* Particularly effective for text-based classification problems

---

## 📌 Future Improvements

* Add deep learning models (LSTM / Transformers)
* Deploy on cloud (AWS / Render / Vercel)
* Add email API integration (Gmail/Outlook)
* Improve UI/UX with React frontend

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.
