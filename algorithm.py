# Псевдокод для иллюстрации

import heapq
import os

def sort_and_save_chunk(chunk, chunk_num):
    chunk.sort()
    chunk_filename = f'chunk_{chunk_num}.txt'
    with open(chunk_filename, 'w') as f:
        for number in chunk:
            f.write(f"{number}\n")
    return chunk_filename

def split_file(input_file, chunk_size):
    chunk_filenames = []
    chunk = []
    chunk_num = 0
    with open(input_file, 'r') as f:
        for line in f:
            chunk.append(int(line.strip()))
            if len(chunk) * 8 >= chunk_size:  # Assume each int is 8 bytes
                chunk_filename = sort_and_save_chunk(chunk, chunk_num)
                chunk_filenames.append(chunk_filename)
                chunk = []
                chunk_num += 1
    if chunk:
        chunk_filename = sort_and_save_chunk(chunk, chunk_num)
        chunk_filenames.append(chunk_filename)
    return chunk_filenames

def merge_files(chunk_filenames, output_file):
    min_heap = []
    file_pointers = []
    for filename in chunk_filenames:
        f = open(filename, 'r')
        file_pointers.append(f)
        num = int(f.readline().strip())
        heapq.heappush(min_heap, (num, f))

    with open(output_file, 'w') as out:
        while min_heap:
            num, f = heapq.heappop(min_heap)
            out.write(f"{num}\n")
            line = f.readline().strip()
            if line:
                heapq.heappush(min_heap, (int(line), f))
    
    for f in file_pointers:
        f.close()

def external_sort(input_file, output_file, chunk_size):
    chunk_filenames = split_file(input_file, chunk_size)
    merge_files(chunk_filenames, output_file)
    for filename in chunk_filenames:
        os.remove(filename)

# Usage example
input_file = 'large_numbers.txt'
output_file = 'sorted_numbers.txt'
chunk_size = 100 * 1024 * 1024  # 100 MB
external_sort(input_file, output_file, chunk_size)
