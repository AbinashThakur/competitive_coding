def check_unique(word):
    str_word = {}
    array_length = len(word)
    for i in range(array_length):
        val = word[i]
        if str_word.get(val):
            return False
        else:
            str_word[val] = 1
    return True


if __name__ == "__main__":
    input = "BorrowOrRob"
    result = check_unique(input)
    print(result)