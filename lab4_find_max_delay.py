input_file = './nof.csv'

min = 20000
max = 0
with open(input_file, 'r') as f:
    for line in f:
        p = line.find(',')
        if p == -1:
            continue

        delay = float(line[p+2:-1])
        print(delay)
        if delay > max:
            max = delay
        elif delay < min:
            min = delay
print(min, max)
