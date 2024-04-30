morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': '\n'}
text = input().upper()
morse_text = []
for char in text:
    morse_char = morse_code.get(char)
    morse_text.append(morse_char)
morse_string = " ".join(morse_text)
morse_lines = morse_string.split('\n')
morse_lines_stripped = []
for line in morse_lines:
    stripped_line = line.strip()
    morse_lines_stripped.append(stripped_line)
final_morse_string = "\n".join(morse_lines_stripped)
print(final_morse_string)