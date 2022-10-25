import sys
from collections import deque

TO = 'to'
FROM = 'from'
DISTANCE = 'distance'
FN = 'fn'
GN = 'gn'


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
        ''' To avoid edge case scenario which might cause infinite loop'''
        if distance == 0:
            distance = 0.01

        if first_city in d:
            d[first_city].append([second_city, distance, first_city])
        else:
            d[first_city] = [[second_city, distance, first_city]]

        if second_city in d:
            d[second_city].append([first_city, distance, second_city])
        else:
            d[second_city] = [[first_city, distance, second_city]]

    return d


def add_successors_to_fringe(fringe, successors, fringe_element):
    def key_col_value(t):
        # return t[DISTANCE]
        return t[GN]

    for arr in successors:
        fringe.append({FROM: arr[2],
                       TO: arr[0],
                       DISTANCE: arr[1],
                       GN: arr[1] + fringe_element[GN]})

    return deque(sorted(fringe, key=key_col_value))


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
    fringe.append({FROM: '',
                   TO: origin,
                   DISTANCE: 0.0,
                   GN: 0.0})

    visited, route_traversed, expanded_arr = [], [], []
    popped, generated, expanded = 0, 1, 0

    while len(fringe) > 0:
        fringe_element = fringe.popleft()
        current_location = fringe_element[TO]
        popped += 1

        if current_location not in visited:
            route_traversed.append(fringe_element)
            visited.append(current_location)

            if current_location == destination:
                route_path, total_distance = route_tracker(route_traversed, origin, fringe_element)
                print('Nodes Popped:', popped)
                print('Nodes Expanded:', expanded)
                print('Nodes Generated:', generated)
                print('Distance:', total_distance, ' km')
                for i in range(len(route_path) - 1, -1, -1):
                    arr = route_path[i]
                    print(arr[FROM], 'to', arr[TO], ',', arr[DISTANCE], 'km')
                return

            successors = map_dict[current_location]
            generated += len(successors)
            fringe = add_successors_to_fringe(fringe, successors, fringe_element)
            expanded += 1
            expanded_arr.append(current_location)

    print('Nodes Popped:', popped)
    print('Nodes Expanded:', expanded)
    print('Nodes Generated:', generated)
    print('Distance: infinity')
    print('Route:\nNone')


def organise_heuristics(input_data):
    d = {}

    for record in input_data:
        city, distance = record[0], float(record[1])
        d[city] = distance
    return d


def add_successors_to_a_star_fringe(fringe, successors, heuristics_dict):
    def key_col_value(t):
        return t[FN]

    for arr in successors:
        from_city, to_city, dist = arr[2], arr[0], arr[1]
        fringe.append({FROM: from_city,
                       TO: to_city,
                       DISTANCE: dist,
                       FN: dist + heuristics_dict[to_city]})

    return deque(sorted(fringe, key=key_col_value))


def a_start_search(origin, destination, map_dict, heuristics_dict):
    fringe = deque()
    fringe.append({FROM: '',
                   TO: origin,
                   DISTANCE: 0.0})

    visited, route_traversed, expanded_arr = [], [], []
    popped, generated, expanded = 0, 1, 0

    while len(fringe) > 0:
        fringe_element = fringe.popleft()
        current_location = fringe_element[TO]
        popped += 1

        if current_location not in visited:
            route_traversed.append(fringe_element)
            visited.append(current_location)

            if current_location == destination:
                route_path, total_distance = route_tracker(route_traversed, origin, fringe_element)
                print('Nodes Popped:', popped)
                print('Nodes Expanded:', expanded)
                print('Nodes Generated:', generated)
                print('Distance:', total_distance, ' km')
                for i in range(len(route_path) - 1, -1, -1):
                    arr = route_path[i]
                    print(arr[FROM], 'to', arr[TO], ',', arr[DISTANCE], 'km')
                return

            successors = map_dict[current_location]
            generated += len(successors)
            fringe = add_successors_to_a_star_fringe(fringe, successors, heuristics_dict)
            expanded += 1
            expanded_arr.append(current_location)

    print('Nodes Popped:', popped)
    print('Nodes Expanded:', expanded)
    print('Nodes Generated:', generated)
    print('Distance: infinity')
    print('Route:\nNone')


def main():
    print('Q1')
    # print(sys.argv)

    # input_filename = sys.argv[1]
    # origin = sys.argv[2]
    # destination = sys.argv[3]

    input_filename = 'input1.txt'

    origin = 'Bremen'
    destination = 'Kassel'
    # origin = 'London'
    # destination = 'Kassel'

    input_data = read_input(input_filename)
    map_dict = organise_map(input_data)

    uniform_cost_search(origin, destination, map_dict)
    print('----------')
    origin = 'London'
    destination = 'Kassel'
    # uniform_cost_search(origin, destination, map_dict)

    heuristics_filename = 'h_kassel.txt'
    heuristics_data = read_input(heuristics_filename)

    heuristics_dict = organise_heuristics(heuristics_data)
    # a_start_search(origin, destination, map_dict, heuristics_dict)

    # if len(sys.argv) == 4:
    #     '''Uninformed Search'''
    #     uniform_cost_search(origin, destination, map_dict)
    #
    # elif len(sys.argv) == 5:
    #     '''Informed Search'''
    print('END')


if __name__ == "__main__":
    main()

#   python3 Q1.py input1.txt Bremen Kassel
