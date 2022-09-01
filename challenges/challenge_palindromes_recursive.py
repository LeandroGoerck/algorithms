def is_palindrome_recursive(word, low_index, high_index):

    if word == "":
        return False
    
    if (word[low_index] != word[high_index]):
        return False

    if len(word) <= 2:
        return True

    wd = word[1:-1]
    return is_palindrome_recursive(wd, 0, len(wd)-1)
