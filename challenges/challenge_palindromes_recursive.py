def is_palindrome_recursive(word, low_index, high_index):
    is_palidrome = True
    if low_index < len(word) and high_index < len(word):
        if (low_index != high_index) and (word[low_index] == word[high_index]):
            if is_palindrome_recursive(word, low_index + 1, high_index - 1):
                is_palidrome = True
            else:
                is_palidrome = False 
        else:
            if word[low_index] != word[high_index] or len(word) == 0:
                is_palidrome = False
    if (word == ''):
        is_palidrome = False
    return is_palidrome

if __name__ == "__main__":
    words = 'hahh'
    print(is_palindrome_recursive(words, 0, len(words) - 1))