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
    return current_index


def compose_max(l):
    first_digit = argmax(l)
    if first_digit==len(l)-1:
        second_digit = argmax(l[:-1])
        return 10*l[second_digit] + l[first_digit]
    else:
        second_digit = argmax(l[first_digit+1:])
        return 10*l[first_digit] + l[first_digit+1+second_digit]


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
