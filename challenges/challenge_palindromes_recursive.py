def is_palindrome_recursive(word, low_index, high_index):
    if low_index != high_index and word[low_index] == word[high_index]:
        is_palindrome_recursive(word, low_index + 1, high_index - 1)
        return True


if __name__ == "__main__":
    print(is_palindrome_recursive('ana'))