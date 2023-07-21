import requests
import detectlanguage

# Устанавливаем ключ API для detectlanguage
detectlanguage.configuration.api_key = 'f4b49a21ef0a4d14a0d898f16471ece4'

def detect_source_language(text):
    try:
        result = detectlanguage.detect(text)
        return result[0]['language']
    except:
        return "en"  # Если не удается определить язык, предположим, что это английский

def translate_text(text, target_language):
    source_language = detect_source_language(text)
    url = "http://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_language}|{target_language}"
    }

    response = requests.get(url, params=params)
    translation = response.json()["responseData"]["translatedText"]
    return translation

if __name__ == "__main__":
    while True:
        input_text = input("Введите текст для перевода (или 'exit' для выхода): ")
        if input_text.lower() == "exit":
            break

        target_language = input("Введите язык перевода (например, 'ru' для русского, 'es' для испанского): ")
        translated_text = translate_text(input_text, target_language)

        print(f"Перевод: {translated_text}")
