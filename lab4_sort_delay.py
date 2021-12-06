from heapq import heapify, heappop

input_file = './lab4_delay.csv'
output_file = './lab4_delay_sorted.csv'

h = []
with open(input_file, 'r') as f:
    for line in f:
        h.append(float(line[11:]))

heapify(h)

with open(output_file, 'x') as f:
    for i in range(len(h)):
        f.write(str(heappop(h)) + '\n')
