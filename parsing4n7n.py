


with open('4n7n.pdb', 'r') as rf:
    with open('ATOMlines.txt', 'w') as wf:

     for line in rf:
        if line.startswith('ATOM'):
            print(line)
            wf.write(line)

