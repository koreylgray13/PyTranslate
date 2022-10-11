import deepl
import sys

auth_key = "YOUR/API/KEY"  # Replace with your key
translator = deepl.Translator(auth_key)


def toSpanish():
    while True:
        inp = input("\nEnglish:   ")   
        if inp == "q":
            break
        else:   
            translation = translator.translate_text(inp, source_lang="EN", target_lang="ES")
            print("Spanish:  ", translation.text)

def toEnglish():
    while True:
        inp = input("\nSpanish:   ")   
        if inp == "q":
            break
        else:   
            translation = translator.translate_text(inp, source_lang="ES", target_lang="EN-US")
            print("English:  ", translation.text)

def detectLang():
    while True:
        inp = input("Detect Language: ")
        if inp == 'q':
            break
        elif inp == '':
            print("No Input Detected, exiting.")
            break
        else:
            lang = translator.translate_text(inp, target_lang="EN-US")
            print(lang.detected_source_lang)


def customTranslate():
    print("""
Available Languages:
    
BG - Bulgarian
CS - Czech
DA - Danish
DE - German
EL - Greek
EN - English
ES - Spanish
ET - Estonian
FI - Finnish
FR - French
HU - Hungarian
ID - Indonesian
IT - Italian
JA - Japanese
LT - Lithuanian
LV - Latvian
NL - Dutch
PL - Polish
PT - Portuguese (all Portuguese varieties mixed)
RO - Romanian
RU - Russian
SK - Slovak
SL - Slovenian
SV - Swedish
TR - Turkish
UK - Ukrainian
ZH - Chinese
    """)
    
    fromLang = input("Translate From: ")
    toLang = input("Translate To: ")
    
    if toLang == "EN":
        toLang = "EN-US"
    
    while True:
        inp = input(f"\n{fromLang}:  ")   
        if inp == "q":
            break
        else:   
            translation = translator.translate_text(inp, source_lang=fromLang, target_lang=toLang)
            print(f"{toLang}:  ", translation.text)

while True:
    start = input("""

 Select An Option: (Type 'q' to exit at any time)

 1. English To Spanish
 2. Spanish To English
 3. Detect Language
 4. Custom

    Selection: """)
    
    if start == "1":
        toSpanish()

    elif start == "2":
        toEnglish()

    elif start == "3":
        detectLang()

    elif start == "4":
        customTranslate()
        
    elif start == 'q':
        sys.exit()

    else:
        print("Please Select An Option 1-3")
