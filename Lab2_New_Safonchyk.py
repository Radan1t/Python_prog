from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

LANG_MAP = {
    'english': 'en',
    'ukrainian': 'uk',
    'french': 'fr',
    'german': 'de',
    'spanish': 'es',
}

def TransLate(text, lang):
    lang_code = lang.lower()
    if lang_code in LANG_MAP:
        lang_code = LANG_MAP[lang_code]
    try:
        translated = GoogleTranslator(target=lang_code).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text):
    try:
        langs = detect_langs(text)  
        best = langs[0]
        return best.lang, best.prob
    except Exception:
        return None, 0

def CodeLang(lang):
    lang_lower = lang.lower()
    if lang_lower in LANG_MAP:
        return LANG_MAP[lang_lower] 
    for name, code in LANG_MAP.items():
        if code == lang_lower:
            return name  
    return None

if __name__ == "__main__":
    text = input("Введіть текст для перекладу: ")
    target_lang = input("Введіть мову або код мови для перекладу: ")
    
    detected_lang, confidence = LangDetect(text)
    print(f"Визначена мова: {detected_lang}, рівень впевненості: {confidence:.2f}")
    
    translation = TransLate(text, target_lang)
    print(f"Переклад: {translation}")
