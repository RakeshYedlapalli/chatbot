import boto3
import json
import urllib.parse
from botocore.exceptions import ClientError
from botocore.config import  Config
import requests
import xml.etree.ElementTree as ET


# AWS Credentials and Configuration
aws_access_key_id = ""  # Replace with your actual AWS access key
aws_secret_access_key = ""  # Replace with your actual AWS secret key
aws_region = ""
 
# Encodage du mot de passe pour l'URL (car il contient des caractères spéciaux)
encoded_password = urllib.parse.quote("")
 
# Configuration du proxy
proxy_config = Config(
    proxies={
        'http': f'http://:{encoded_password}@hostaddress',
        'https': f'http://:{encoded_password}@hostaddress'
    }
)


#This function is not in use as of now:
def fetch_abstracts(user_prompt):
    """
    Fetch abstracts of documents based on the user prompt.

    Args:
        user_prompt (str): The query term entered by the user.

    Returns:
        list: A list of abstracts if found, otherwise an empty list.
    """
    url = "https://search.worldbank.org/api/v3/wds"
    params = {
        "format": "json",  # Request JSON format
        "qterm": user_prompt,  # User-entered query term
        "fl": "abstracts",  # Retrieve the abstracts field
        "rows": 5  # Fetch 20 rows
    }
    try:
        response = requests.get(url, params=params,proxies=proxy_config.proxies)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            documents = data.get("documents", {})
            abstracts = [
                doc.get("abstracts", {}).get("cdata!", None)
                for doc in documents.values()
                if "abstracts" in doc
            ]
            # Filter out None values
            abstracts = [abstract for abstract in abstracts if abstract]
            print(abstracts)
            return abstracts
        else:
            print(f"Failed to fetch metadata: {response.status_code}")
            return []
    except Exception as e:
        print(f"Exception occurred while fetching metadata: {e}")
        return []
 

#mocking search api for context
def get_context_from_json(file_path):
    """
    Extract context from the Wind.json file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        str: Combined context from abstracts or other relevant fields.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            documents = data.get("documents", {})
            
            # Extract abstracts or other relevant fields
            context_list = [
                doc.get("abstracts", {}).get("cdata!", None)
                for doc in documents.values()
                if "abstracts" in doc
            ]
            
            # Filter out None values and combine into a single string
            context = "\n\n".join([abstract for abstract in context_list if abstract])
            return context
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def get_bedrock_response(prompt,pdf_url=None):
    try:
        # Create the Bedrock client with proxy configuration
        bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            config=proxy_config
        )
        
        
        # Combine the PDF URL with the user prompt
        full_prompt = f"Context: {pdf_url}\n\nQuestion: {prompt}"
        
        # Prepare the request body
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        })
        
        
        # Invoke the model
        response = bedrock_runtime.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",  # Replace with your MODEL ID
            body=body
        )
        
        # Parse the response body
        response_body = json.loads(response.get("body").read())
        return response_body["content"][0]["text"]
    
    except ClientError as e:
        print(f"Error call: {e}")
        print(f"Error type: {type(e)}")
        print(f"Error code: {e.response['Error']['Code'] if 'Error' in e.response else 'Unavailable'}")
        return None
    
    except Exception as e:
        print(f"Exception: {e}")
        print(f"Exception type: {type(e)}")
        return None