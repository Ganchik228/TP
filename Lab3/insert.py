class InsertionSort:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def read_file(self):
        with open(self.filename, 'r') as file:
            self.lines = file.readlines()

    def sort(self):
        for i in range(1, len(self.lines)):
            key = self.lines[i]
            j = i - 1
            while j >= 0 and self.lines[j] > key:
                self.lines[j + 1] = self.lines[j]
                j -= 1
            self.lines[j + 1] = key

    def write_sorted_file(self, output_filename):
        with open(output_filename, 'w') as file:
            file.writelines(self.lines)

class TrackedInsertionSort(InsertionSort):
    def __init__(self, filename):
        super().__init__(filename)
        self.steps = []

    def sort(self):
        for i in range(1, len(self.lines)):
            key = self.lines[i]
            j = i - 1
            while j >= 0 and self.lines[j] > key:
                self.lines[j + 1] = self.lines[j]
                j -= 1
            self.lines[j + 1] = key
            self.steps.append(self.lines[:])  # Сохраняем копию массива на каждом шаге

class VisualizedInsertionSort:
    def __init__(self, filename):
        self.sorter = TrackedInsertionSort(filename)

    def visualize(self):
        self.sorter.read_file()
        self.sorter.sort()
        
        print("Промежуточные шаги:")
        for i, step in enumerate(self.sorter.steps[:5], 1):  # Показываем первые 5 шагов
            print(f"Шаг {i}:")
            print(''.join(step[:10]))  # Показываем первые 10 строк каждого шага
        
        self.sorter.write_sorted_file("Lab3/sorted_benchmark.txt")

# Пример использования
if __name__ == "__main__":
    vis_sorter = VisualizedInsertionSort("Lab3/sort_benchmark.txt")
    vis_sorter.visualize()
