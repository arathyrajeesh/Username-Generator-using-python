import re

def text_analyzer(text):
    characters = len(text)

    words = len(text.split())

    sentences = re.split(r'[.!?]+', text)

    return {
        "Characters": characters,
        "Words": words,
        "Sentences": len(sentences)
    }

paragraph = "Python is a powerful programming language. It is widely used in web development, data science, and artificial intelligence"

result = text_analyzer(paragraph)

print("Characters:", result["Characters"])
print("Words:", result["Words"])
print("Sentences:", result["Sentences"])
