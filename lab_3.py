#treść zadania:
# Opracuj program, korzystający z wyrażeń regularnych zmień przykładowy nagłówek wiadomości w słownik.
                                # From: author@example.com
                                # User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
                                # MIME-Version: 1.0
                                # To: editor@example.com


import re

data = '''From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com'''

lines = re.split(r'\n', data)
temp = []


for i in range(len(lines)):
    temp.append(re.split(r':\s', lines[i]))

dictionary = {}

for i in range(len(temp)):
    dictionary[temp[i][0]] = temp[i][1]


print(dictionary)
