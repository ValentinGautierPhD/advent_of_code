#!/usr/bin/env python3

def parse_input(f):
    fresh_ranges = []
    text = f.read()
    str_ranges, str_ids = text.split("\n\n")
    for line in str_ranges.split('\n'):
        a,b = line.split('-')
        fresh_ranges.append((int(a), int(b)))
    
    return fresh_ranges


def merge(ranges):
    ranges = sorted(ranges)
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # chevauchement ou contigu
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged
            

def main():
    input_file = "input.txt"
    with open("input.txt") as f:
        fresh_ranges = parse_input(f)

    merged = merge(fresh_ranges)
    total = sum(b - a + 1 for a,b in merged)
    print(total)
    
if __name__ == '__main__':
    main()

