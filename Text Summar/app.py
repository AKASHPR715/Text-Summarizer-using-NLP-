from flask import Flask, redirect, render_template, request, url_for
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

app = Flask(__name__)
app.secret_key = "textsummar"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summery_type', methods=['POST'])  # Changed to POST method
def summery_type():
    # Check if the form method is POST
    if request.method == 'POST':
        # Get the form data
        summery_method = request.form['sum_method']
        userText = request.form['userText']

        # Redirect to the appropriate summarizer based on the selected method
        if summery_method == "etractive":
            return redirect(url_for('Ex_summerize', userText=userText))
        if summery_method == "sumy":
            return redirect(url_for('sumy', userText=userText))
    return render_template('index.html')


@app.route('/make_summery', methods=['GET'])
def make_summery():
    summary_text = request.args.get('summary_text')
    return render_template('output.html', summary_text=summary_text)


# Example placeholder for an extractive summarizer
@app.route('/Ex_summerize')
def Ex_summerize():
    userText = request.args.get('userText')
    # Perform the extractive summarization here (replace with your logic)
    # Example: Just returning the first 200 characters
    summary = userText[:200]
    return redirect(url_for('make_summery', summary_text=summary))


# Example placeholder for the Sumy summarizer (TextRank)
@app.route('/sumy')
def sumy():
    userText = request.args.get('userText')
    # Use Sumy TextRank summarizer
    parser = PlaintextParser.from_string(userText, Tokenizer())
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 2)  # Summarize to 2 sentences (can be adjusted)
    
    summary_text = ' '.join(str(sentence) for sentence in summary)
    return redirect(url_for('make_summery', summary_text=summary_text))


if __name__ == "__main__":
    app.run(debug=True)
