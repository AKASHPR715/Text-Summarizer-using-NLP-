# 📝 Text Summarizer Web App

A Flask-based web application for text summarization using two methods:  
1. **Extractive Summarization** (custom keyword-based logic)  
2. **Sumy (TextRank Algorithm)** for graph-based ranking of sentences.

This project allows users to input large text blocks and receive concise summaries through a clean, responsive web interface.

---

## 🌟 Features

- ✨ Clean UI built with HTML and CSS for better readability.
- ⚙️ Two summarization options:
  - **Extractive**: Basic keyword frequency-based summarizer.
  - **Sumy**: Advanced TextRank algorithm-based summarizer using the `sumy` library.
- 🧠 Natural Language Toolkit (NLTK) integration for tokenization and stopword removal.
- 🚀 Built with Python’s Flask micro-framework — simple and scalable.

---

## 📁 Project Structure
text-summarizer/
│
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html          # Main input form page
│   └── output.html         # Summary results page
├── static/                 # (Optional) CSS or assets
│
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies

## 🔍 How It Works

### 🧠 Extractive Summarization

This method identifies the most important sentences in the original text and selects them to create a summary. Here's how it works:

1. **Sentence Tokenization**:  
   The input text is broken down into individual sentences using `nltk.sent_tokenize()`.

2. **Word Tokenization and Cleaning**:  
   Each sentence is tokenized into words, with stopwords (like "the", "and", "is") removed using NLTK's built-in stopword list.

3. **Frequency Calculation**:  
   A frequency table is created for the remaining keywords to determine how important each word is.

4. **Sentence Scoring**:  
   Each sentence is scored based on the total frequency of its words.

5. **Top Sentence Selection**:  
   The top-scoring sentences (typically those above a certain average score threshold) are selected to form the summary.

---

### 🧠 Sumy Summarization (TextRank)

This method uses an advanced graph-based algorithm called **TextRank**, which is similar to Google’s PageRank:

1. **Parsing and Tokenizing**:  
   The input text is parsed and tokenized using `sumy.parsers.plaintext.PlaintextParser` and `sumy.nlp.tokenizers.Tokenizer`.

2. **Building a Sentence Graph**:  
   Sentences are represented as nodes in a graph. Edges represent similarity between sentences (e.g., based on common words).

3. **Ranking Sentences**:  
   The TextRank algorithm ranks sentences based on their importance in the graph.

4. **Generating Summary**:  
   The top-ranked sentences are selected to form the final summary.

> This approach is considered more context-aware and tends to produce summaries that better preserve the meaning of the original text.

## 🚀 Running the App

Follow these steps to get the Text Summarizer up and running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py

