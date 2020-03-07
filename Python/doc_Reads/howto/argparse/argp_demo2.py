import argparse

parser = argparse.ArgumentParser(description='Calculate X to the power of Y.')

parser.add_argument('x', help='The base.', type=int)
parser.add_argument('y', help='The exponent.', type=int)
parser.add_argument('-v', '--verbosity',
                    action='count',
                    default=0,
                    help='For different amount of -v used, result format will be different.')

parser.add_argument('-t', help='Test the value if -t is not passed to the program.', action='store_true')

args = parser.parse_args()

result = args.x ** args.y

print(args.t)

if args.verbosity >= 2:
    print('running \'{}\''.format(__file__))
if args.verbosity >= 1:
    print('{}^{} = {}'.format(args.x, args.y, result))
else:
    print(result)