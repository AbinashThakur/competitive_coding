def check_unique(str):
    str_length = len(str)
    act_length = 13
    str_new = ""
    for i in range(13):
        str_new += str[i]
    
    str_new = str_new.replace(" ", "%20")
    return str_new


if __name__ == "__main__":
    input = "Mr John Smith   "
    result = check_unique(input)
    print(result)