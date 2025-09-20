from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text, lang):
    code = CodeLang(lang)
    if not code:
        return f"Помилка: Невідома мова '{lang}'"
    try:
        result = translator.translate(text, dest=code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt):
    try:
        detected = translator.detect(txt)
        return f"Detected(lang={detected.lang}, confidence={detected.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang):
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:   
        return lang_lower
    for code, name in LANGUAGES.items():  
        if name.lower() == lang_lower:
            return code
    return None

txt = input("Введіть текст для перекладу: ")
lang = input("Введіть мову перекладу (код або назву): ")

print("\n--- Результати ---")
print("Ваш текст:", txt)
print(LangDetect(txt))
print("Переклад:", TransLate(txt, lang))
print("Код мови:", CodeLang(lang))
