# DirectedGraphTraversal
#Imagine you are dropped into a maze. You have to find the shortest path to find an item, and then you have to find the shortest path back to the entrance. However, every room has unique paths to other adjacent rooms which may not necessarily be two ways. How will you find the shortest path?

#This can be turned into an unweighted directed graph problem. We may use BFS to solve this. All we have to do is BFS from the entrance to the item and then back from the item to the entrance and add the two distances together. Since it is a directed graph, the shortest path from the entrance to the treasure is not trivially the same as the reverse, hence why we do BFS twice.

#The maze is encoded with hexadecimal values. Put into binary form we get a value from 0000 to 1111. Each digit acts as a switch which controls which adjacent room you may travel to. From left to right, a 1 corresponds to a blockage going right, up, left and down. So 1000 means you can go any direction but down and 1111 means you cannot move at all from this square!

#I have solved this problem in python, my solution has not been entirely optimized but I wanted to post it here and perhaps I will polish it further at a later date. Thank you for checking this out!
