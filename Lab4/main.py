import time
from typing import List, Tuple

def read_fasta(file_path: str) -> str:
    """Читает FASTA файл и возвращает последовательность."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return ''.join(line.strip() for line in lines if not line.startswith('>'))

def naive_search(text: str, pattern: str) -> List[int]:
    """Наивный алгоритм поиска."""
    occurrences = []
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences.append(i)
    return occurrences

def bmh_search(text: str, pattern: str) -> List[int]:
    """Алгоритм Бойера-Мура-Хорспула."""
    occurrences = []
    n, m = len(text), len(pattern)
    if m > n:
        return occurrences

    # Предварительная обработка
    skip = {c: m for c in set(text)}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1

    # Поиск
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            occurrences.append(i - m + 1)
        i += skip.get(text[i], m)

    return occurrences

def find_longest_cat_sequence(genome: str) -> Tuple[str, List[int]]:
    """Находит самую длинную последовательность 'CAT..CAT' в геноме."""
    longest_seq = ""
    positions = []
    for i in range(1, len(genome) // 3 + 1):
        pattern = "CAT" * i
        occurrences = bmh_search(genome, pattern)
        if occurrences:
            longest_seq = pattern
            positions = occurrences
        else:
            break
    return longest_seq, positions

def main():
    genome = read_fasta("cat_genome.fasta")  # Замените на путь к вашему FASTA файлу

    # Поиск самой длинной последовательности CAT
    start_time = time.time()
    longest_seq, positions = find_longest_cat_sequence(genome)
    bmh_time = time.time() - start_time

    # Наивный поиск для сравнения
    start_time = time.time()
    naive_positions = naive_search(genome, longest_seq)
    naive_time = time.time() - start_time

    print(f"Самая длинная последовательность 'CAT': {longest_seq}")
    print(f"Длина последовательности: {len(longest_seq)}")
    print(f"Количество вхождений: {len(positions)}")
    print(f"Позиции вхождений: {positions}")
    print(f"Время выполнения БМХ: {bmh_time:.6f} секунд")
    print(f"Время выполнения наивного алгоритма: {naive_time:.6f} секунд")

if __name__ == "__main__":
    main()
