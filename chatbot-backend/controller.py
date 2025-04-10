import re
from flask import Flask, request, jsonify
from connectBedrock import get_bedrock_response,get_context_from_json
from flask_cors import CORS, cross_origin
 


app = Flask(__name__)
CORS(app, support_credentials=True)

 
def sanitize_input(input_text):
    # Remove any unwanted characters (e.g., HTML tags, special characters)
    sanitized = re.sub(r'[^\w\s]', '', input_text)
    return sanitized
 
def truncate_input(input_text, max_length=100):
    # Truncate the input to a maximum length
    return input_text[:max_length]
 
def tokenize_input(input_text):
    # Tokenize the input (simple whitespace tokenization)
    tokens = input_text.split()
    return tokens
 
def sanitize_and_remove_duplicates(input_text):
    # Remove punctuation using regex
    sanitized = re.sub(r'[^\w\s]', '', input_text)
    
    # Tokenize the input (split by whitespace)
    tokens = sanitized.split()
    
    # Remove duplicate words while preserving order
    seen = set()
    unique_tokens = [word for word in tokens if not (word.lower() in seen or seen.add(word.lower()))]
    
    return unique_tokens

def remove_stop_words(tokens):
    # Extensive list of stop words
    custom_stop_words = {
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
        'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
        'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
        'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
        'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
        'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
        'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
        'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven',
        'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'
    }
    
    # Remove stop words from the token list
    filtered_tokens = [word for word in tokens if word.lower() not in custom_stop_words]
    return filtered_tokens


@app.route('/ask', methods=['POST'])
@cross_origin(supports_credentials=True)
def ask():
    question = request.json.get('question')
   
    # Sanitize, truncate, and tokenize the input
    processed_tokens = sanitize_and_remove_duplicates(question)
    
    # Join tokens back to a single string
    processed_question = ' '.join(processed_tokens)
    sanitized_question = sanitize_input(processed_question)
    truncated_question = truncate_input(sanitized_question)
    tokenized_question = tokenize_input(truncated_question)
   
    # Remove stop words
    filtered_question = remove_stop_words(tokenized_question)
   
    # Join tokens back to a single string for the LLM
    processed_question = ' '.join(filtered_question)
    
    #get the context
    context=get_context_from_json("Data.json")

    #Call LLM with context
    processed_query = get_bedrock_response(processed_question, context)

    return jsonify({'text': processed_query,'sender':'bot'})

 
if __name__ == '__main__':
    app.run(debug=True)