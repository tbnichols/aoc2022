f = open('realinput.txt', 'r')
import functools
path = ["/"]
sizedict = {"/": 0}
for x in f:
    if "$" in x.strip():
        if x.strip() == "$ cd /":
            path = ["/"]
        elif x.strip() == "$ cd ..":
            path.pop(len(path)-1)
        elif x.strip() != "$ ls":
            print(x.strip())
            path.append(x.strip().split(" ")[2])
    else:
        if not ("dir" in x.strip()):
            size, filename = x.strip().split(" ")
            for i in range(len(path)+1):
                if i!=0:
                    print(path[:i])
                    print(x)
                    print(path)
                    print(sizedict)
                    sizedict[functools.reduce(lambda x, y: x +"/" + y,path[:i])] += int(size)
        else:
            print(functools.reduce(lambda x, y: x +"/" + y,path)+"/"+ x.strip().split(" ")[1])
            print(x)
            sizedict[functools.reduce(lambda x, y: x +"/" + y,path)+"/" + x.strip().split(" ")[1]]=0
total = 0
for y in sizedict.values():
    if y<100000:
        total+= y
print(total)