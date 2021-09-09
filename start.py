import argparse

parser = argparse.ArgumentParser(description='Description of your program')

parser.add_argument(
    '-a', '--action', help='Action type', required=True)
parser.add_argument(
    '-t', '--time', help='Description for bar argument', required=True)


args = parser.parse_args()


print (args.foo)

