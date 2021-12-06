from os import write

input_file = './tidy.csv'
output_file = './nof.csv'

open(output_file, 'x')

with open(input_file, 'r') as f:
    lns = f.readlines()

i = 0
# ack_list = [-1]
for i in range(len(lns)):
    if lns[i].find(' I,') == -1:
        continue

    p = lns[i].find(' ack ')
    if p == -1:
        continue
    ack_num = lns[i][p+5:-1]

    o = i - 1
    while o >= 0:
        #     # if j == ack_list[0]:
        #     # break
        #     # if i - j > 16:
        #     # break

        if lns[o].find(' O,') == -1:
            o -= 1
            continue

        p = lns[o].find('seq')
        p = lns[o].find(':', p)
        q = lns[o].find(',', p)
        if lns[o].find(ack_num, p, q) == -1:
            o -= 1
            continue

        # ack_list.append(j)
        # if len(ack_list) > 250:
        # ack_list.pop(0)

        ack_sec = float(lns[i][:17])
        seq_sec = float(lns[o][:17])
        del_ms = (ack_sec - seq_sec) * 1000
        with open(output_file, 'a') as f:
            f.write(lns[o][8:17] + ', ' + str(del_ms) + '\n')
        break
