from challenges.helpers.merge_sort import mergesort


def validate_length_or_empty(nums):
    return (len(nums) < 2) or nums is None


def validate_not_number_or_not_positive_number(numero):
    return type(numero) is not int or numero < 1


def validate_number_duplicate(numero_duplicado):
    if numero_duplicado == 0:
        return False
    numero_duplicado


def find_duplicate(nums):
    """1º validações sem nullo e com menos de 2 valores
    2º ordenação com validações, se é numero, e se já existe
    se é negativo, Se numero repetido, tiver mais de um, retorna false
    se ao percorrer toda a lista o numero que tiver repetido, é
    retornado
    Possibilidades: Array vazio e array duplicados, o todos vai receber se não
    existir, se já existir, guarda na variavel , continua fazendo para validar
    se não tem negativos ou string
    """
    if validate_length_or_empty(nums):
        return False
    mergesort(nums)
    number_duplicate = 0
    for index in range(0, len(nums)):
        if validate_not_number_or_not_positive_number(nums[index]):
            return False
        if nums[index] == nums[index - 1]:
            number_duplicate = nums[index]
            return number_duplicate
    return False


# print(find_duplicate([2, 5, 8, 4, 2, 1]))
