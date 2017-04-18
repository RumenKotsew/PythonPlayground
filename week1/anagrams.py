def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    for i in word1:
        if i in word2:
            word1 = word1.replace(i, "", 1)
            word2 = word2.replace(i, "", 1)
    if word1 == "" and word2 == "":
        return True
    else:
        return False
