import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_morse_code(morse_file):
    morse_dict = {}
    if os.path.isfile(morse_file):
        with open(morse_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('\t')
                    if len(parts) == 2:
                        word, code = [part.strip() for part in parts]
                        morse_dict[word.lower()] = code

    return morse_dict


def save_morse_code(morse_file, morse_dict):
    with open(morse_file, 'w') as file:
        for word, code in morse_dict.items():
            file.write(f"{word}\t{code}\n")


def text_to_morse_code(text, morse_dict):
    text = text.lower()  # Convert input text to lowercase
    morse_code_sentence = []
    for word in text.split():
        if word in morse_dict:
            morse_code_sentence.append(morse_dict[word])
        else:
            print(f"Word '{word}' not found in the Morse code dictionary. Translating and adding to the dictionary.")
            new_code = translate_to_morse_code(word)
            morse_dict[word] = new_code
            morse_code_sentence.append(new_code)
    return ' / '.join(morse_code_sentence)


def translate_to_morse_code(word):
    # Morse code translation for letters and numbers
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    morse_word = []
    for char in word:
        if char in morse_dict:
            morse_word.append(morse_dict[char])
    return ' '.join(morse_word)


clear_screen()
print('This is a program that will translate any letter and number into Morse code use no special characters\n')
print('Created By Gabriel Andrade\n')

filename = "60191_6420925_3275306.txt"
morse_code_dict = load_morse_code(filename)

while True:

    input_text = input("Enter a sentence to translate to Morse code (or type 'exit' to quit): ")
    if input_text.lower() == 'exit':
        break
    morse_code = text_to_morse_code(input_text, morse_code_dict)

    if morse_code:
        print("Morse code translation:")
        print(morse_code)
        save_morse_code(filename, morse_code_dict)
