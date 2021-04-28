def check_unique(word):
    str_word = {}
    word = word.lower()
    word = word.replace(" ", "")
    array_length = len(word)
    
    for i in range(array_length):
        if str_word.get(word[i]):
           str_word[word[i]] += 1
        else:
           str_word[word[i]] = 1
    
    res = 0
    for i in str_word:
        if str_word[i]%2==0:
            pass
        else:
            res += 1
    
    if res <= 1:
        return True
    
    return False


if __name__ == "__main__":
    input = "Tact Coa"
    result = check_unique(input)
    print(result)