#Count how many words in a list have length 5.

def word_len(w):
    num = 0
    for word in w:
        if len(word) == 5:
            num = num + 1
        else:
            pass
    return num
    
wordl = ['word', 'world', 'five', 'noahs']
print(word_len(wordl))