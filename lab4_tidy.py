from os import write

input_file = './raw.csv'
output_file = './tidy.csv'

open(output_file, 'x')

with open(input_file, 'r') as f:
    lns = f.readlines()

for ln in lns:
    p = ln.find(' ack')
    q = ln.find(',', p)
    ln = ln[:q]

    p = ln.find(':')
    q = ln.find(',', p)
    ln = ln[:p] + ln[q:]

    p = ln.find('IP')
    if ln[p+3:p+6] == '10.':
        p = ln.find('IP')
        q = ln.find(',', p)
        ln = ln[:p] + ', O,' + ln[q+1:]
    if ln[p+3:p+6] == '140':
        p = ln.find('IP')
        q = ln.find(',', p)
        ln = ln[:p] + ', I,' + ln[q+1:]

    with open(output_file, 'a') as f:
        f.write(ln + '\n')
