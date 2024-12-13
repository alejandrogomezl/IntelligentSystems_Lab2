import random

def mutate_binary_array(binary_array, mutation_rate):
    """
    Muta un array binario manteniendo el número exacto de 1 y 0 del original.

    :param binary_array: Lista binaria a mutar.
    :param mutation_rate: Tasa de mutación (valor entre 0 y 1).
    :return: Nuevo array binario mutado.
    """
    if not isinstance(mutation_rate, (int, float)):
        raise TypeError("mutation_rate debe ser un número (int o float)")
    if not (0 <= mutation_rate <= 1):
        raise ValueError("mutation_rate debe estar entre 0 y 1")

    # Contar el número de 1 y 0 en el array original
    ones_count = sum(binary_array)
    zeros_count = len(binary_array) - ones_count

    # Crear una lista con los índices de los 1 y los 0
    ones_indices = [i for i, x in enumerate(binary_array) if x == 1]
    zeros_indices = [i for i, x in enumerate(binary_array) if x == 0]

    # Calcular cuántos elementos mutar
    total_elements = len(binary_array)
    num_mutations = int(total_elements * mutation_rate)

    # Elegir índices aleatorios para mutar
    ones_to_flip = random.sample(ones_indices, min(len(ones_indices), num_mutations // 2))
    zeros_to_flip = random.sample(zeros_indices, min(len(zeros_indices), num_mutations - len(ones_to_flip)))

    # Crear el nuevo array mutado
    mutated_array = binary_array[:]

    # Mutar los índices seleccionados
    for index in ones_to_flip:
        mutated_array[index] = 0
    for index in zeros_to_flip:
        mutated_array[index] = 1

    # Asegurar que el número de 1 y 0 es igual al original
    assert sum(mutated_array) == ones_count, "El número de 1 no coincide con el original"

    return mutated_array

# Ejemplo de uso
binary_array =  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
mutation_rate = 0.1

for i in range(10000):
    mutated_array = mutate_binary_array(binary_array, mutation_rate)
    print("Original array:", sum(binary_array))
    print("Mutated array:", sum(mutated_array))