

with open('read.txt','r') as rf:
    with open('write.txt','w') as wf:

        for line in rf:
            rf_contenst = rf.readline(4)
            print(rf_contenst)
            s = str(rf_contenst)
            print(s)
            if (s=='This'):
                print("True")
            else:
                print("False")

    wf.close()
rf.close()


