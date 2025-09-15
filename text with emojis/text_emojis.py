#Create a Python program that replaces certain words in a text with emojis.

emoji = {
    "happy": "😀",
    "sad": "😔",
    "super": "👌",
    "ok": "👍"
}
def text_replace():
    text = input("Enter the text you want to replace: ").lower()
    # text = "I am SUPER Happy today, but my friend is sad. It's ok, we will still have a super day!"
    for word,emj in emoji.items():
        text = text.replace(word,emj)
    return text
print("Converted text : ",text_replace())