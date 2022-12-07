f = open('realinput.txt', 'r')
import functools
path = ["/"]
sizedict = {"/": 0}
totaldisk = 70000000

input()
for x in f:
    if "$" in x.strip():
        if x.strip() == "$ cd /":
            path = ["/"]
        elif x.strip() == "$ cd ..":
            path.pop(len(path)-1)
        elif x.strip() != "$ ls":
            path.append(x.strip().split(" ")[2])
    else:
        if not ("dir" in x.strip()):
            size, filename = x.strip().split(" ")
            for i in range(len(path)+1):
                if i!=0:
                    sizedict[functools.reduce(lambda x, y: x +"/" + y,path[:i])] += int(size)
        else:
            sizedict[functools.reduce(lambda x, y: x +"/" + y,path)+"/" + x.strip().split(" ")[1]]=0
currfree = totaldisk - sizedict["/"]
freed = 30000000 - currfree
smallest = 70000000
for y in sizedict.values():
    if y<smallest and y>= freed:
        smallest = y
print(smallest)