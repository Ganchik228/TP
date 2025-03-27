import heapq
import pickle

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_tree(frequency):
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap) if heap else None

def build_codebook(root, current_code="", codebook=None):
    if codebook is None:
        codebook = {}
    
    if root is None:
        return
    
    if root.char is not None:
        codebook[root.char] = current_code
        return
    
    build_codebook(root.left, current_code + "0", codebook)
    build_codebook(root.right, current_code + "1", codebook)
    return codebook

def huffman_encode(data):
    if not data:
        return "", None
    frequency = build_frequency_dict(data)
    root = build_huffman_tree(frequency)
    codebook = build_codebook(root)
    encoded_data = ''.join([codebook[char] for char in data])
    return encoded_data, root

def huffman_decode(encoded_data, root):
    if not encoded_data:
        return ""
    current_node = root
    decoded_data = []
    
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root
    
    return ''.join(decoded_data)

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read().decode('utf-8')    
    encoded, tree = huffman_encode(data)
    padding = 8 - len(encoded) % 8
    encoded += '0' * padding
    bytes_data = bytes(int(encoded[i:i+8], 2) for i in range(0, len(encoded), 8))
    
    with open(output_file, 'wb') as f:
        pickle.dump((padding, tree), f)
        f.write(bytes_data)

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        padding, tree = pickle.load(f)
        bytes_data = f.read()
    
    encoded = ''.join(f'{byte:08b}' for byte in bytes_data)
    encoded = encoded[:-padding] if padding else encoded
    
    decoded = huffman_decode(encoded, tree)
    
    with open(output_file, 'wb') as f:
        f.write(decoded.encode('utf-8'))

if __name__ == "__main__":
    input_file = "m.qrf ael.elfeh sb.txt"
    output_file = "compresed.huf"
    out_decomp = "decompressed.txt"

    compress_file(input_file, output_file)
    print(f"File {input_file} compressed to {output_file}")
    decompress_file(output_file, out_decomp)
    print(f"File {output_file} decompressed to {out_decomp}")
