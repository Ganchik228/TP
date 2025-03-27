def gorner_scheme(text):
    result = ord(text[0])
    base = 31
    for i in range(len(text)-1):
        result = result * base + ord(text[i+1])
    return result

def calculate_hash(text):
    q = 2147483647
    return gorner_scheme(text) % q

import time

def search_text(text, sub_text):
    start_time = time.time()
    base = 31
    q = 2147483647
    sub_hash = calculate_hash(sub_text)
    m = len(sub_text)
    current_hash = calculate_hash(text[0:m])
    i = 0
    while True:
        if sub_hash == current_hash:
            if sub_text == text[i:i+m]:
                return i 
        if i + m >= len(text):
            break
        current_hash = ((current_hash - ord(text[i]) * base ** (m-1)) * base + ord(text[i + m])) % q
        i = i + 1
    end_time = time.time()
    print(f"Рабин: {end_time - start_time:.6f} секунд")
    return None

def simple_search(text, sub_text):
    start_time = time.time()
    n = len(text)
    m = len(sub_text)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == sub_text[j]:
            j += 1
        if j == m:
            return i
    end_time = time.time()
    print(f"Простой поиск: {end_time - start_time:.6f} секунд")
    return None

with open("qlgoaxgwen gr,sdz.txt", "r") as file:
    text = file.read()
sub_text = "tdm"
print("Рабин", search_text(text, sub_text))
print("Простая:", simple_search(text, sub_text))
