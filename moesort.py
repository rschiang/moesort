import requests

cache = {}

def get_definition(char):
    if char not in cache:
        response = requests.get('https://www.moedict.tw/uni/{}'.format(char))
        cache[char] = response.json()
    return cache[char]

def radical_sort(arr):
    def radical_key(chars):
        buf = ''
        for char in chars:
            defs = get_definition(char)
            buf += '{:02d}'.format(defs.get('stroke_count', 0))
        return buf
    return sorted(arr, key=radical_key)

def bopomofo_sort(arr):
    def bopomofo_key(chars):
        buf = ''
        for char in chars:
            defs = get_definition(char)
            if 'heteronyms' in defs:
                buf += defs['heteronyms'][0]['bopomofo'].ljust(4)
            else:
                buf += ' ' * 4
        return buf
    return sorted(arr, key=bopomofo_key)
