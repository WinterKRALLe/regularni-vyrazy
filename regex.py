import re

def isValid(string, pattern):
    patternMap = {
        '#': r'\d',
        '$': r'[a-zA-Z]',
        '&': r'\w',
        '|': r'|',
        '*': r'*',
        '.': r'\.',
    }

    regex = ''.join([patternMap.get(ch, ch) for ch in pattern])

    return bool(re.fullmatch(regex, string))


print(isValid('test@example.com', '&&*@&&*.$$$*'))
print(isValid('test@example', '&&*@&&*.$$$*'))

print(isValid('1234567890', '#########'))
print(isValid('123456789', '#########'))