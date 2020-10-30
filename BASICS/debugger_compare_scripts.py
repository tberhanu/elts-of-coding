def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())


    with open(File2,'r') as f:
        e=set(f.readlines())

    open('scripts_diff.py', 'w').close() #Create the file

    with open('scripts_diff.py', 'a') as f:
        for line in list(d-e):
           f.write(line)
if __name__ == "__main__":
    compare("script1.py", "script2.py")