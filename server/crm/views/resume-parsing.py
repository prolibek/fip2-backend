import spacy
from spacy.matcher import Matcher

# Загрузка модели spaCy
nlp = spacy.load("en_core_web_sm")

def extract_information(text):
    # Обработка текста с помощью модели spaCy
    doc = nlp(text)
    
    # Инициализация Matcher
    matcher = Matcher(nlp.vocab)
    
    # Определение шаблонов для поиска
    patterns = [
        {"label": "NAME", "pattern": [{"POS": "PROPN"}]},
        {"label": "EMAIL", "pattern": [{"LIKE_EMAIL": True}]},
        {"label": "PHONE", "pattern": [{"ORTH": "("}, {"SHAPE": "ddd"}, {"ORTH": ")"}, {"SHAPE": "ddd"}, {"ORTH": "-"}, {"SHAPE": "dddd"}]},
        {"label": "PHONE", "pattern": [{"SHAPE": "ddd"}, {"ORTH": "-"}, {"SHAPE": "ddd"}, {"ORTH": "-"}, {"SHAPE": "dddd"}]}
    ]
    
    for pattern in patterns:
        matcher.add(pattern["label"], [pattern["pattern"]])
    
    # Поиск шаблонов в тексте
    matches = matcher(doc)
    
    # Извлечение и вывод информации
    extracted_info = {"name": "", "email": "", "phone": ""}
    for match_id, start, end in matches:
        span = doc[start:end]
        label = nlp.vocab.strings[match_id]
        if label == "NAME" and not extracted_info["name"]:
            extracted_info["name"] = span.text
        elif label == "EMAIL":
            extracted_info["email"] = span.text
        elif label == "PHONE":
            extracted_info["phone"] = span.text
    
    return extracted_info

# Пример использования
resume_text = """
John Doe
123 Main St, Anytown, USA
john.doe@example.com
(123) 456-7890
Experience:
- Software Developer at XYZ Corp.
- Data Analyst at ABC Inc.
"""

info = extract_information(resume_text)
print(info)
