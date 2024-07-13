

with open('write.txt','w') as f:

    f_contents = f.writelines('Hello\n')
    f_contents = f.writelines("This is Param")

    f.seek(0)
    s = "String"
    f_contents = f.writelines(s)
f.close()