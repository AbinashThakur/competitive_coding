def check_unique(word1, word2):
    str_word = {}
    array_length1 = len(word1)
    array_length2 = len(word2)

    if array_length1 == array_length2:
        return check_onereplace(word1, word2)
    elif array_length1+1 == array_length2:
        return check_oneremove(word1, word2)
    elif array_length1 == array_length2+1:
        return check_oneinsert(word1, word2)
    else:
        return False

def check_oneinsert(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    str_word = {}
    count = 0
    for i in range(length1):
        if str_word.get(word1[i]):
            str_word[word1[i]] += 1
        else:
            str_word[word1[i]] = 1
    
    for i in range(length2):
        if str_word.get(word2[i]):
            str_word[word2[i]] -= 1
        
        if str_word[word2[i]] == 1:
                count += 1
    
    print(count)
    if count <=1:
        return True
    else:
        return False

def check_oneremove(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    str_word = {}
    count = 0
    for i in range(length1):
        if str_word.get(word1[i]):
            str_word[word1[i]] += 1
        else:
            str_word[word1[i]] = 1
    
    for i in range(length2):
        if str_word.get(word2[i]):
            str_word[word2[i]] -= 1
        else:
            str_word[word2[i]] = 1
        
        if str_word[word2[i]] == 1:
            count += 1
    
    print(count)
    if count <=1:
        return True
    else:
        return False

def check_onereplace(word1, word2):
    length1 = len(word1)
    length2 = len(word2)
    str_word = {}
    count = 0
    for i in range(length1):
        if str_word.get(word1[i]):
            str_word[word1[i]] += 1
        else:
            str_word[word1[i]] = 1
    
    for i in range(length2):
        if str_word.get(word2[i]):
            str_word[word2[i]] -= 1
        else:
            str_word[word2[i]] = 1
        
        if str_word[word2[i]] == 1:
            count += 1
    print(str_word)
    print(count)
    if count <=1:
        return True
    else:
        return False



if __name__ == "__main__":
    input1 = "pale"
    input2 = "bake"
    result = check_unique(input1, input2)
    print(result)