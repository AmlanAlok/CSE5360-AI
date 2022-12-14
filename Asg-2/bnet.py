import sys

p_burglary = {
    't': 0.001
}
p_earthquake = {
    't': 0.002
}
p_alarm = {
    'tt': 0.95,
    'tf': 0.94,
    'ft': 0.29,
    'ff': 0.001
}
p_john_calls = {
    't': 0.90,
    'f': 0.05
}
p_mary_calls = {
    't': 0.70,
    'f': 0.01
}


class BayesianNetwork:
    def __init__(self):
        self.burglary = ''
        self.earthquake = ''
        self.alarm = ''
        self.john_calls = ''
        self.mary_calls = ''

    def print_val(self):
        print('B    E      A       M     J')
        print(self.burglary, self.earthquake, self.alarm, self.john_calls, self.mary_calls)

    def get_pb(self, x):

        if x:
            return p_burglary['t']
        else:
            return 1 - p_burglary['t']

    def get_pe(self, x):
        if x:
            return p_earthquake['t']
        else:
            return 1 - p_earthquake['t']

    def get_pa(self, x):
        return p_alarm[x]

    def get_pfc(self, x):
        return p_john_calls[x]

    def get_pmc(self, x):
        return p_mary_calls[x]

    def computeProbability(self, b, e, a, j, m):

        p_b = self.get_pb(b)
        p_e = self.get_pe(e)

        if b and e:
            p_a = self.get_pa('tt')
        elif b and not e:
            p_a = self.get_pa('tf')
        elif not b and e:
            p_a = self.get_pa('ft')
        elif not b and not e:
            p_a = self.get_pa('ff')

        if a:
            p_fc = self.get_pfc('t')
            p_mc = self.get_pmc('t')
        else:
            p_fc = self.get_pfc('f')
            p_mc = self.get_pmc('f')

        jp = p_b * p_e * p_a * p_fc * p_mc

        print(str(p_b) + ' * ' + str(p_e) + ' * ' + str(p_a) + ' * ' + str(p_fc) + ' * ' + str(p_mc) + ' = ' + str(jp))


def get_value(x):
    if x[1] == 't':
        return True
    elif x[1] == 'f':
        return False
    else:
        print('value is neither t nor f somewhere')
        exit(0)


def main():
    # print('Hi')
    bn = BayesianNetwork()
    bn.burglary = get_value(sys.argv[1])
    bn.earthquake = get_value(sys.argv[2])
    bn.alarm = get_value(sys.argv[3])
    bn.john_calls = get_value(sys.argv[4])
    bn.mary_calls = get_value(sys.argv[5])

    # print(bn)
    # bn.print_val()
    # print(b)
    bn.computeProbability(bn.burglary, bn.earthquake, bn.alarm, bn.john_calls, bn.mary_calls)


if __name__ == '__main__':
    main()
