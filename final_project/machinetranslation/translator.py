"""Instances a IBM Watson translator and defines two functions to translate e2f and viceversa."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'
authenticator_lt = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT,
    authenticator=authenticator_lt
)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """Takes an English string in input and provides French translation string as output."""

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """Takes a French string in input and provides with English translation string as output."""

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
