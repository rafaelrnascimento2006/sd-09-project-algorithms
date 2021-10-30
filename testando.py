def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return False
    if (
        first_string[0] == second_string[0]
        and first_string[-1] == second_string[-1]
    ):
        return True
    return True


f = "xablau"
s = "balaxu"

print(is_anagram(f, s))
