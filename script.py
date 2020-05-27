import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--n', action='append', type=int)

parser.add_argument('--sum', action='store_true')
parser.add_argument('--mult', action='store_true')

args = parser.parse_args()

if(args.sum):
    print(sum(args.n))
elif (args.mult):
    acc = 1
    for n in args.n:
        acc *= n
    print(acc)
