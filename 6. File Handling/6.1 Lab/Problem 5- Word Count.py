import re


with open(r"words.txt") as word_data, \
     open(r"text.txt") as text_data, \
     open("output.text", "w") as output:

    text = text_data.read()
    word_frequencies = {}

    for word in word_data.read().split():
        matches = re.findall(rf'[- .,!?]({word}[- .,!?])', text, re.MULTILINE + re.IGNORECASE)
        word_frequencies[word] = len(matches)

    for word, count in sorted(word_frequencies.items(), key=lambda x: -x[1]):
        print(f"{word} - {count}", file=output)


with open("output.text") as output:
    for line in output:
        print(line, end="")
