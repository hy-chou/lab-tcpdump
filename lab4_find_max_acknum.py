from os import write

input_file = './lab4_data_tidy.csv'
output_file = input_file[:-9] + '_acknum.csv'

open(output_file, 'x')

max = 0
with open(input_file, 'r') as fi:
    for line in fi:
        ln = line

        p = ln.find(' ack')
        if p != -1:
            ack_num = int(ln[p+4:-1])
            if ack_num > max:
                max = ack_num
            with open(output_file, 'a') as fo:
                fo.write(str(ack_num) + '\n')
print(max)
