def words(index):
    index = index.strip().split()
    words = {}
    for word in index:
        try:
            word = int(word)
        except ValueError:
            pass
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words
