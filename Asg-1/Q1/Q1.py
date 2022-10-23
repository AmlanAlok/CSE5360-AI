import sys
from collections import deque

TO = 'to'
FROM = 'from'
DISTANCE = 'distance'


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
            d[first_city].append([second_city, distance, first_city])
        else:
            d[first_city] = [[second_city, distance, first_city]]

        if second_city in d:
            d[second_city].append([first_city, distance, second_city])
        else:
            d[second_city] = [[first_city, distance, second_city]]

    return d


def add_successors_to_fringe(fringe, successors):
    def key_col_value(t):
        return t[DISTANCE]

    for arr in successors:
        # fringe.append(arr)
        fringe.append({FROM: arr[2],
                       TO: arr[0],
                       DISTANCE: arr[1]})

    return deque(sorted(fringe, key=key_col_value))


def uniform_cost_search_2(origin, destination, map_dict):
    fringe = deque()
    fringe.append([origin, 0.0, ''])

    visited = []
    route_traversed = []
    expanded_arr = []
    popped = 0
    generated = 0
    expanded = 0

    route_stack = deque()

    while len(fringe) > 0:
        fringe_element = fringe.popleft()
        current_location = fringe_element[0]
        popped += 1
        route_traversed.append(current_location)

        if current_location not in visited:

            visited.append(current_location)

            if current_location == destination:
                print('Found :', destination)
                # print('Route =', route_traversed)
                print('Nodes Popped:', popped)
                print('Nodes Expanded:', expanded)
                print('Nodes Generated:', generated)
                print('Distance:')
                break

            successors = map_dict[current_location]
            generated += len(successors)
            fringe = add_successors_to_fringe(fringe, successors)
            expanded += 1
            expanded_arr.append(current_location)

    print('ucs')


def route_tracker(route_traversed, origin, curr_fringe_element):
    from_loc = curr_fringe_element[FROM]
    dist = curr_fringe_element[DISTANCE]

    final_path_arr = [curr_fringe_element]

    for i in range(len(route_traversed) - 1, -1, -1):
        arr = route_traversed[i]

        if from_loc == origin:
            return final_path_arr, dist
        if from_loc == arr[TO]:
            dist += arr[DISTANCE]
            from_loc = arr[FROM]
            final_path_arr.append(arr)


def uniform_cost_search(origin, destination, map_dict):
    fringe = deque()
    # fringe.append([origin, 0.0, ''])
    fringe.append({FROM: '',
                   TO: origin,
                   DISTANCE: 0.0})

    visited = []
    route_traversed = []
    expanded_arr = []
    popped = 0
    generated = 0
    expanded = 0

    route_stack = deque()

    while len(fringe) > 0:
        fringe_element = fringe.popleft()
        current_location = fringe_element[TO]
        popped += 1
        # route_traversed.append(current_location)
        # route_traversed.append(fringe_element)

        if current_location not in visited:
            route_traversed.append(fringe_element)
            visited.append(current_location)

            # if len(route_stack) > 1:
            #     if fringe_element[TO] == route_stack[-1][FROM]:
            #         route_stack.pop()
            #     else:
            #         route_stack.append(fringe_element)
            # else:
            #     route_stack.append(fringe_element)

            if current_location == destination:
                print('Found :', destination)
                x, total_distance = route_tracker(route_traversed, origin, fringe_element)
                # print('Route =', route_traversed)
                print('Nodes Popped:', popped)
                print('Nodes Expanded:', expanded)
                print('Nodes Generated:', generated)
                print('Distance:', total_distance, ' km')

                break

            successors = map_dict[current_location]
            generated += len(successors)
            fringe = add_successors_to_fringe(fringe, successors)
            expanded += 1
            expanded_arr.append(current_location)
        # else:
        #     if len(route_stack) > 1:
        #         if fringe_element[TO] == route_stack[-1][FROM]:
        #             route_stack.pop()

    print('ucs')


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

    uniform_cost_search(origin, destination, map_dict)

    # if len(sys.argv) == 4:
    #     '''Uninformed Search'''
    #
    # elif len(sys.argv) == 5:
    #     '''Informed Search'''


if __name__ == "__main__":
    main()

#   python3 Q1.py input1.txt Bremen Kassel
