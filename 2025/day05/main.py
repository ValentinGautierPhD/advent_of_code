#!/usr/bin/env python3

def parse_input(f):
    fresh_ranges = []
    text = f.read()
    str_ranges, str_ids = text.split("\n\n")
    for line in str_ranges.split('\n'):
        a,b = line.split('-')
        fresh_ranges.append((int(a), int(b)))
    fresh_ids = [int(ingredient_id) for ingredient_id in str_ids.split('\n')[:-1]]
    
    return fresh_ranges, fresh_ids


def is_fresh(ingredient_id, fresh_ranges):
    for fresh_range in fresh_ranges:
        if fresh_range[0] <= ingredient_id <= fresh_range[1]:
            return True
    return False


def main():
    input_file = "input.txt"
    count = 0
    with open(input_file) as f:
        fresh_ranges, fresh_ids = parse_input(f)
    for ingredient_id in fresh_ids:
        if is_fresh(ingredient_id, fresh_ranges):
            count += 1
    print(count)
        

if __name__ == '__main__':
    main()
