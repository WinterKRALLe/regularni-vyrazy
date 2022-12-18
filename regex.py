import string

patternMap = {
    '#': '0123456789',
    '$': string.ascii_letters,
    '&': string.ascii_letters + '0123456789',
    '|': '|',
    '*': '*',
}

def prechod(pattern):
    prechodnyStav = {}
    aktualniStav = 0
    pozice = 0

    for char in pattern:
        if char == "#":
            for pat in patternMap.get(char, char):
                prechodnyStav[(aktualniStav, pat)] = aktualniStav + 1
            aktualniStav += 1
            pozice += 1
        elif char == "$":
            for pat in patternMap.get(char, char):
                prechodnyStav[(aktualniStav, pat)] = aktualniStav + 1
            aktualniStav += 1
            pozice += 1
        elif char == "&":
            for pat in patternMap.get(char, char):
                prechodnyStav[(aktualniStav, pat)] = aktualniStav + 1
            aktualniStav += 1
            pozice += 1
        elif char == "|":
            next_char = pattern[pozice + 1]
            for pat in patternMap.get(next_char, next_char):
                prechodnyStav[(aktualniStav - 1, pat)] = aktualniStav
            pozice += 2
        elif char == "*":
            prev_char = pattern[pozice - 1]
            for pat in patternMap.get(prev_char, prev_char):
                prechodnyStav[(aktualniStav - 1, pat)] = aktualniStav - 1
            aktualniStav -= 1
            pozice += 1
        else:
            prechodnyStav[(aktualniStav, char)] = aktualniStav + 1
            aktualniStav += 1
            pozice += 1

    koncovyStav = [aktualniStav]
    return prechodnyStav, koncovyStav


def ka(slovo, prechodnyStav, koncovyStav):
    aktualniStav = 0
    for znak in slovo:
        novyStav = prechodnyStav.get((aktualniStav, znak), None)
        if novyStav is None:
            return False
        else:
            aktualniStav = novyStav
    return aktualniStav in koncovyStav


def isValid(slovo, pattern):
    automat = prechod(pattern)
    return ka(slovo, *automat)


print(isValid('test@example.com', '&&*@&&*.$$$*'))
print(isValid('test@example', '&&*@&&*.$$$*'))
print(isValid('1234567890', '#########'))
print(isValid('123456789', '#########'))