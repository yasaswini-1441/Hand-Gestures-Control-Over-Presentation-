from unidecode import unidecode

with open("presentation_controller.py", "r", encoding="utf-8") as f:
    content = f.read()

cleaned = unidecode(content)

with open("presentation_controller.py", "w", encoding="utf-8") as f:
    f.write(cleaned)
