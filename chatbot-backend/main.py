# # import openai

# # import openai
# import os
# from openai import OpenAI

# # openai.api_key = "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"

# # chat_assistant.py


# # Set your API key here
# openai.api_key = "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"  # recommended
# # OR directly (not safe): openai.api_key = "sk-..."



# client = OpenAI()  # This automatically reads OPENAI_API_KEY from env

# def chat_with_gpt(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=150
#     )
#     return response.choices[0].message.content


# # Example usage
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         reply = chat_with_gpt(user_input)
#         print("Assistant:", reply)



# from openai import OpenAI

# client = OpenAI()  # This automatically reads OPENAI_API_KEY from env

# def chat_with_gpt(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4"
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=150
#     )
#     return response.choices[0].message.content
