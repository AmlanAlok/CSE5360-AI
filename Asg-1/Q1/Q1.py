import sys


def clean_data(line):
    return line.replace('\n', '').split(' ')


def read_input(filename):
    with open(filename, 'r') as f:
        input_data = f.readlines()
        clean_input = list(map(clean_data, input_data))
        f.close()
    return clean_input


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

    if len(sys.argv) == 4:
        '''Uninformed Search'''

    elif len(sys.argv) == 5:
        '''Informed Search'''


if __name__ == "__main__":
    main()

#   python3 Q1.py input1.txt Bremen Kassel
