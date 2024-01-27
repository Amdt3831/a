import re

def func(initial_text, o):
    match = re.search('(@[^#]*)#', initial_text[o:])
    if match:
        a = match.group(1)
        r = initial_text[o:].replace(a + '#', a, 1)
        initial_text = initial_text.replace(initial_text[o:], r, 1)
    return initial_text

initial_text = input()

e = initial_text.count('@')
r = 0
o = 0

while o < len(initial_text):
    if r < e and initial_text[o] == '@' and bool(re.search('(@[^#]*)#', initial_text)):
        initial_text = func(initial_text, o)
        r += 1
    o += 1

initial_text = initial_text.strip()
initial_text = re.sub(r'\s+', ' ', initial_text)
s = re.sub(r'\\n', "\n", initial_text)
print(f'Formatted Text: {s}')
