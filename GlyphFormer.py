import json
import sys

def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def kanji_to_subchars(text, kanji_mapping):
    subchar_text = ""
    for char in text:
        if char in kanji_mapping:
            subchar_text += " ".join(kanji_mapping[char])
        else:
            subchar_text += char
        subchar_text += " "
    return subchar_text.strip()

def main(mode, text):
    if mode == "radical":
        kanji_mapping = load_json_file('kanji2radical.json')
    elif mode == "element":
        kanji_mapping = load_json_file('kanji2element.json')
    else:
        raise ValueError("Unsupported mode. Use 'radical' or 'element'.")

    converted_text = kanji_to_subchars(text, kanji_mapping)
    print(converted_text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [radical|element] 'text to decompose'")
        sys.exit(1)
    mode = sys.argv[1]
    text = sys.argv[2]
    main(mode, text)

