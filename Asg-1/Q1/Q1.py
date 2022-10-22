import sys


def clean_data(line):
    return line.replace('\n', '').split(' ')


def read_input(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()

        ''' Remove END OF INPUT line '''
        input_data.pop()

        clean_input = list(map(clean_data, input_data))
        f.close()
    return clean_input


def organise_map(input_data):
    d = {}

    for record in input_data:
        first_city, second_city, distance = record[0], record[1], float(record[2])

        if first_city in d:
            d[first_city].append([second_city, distance])
        else:
            d[first_city] = [[second_city, distance]]

        if second_city in d:
            d[second_city].append([first_city, distance])
        else:
            d[second_city] = [[first_city, distance]]

    return d


def main():
    print('Q1')
    # print(sys.argv)

    # input_filename = sys.argv[1]
    # origin = sys.argv[2]
    # destination = sys.argv[3]

    input_filename = 'input1.txt'
    origin = 'Bremen'
    destination = 'Kassel'

    input_data = read_input(input_filename)

    map_dict = organise_map(input_data)

    if len(sys.argv) == 4:
        '''Uninformed Search'''

    elif len(sys.argv) == 5:
        '''Informed Search'''


if __name__ == "__main__":
    main()

#   python3 Q1.py input1.txt Bremen Kassel
