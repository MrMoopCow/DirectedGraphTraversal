#Imagine you are dropped into a maze. You have to find the shortest path to find an item, and then you have to find the shortest path back to the entrance. However, every room has unique paths to other adjacent rooms which may not necessarily be two ways. How will you find the shortest path?

#This can be turned into an unweighted directed graph problem. We may use BFS to solve this. All we have to do is BFS from the entrance to the item and then back from the item to the entrance and add the two distances together. Since it is a directed graph, the shortest path from the entrance to the treasure is not trivially the same as the reverse, hence why we do BFS twice.

#The maze is encoded with hexadecimal values. Put into binary form we get a value from 0000 to 1111. Each digit acts as a switch which controls which adjacent room you may travel to. From left to right, a 1 corresponds to a blockage going right, up, left and down. So 1000 means you can go any direction but down and 1111 means you cannot move at all from this square!

#I have solved this problem in python, my solution has not been entirely optimized but I wanted to post it here and perhaps I will polish it further at a later date. Thank you for checking this out!

import sys
import math
#input for starting x and y:
xs, ys = [int(i) for i in input().split()]
#input for the rabbit (or goal square)
xr, yr = [int(i) for i in input().split()]
#input for width and height of map
w, h = [int(i) for i in input().split()]
#defining some variables for BFS
dFirst = [[[xs,ys]]]
F1 = [[xs,ys]]
F2 = [[xr,yr]]
Entry = [xs,ys]
Rabbit = [xr,yr]
dSecond= [[[xr,yr]]]
grid=[]
for i in range(h):
    l = input()
    grid.append(l)
    print(l, file=sys.stderr, flush=True)
k = 1
foundRabbit = False
while(k>0):
    print("k:",k, file=sys.stderr, flush=True)
    pDepth = dFirst[k-1]
    dFirst.append([])
    print("dFirst:",dFirst, file=sys.stderr, flush=True)
    print("pDepth:",pDepth, file=sys.stderr, flush=True)
    for a in pDepth:
        x = a[0]
        y = a[1]
        val = grid[y][x]
        print("Grid value:",val, file=sys.stderr, flush=True)
        #test if we have a right wall:
        TMP = int(val, 16)
        TMP = format(TMP, '0>4b')
        TMP = str(TMP)
        print("TMP:",TMP, file=sys.stderr, flush=True)
        if(TMP[0]=='0' and x!=w-1):
            #can go right
            print("We can go right!", file=sys.stderr, flush=True)
            new = [x+1,y]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[1]=='0' and y!=0):
            #can go up
            print("We can go up!", file=sys.stderr, flush=True)
            new = [x,y-1]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[2]=='0' and x!=0):
            #can go left
            print("We can go left!", file=sys.stderr, flush=True)
            new = [x-1,y]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[3]=='0' and y!=h-1):
            #can go down
            print("We can go down!", file=sys.stderr, flush=True)
            new = [x,y+1]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)
    if(foundRabbit):
        break
    k=k+1
firstPath = len(dFirst)-1
k = 1
foundRabbit = False
Rabbit = Entry
dFirst=dSecond
F1=F2
while(k>0):
    pDepth = dFirst[k-1]
    dFirst.append([])
    for a in pDepth:
        x = a[0]
        y = a[1]
        val = grid[y][x]
        print(val, file=sys.stderr, flush=True)
        #test if we have a right wall:
        TMP = int(val, 16)
        TMP = format(TMP, '0>4b')
        TMP = str(TMP)
        if(TMP[0]=='0' and x!=w-1):
            #can go right
            new = [x+1,y]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[1]=='0' and y!=0):
            #can go up
            new = [x,y-1]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[2]=='0' and x!=0):
            #can go left
            new = [x-1,y]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)

        if(TMP[3]=='0' and y!=h-1):
            #can go down
            new = [x,y+1]
            if(new==Rabbit):
                foundRabbit = True
                break
            inF1 = False
            for coord in F1:
                if coord == new:
                    inF1 = True
                    break
            if(inF1 == False):
                F1.append(new)
                dFirst[k].append(new)
    if(foundRabbit):
        break
    k=k+1

print(firstPath,len(dSecond)-1)
