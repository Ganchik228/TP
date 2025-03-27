def insertion_sort(arr) -> list:
    for i in range(1, len(arr)):
        paste_element = arr[i]
        while i > 0 and arr[i-1] > paste_element:
            arr[i] = arr[i-1]
            i = i - 1
        arr[i] = paste_element
    return arr

def sort_file(input_file: str, output_file:str | None):
    with open(input_file, 'r') as file:
        lines = file.readlines()        
        data = [line.strip() for line in lines]
        sorted_data = insertion_sort(data)
        with open(output_file, 'w') as file:
            for item in sorted_data:
                file.write(f"{item}\n")
        
if __name__ == "__main__":
    sort_file("sort_benchmark.txt", "sorted_insert_data.txt")
