from typing import List, Any
import os
import time

class IntermediateSorter:
    def __init__(self):
        self.intermediate_states = []

    def sort(self, collection: List[Any]) -> List[Any]:
        pass

    def get_intermediate_states(self):
        return self.intermediate_states

class SelectionSorter(IntermediateSorter):
    def sort(self, collection: List[Any]) -> List[Any]:
        for i in range(len(collection)):
            min_idx = i
            for j in range(i + 1, len(collection)):
                if collection[j] < collection[min_idx]:
                    min_idx = j
            collection[i], collection[min_idx] = collection[min_idx], collection[i]
            self.intermediate_states.append(collection.copy())
        return collection

class MergeSorter(IntermediateSorter):
    def sort(self, collection: List[Any]) -> List[Any]:
        if len(collection) <= 1:
            return collection
        
        mid = len(collection) // 2
        left = self.sort(collection[:mid])
        right = self.sort(collection[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[Any], right: List[Any]) -> List[Any]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        self.intermediate_states.append(result.copy())
        return result

class FileSorter:
    @staticmethod
    def sort_file(input_file: str, output_file: str, chunk_size: int = 1000, method: str = 'merge'):
        sorter = MergeSorter() if method == 'merge' else SelectionSorter()
        
        # Разделение файла на отсортированные чанки
        chunks = []
        with open(input_file, 'r') as f:
            while True:
                chunk = f.readlines(chunk_size)
                if not chunk:
                    break
                sorted_chunk = sorter.sort(chunk)
                chunks.append(sorted_chunk)
        
        # Слияние отсортированных чанков
        with open(output_file, 'w') as out:
            while chunks:
                smallest_chunks = [min(chunk) for chunk in chunks if chunk]
                smallest = min(smallest_chunks)
                out.write(smallest)
                chunk_index = smallest_chunks.index(smallest)
                chunks[chunk_index].pop(0)
                if not chunks[chunk_index]:
                    chunks.pop(chunk_index)

# Пример использования
if __name__ == "__main__":
    input_file = 'sort_benchmark.txt'
    output_file_merge = 'sorted_benchmark_merge.txt'
    output_file_selection = 'sorted_benchmark_selection.txt'
    
    # Сортировка слиянием
    start_time = time.time()
    FileSorter.sort_file(input_file, output_file_merge, method='merge')
    end_time = time.time()
    merge_time = end_time - start_time
    
    # Сортировка выбором
    start_time = time.time()
    FileSorter.sort_file(input_file, output_file_selection, method='selection')
    end_time = time.time()
    selection_time = end_time - start_time
    
    print(f"Файл {input_file} отсортирован методом слияния и сохранен как {output_file_merge}")
    print(f"Время выполнения (слияние): {merge_time:.2f} секунд")
    print(f"Файл {input_file} отсортирован методом выбора и сохранен как {output_file_selection}")
    print(f"Время выполнения (выбор): {selection_time:.2f} секунд")
