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

    if (len(nums) < 2) or nums is None:
        return False
    array_completo = []
    numero_duplicado = 0

    for numero in nums:
        if type(numero) is not int or numero < 1:
            return False
        if numero not in array_completo:
            array_completo.append(numero)
        elif numero != numero_duplicado:
            numero_duplicado = numero
    if numero_duplicado == 0:
        return False
    return numero_duplicado


# print(find_duplicate([2, 5, 8, 4, 2, 1]))
