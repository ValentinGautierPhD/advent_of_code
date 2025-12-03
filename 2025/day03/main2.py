#!/usr/bin/env python3

def parse_line(line):
    return [int(digit) for digit in line]


def argmax(l):
    current_index = 0
    current_max = l[0]
    for i in range(len(l)):
        if l[i]>current_max:
            current_index=i
            current_max=l[i]
    return current_index, current_max


def compose_max(l):
    current_list = l
    current_res = ""
    for i in reversed(range(1,12)):
        max_index, max_value = argmax(current_list[:-i])
        current_list = current_list[max_index+1:]
        current_res = current_res + str(max_value)

    # Last iteration because current_list[:0] is empty
    _, max_value = argmax(current_list)
    current_res = current_res + str(max_value)

    return int(current_res)
    

def main():
    input_file = "input.txt"
    total = 0
    with open(input_file) as f:
        for line in f:
            l = parse_line(line[:-1])
            add = compose_max(l)
            total += add

    print(total)
            
if __name__ == '__main__':
    main()
