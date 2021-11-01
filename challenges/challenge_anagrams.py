def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
# https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html
#     if(not first_string) or (not second_string):
#         return False

#     if len(first_string) != len(second_string):
#         return False

#     f_counter = 0

#     while f_counter < len(first_string) and True:
#         s_counter = 0
#         anagram = False
#         while s_counter < len(list(second_string)) and not anagram:
#             if first_string[f_counter] == list(second_string)[s_counter]:
#                 return True
#             else:
#                 s_counter = s_counter + 1

#         if anagram:
#             list(second_string)[s_counter] = None
#         else:
#             return False

#         f_counter = f_counter + 1
