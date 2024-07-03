import json
import os
import requests
import time

def wait_for_service(url, timeout=1800):
    """Wait for the service to become available."""

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Service is up and running.")
                return True
        except requests.exceptions.RequestException:
            pass
        print("Waiting for service to be available...")
        time.sleep(5)
    raise Exception("Service did not become available within the timeout period.")

def translate_text(text, target_language):
    """Translates text into the target language using LibreTranslate API."""
    url = "http://libretranslate:5000/translate"
    payload = {
        "q": text,
        "source": "en",
        "target": target_language,
        "format": "text"
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()
    response_json = response.json()
    return response_json["translatedText"]

def translate_json(input_file, output_file, target_language):
    """Translates the content of a JSON file to the target language using LibreTranslate API."""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated_data = translate(target_language, data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)

def translate(target_language, data):
    translated_data = {}

    for key, value in data.items():
        if isinstance(value, str):
            translated_data[key] = translate_text(value, target_language)
        elif isinstance(value, dict):
            translated_data[key] = translate(target_language, value)
        else:
            translated_data[key] = value
    return translated_data

if __name__ == "__main__":
    service_url = "http://libretranslate:5000"
    wait_for_service(service_url)

    input_file = 'locales/en/common.json'  # Path to the input JSON file
    locales_dir = 'locales'

    for locale in os.listdir(locales_dir):
        if locale == 'en' or locale.startswith('.'):
            continue
        output_dir = os.path.join(locales_dir, locale)
        output_file = os.path.join(output_dir, 'common.json')
        target_language = locale

        os.makedirs(output_dir, exist_ok=True)
        translate_json(input_file, output_file, target_language)
        print(f"Translation to {target_language} completed. Translated file saved as {output_file}")