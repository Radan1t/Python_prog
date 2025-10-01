from translator_pkg import gtrans_v4 as g4

if __name__ == "__main__":
    sample = "Добрий день. Як справи?"
    print("LangDetect (all):", g4.LangDetect(sample, "all"))
    print("Translate to en:", g4.TransLate(sample, "auto", "en"))
    print("CodeLang('ukrainian') ->", g4.CodeLang("ukrainian"))
    g4.LanguageList("screen", sample)
