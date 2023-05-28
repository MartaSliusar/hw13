def popular_words(text, words):
    dct = {}
    text = text.lower()
    text = text.split(' ')
    for el in words:
        dct[el] = text.count(el)
    return dct
