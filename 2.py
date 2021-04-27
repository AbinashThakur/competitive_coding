def check_unique(word1, word2):
    str_word = {}
    array_length1 = len(word1)
    array_length2 = len(word2)
    
    if array_length1 != array_length2:
        return False
    
    for i in range(array_length1):
        if str_word.get(word1[i]):
            str_word[word1[i]] += 1
        else:
            str_word[word1[i]] = 1
    
    for i in range(array_length2):
        if str_word.get(word2[i]):
            str_word[word2[i]] -= 1
            if str_word[word2[i]] == 0:
                str_word.pop(word2[i])
        else:
            return False
    
    if not bool(str_word):
        return True
    
    return True


if __name__ == "__main__":
    input1 = "BorrowOrRob"
    input2 = "OrRobBorrow"
    result = check_unique(input1, input2)
    print(result)