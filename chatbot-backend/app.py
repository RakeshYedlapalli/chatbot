# from flask import Flask, request, jsonify
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# app = Flask(__name__)

# # Load the pre-trained Sentence Transformer model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Sample FAQ data (could be loaded from a JSON or database in production)
# faq_data = [
#     {"question": "How do I return a product?", "answer": "You can return products within 30 days of purchase."},
#     {"question": "Where is my order?", "answer": "Please provide your order ID to track the status."},
#     {"question": "What is your return policy?", "answer": "You can return items within 30 days."},
#     {"question": "How do I track my order?", "answer": "You can track your order on our order tracking page."}
# ]

# # Precompute embeddings for the FAQ questions
# faq_questions = [item["question"] for item in faq_data]
# faq_embeddings = model.encode(faq_questions)

# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_input = request.json.get('message')
    
#     # Embed the user's input
#     user_input_embedding = model.encode([user_input])
    
#     # Compute cosine similarities between user's input and FAQ questions
#     similarities = cosine_similarity(user_input_embedding, faq_embeddings)
#     best_match_index = np.argmax(similarities)
    
#     # Return the best matching FAQ response
#     response = faq_data[best_match_index]["answer"]
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)  # Run on port 5000
