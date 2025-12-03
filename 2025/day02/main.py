#!/usr/bin/env python3

def parse_input(f):
    ranges = f.split(",")
    return ranges

def parse_ids(ids_range):
    splitted = ids_range.split("-")
    assert len(splitted) == 2

    id_min, id_max = int(splitted[0]), int(splitted[1])
    return range(id_min, id_max+1)

def is_invalid(product_id):
    str_id = str(product_id)
    length = len(str_id)
    if length%2==0:
        return str_id[:length//2]==str_id[length//2:]
    else:
        return False
    
def main():
    input_file = "input.txt"
    invalids = []
    with open(input_file) as f:
        parsed = parse_input(f.read()[:-1])
        for ids_range in parsed:
            for product_id in parse_ids(ids_range):
                if is_invalid(product_id):
                    invalids.append(product_id)
    print(sum(invalids))
                    
if __name__ == '__main__':
    main()
