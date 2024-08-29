import heapq
from collections import defaultdict
import os

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

def compress(text):
    frequency = build_frequency_dict(text)
    huffman_tree = build_huffman_tree(frequency)
    
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)
    
    encoded_text = "".join(huffman_codes[char] for char in text)
    
    padding = 8 - len(encoded_text) % 8
    encoded_text += "0" * padding
    
    padded_info = "{0:08b}".format(padding)
    encoded_text = padded_info + encoded_text
    
    b = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        b.append(int(byte, 2))
    
    return bytes(b), huffman_codes

def decompress(encoded_data, huffman_codes):
    bit_string = ""

    for byte in encoded_data:
        bit_string += "{0:08b}".format(byte)

    padded_info = bit_string[:8]
    extra_padding = int(padded_info, 2)

    bit_string = bit_string[8:]
    encoded_text = bit_string[:-extra_padding]

    reversed_huffman_codes = {code: char for char, code in huffman_codes.items()}

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_huffman_codes:
            character = reversed_huffman_codes[current_code]
            decoded_text += character
            current_code = ""

    return decoded_text

def compress_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    compressed_data, huffman_codes = compress(text)
    
    with open(output_file, 'wb') as file:
        file.write(compressed_data)
    
    return huffman_codes


def decompress_file(input_file, output_file, huffman_codes):
    with open(input_file, 'rb') as file:
        compressed_data = file.read()
    
    decompressed_text = decompress(compressed_data, huffman_codes)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decompressed_text)


def calculate_compression_ratio(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    ratio = (1 - compressed_size / original_size) * 100
    return ratio


input_file = 'sgmcnmpiaxs.txt'
compressed_file = 'compressed.bin'
decompressed_file = 'decompressed.txt'

# Сжатие
huffman_codes = compress_file(input_file, compressed_file)

# Расчет степени сжатия
compression_ratio = calculate_compression_ratio(input_file, compressed_file)
print(f"Степень сжатия: {compression_ratio:.2f}%")

# Распаковка
decompress_file(compressed_file, decompressed_file, huffman_codes)

# Сравнение файлов
import difflib

with open(input_file, 'r', encoding='utf-8') as file1, open(decompressed_file, 'r', encoding='utf-8') as file2:
    diff = difflib.unified_diff(file1.readlines(), file2.readlines())

print("Разница между исходным и распакованным файлами:")
print(''.join(diff))