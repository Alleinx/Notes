import argparse

parser = argparse.ArgumentParser()

parser.add_argument('x', help='The base.', type=int)
parser.add_argument('y', help='The exponent.', type=int)
parser.add_argument('-v', '--verbosity',
                    action='count',
                    default=0,
                    help='For different amount of -v used, result format will be different.')

args = parser.parse_args()

result = args.x ** args.y

if args.verbosity >= 2:
    print('{} to the power of {} equals to {}'.format(args.x, args.y, result))
elif args.verbosity >= 1:
    print('{}^{} = {}'.format(args.x, args.y, result))
else:
    print(result)