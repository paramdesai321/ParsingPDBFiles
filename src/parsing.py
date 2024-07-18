import sys


if len(sys.argv) < 2:
    print("Usage: python filename.py <variable>")
    sys.exit(1)


variable = sys.argv[1]


with open(f'{variable}.pdb', 'r') as rf:
    with open(f'ATOMlines{variable}.txt', 'w') as wf:

     for line in rf:
        if line.startswith('ATOM'):
            print(line)
            wf.write(line)