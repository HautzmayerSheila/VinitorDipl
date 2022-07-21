def emoji_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "happy face",
        ":(": "sad face"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output