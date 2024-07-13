

with open('read.txt','r') as f:

    ## this works for small files as you might want to read everything in a small file
    # print(f_contents)
    ## printing  a line
    f_contents  = f.read(10)
    print(f_contents,end='\n')
    f.seek(20)
    f_contents = f.read(10)

    print(f_contents)
    f_contents = f.readline()
    print(f.tell()) ## it tells the length
    
    print(f_contents)
f.close() # it's improtant to close the files and having this function as it can run out of memory
