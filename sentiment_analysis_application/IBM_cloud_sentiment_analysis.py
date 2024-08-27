from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
import unittest

{
  "apikey": "dIJFXkPYMSby0_ZjpDvw6JC07TwMJmm8T4dBa-olG7Zw",
  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:natural-language-understanding:eu-de:a/410de59c8c7b4690a96487be533458d0:b9864ad2-d78f-4dbd-9ac4-5c87e89c8d60:resource-key:a7f8cf14-3472-4bfd-a318-e62b646e392a",
  "iam_apikey_id": "ApiKey-b075f2b9-65ce-47f6-857a-c55e8fe46903",
  "iam_apikey_name": "Auto-generated service credentials",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/410de59c8c7b4690a96487be533458d0::serviceid:ServiceId-86aa9b73-5cdb-4cd9-be84-082d26bb006b",
  "url": "https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/b9864ad2-d78f-4dbd-9ac4-5c87e89c8d60"
}

def analyze_sentiment(text):
    # Replace with your API Key and URL
    api_key = 'dIJFXkPYMSby0_ZjpDvw6JC07TwMJmm8T4dBa-olG7Zw'
    url = 'https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/b9864ad2-d78f-4dbd-9ac4-5c87e89c8d60'

    # Create an IAM authenticator
    authenticator = IAMAuthenticator(api_key)

    # Create the Natural Language Understanding service
    nlu = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )
    nlu.set_service_url(url)

    # Analyze the sentiment
    response = nlu.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions())
    ).get_result()

    return response['sentiment']['document']

# Test the function
text = "I love this product! It's amazing!"
result = analyze_sentiment(text)
print(f"The sentiment of the text is: {result['label']}")