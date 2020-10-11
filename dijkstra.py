#Imports system module to access the largest usuable number (Substitute for Infinity)
from sys import maxsize
class graph:
#Initialization
    def __init__(self, verts, matrix, title):
#Takes a list of the vertices
        self.__verts = verts
#Takes a 2D array containing the information of the adjacency matrix
        self.__matrix = matrix
        self.__title = title

#Method used to find the shortest route to all vertices in a graph (From startV)
    def shortestPath(self, startV):
#Sets a list to contain all of the shortest distances
#At the beginning all values set to infinity (Maxsize)
        self.__dists = [maxsize for vert in self.__verts]
#The distance value of the vertex being searched is set to 0 (This is the only vertex that doesn't need to be checked)
        self.__dists[self.__verts.index(startV)] = 0
#Sets a list to contain all of the previous vertices for the shortest path
#At the beginning all values set to null (-)
        self.__prev = ["-" for vert in self.__verts]
#The previous value of the vertex being searched is set to SI (Search Item)
        self.__prev[self.__verts.index(startV)] = "SI"
#Sets a list to contain boolean values indicating if a vertex has been checked
#At the beginning all values are set to False
        self.__finished = [False for vert in self.__verts]
#Loops through each vertex
        for vert in self.__verts:
#Calls the nextVert method to determine which vertex to check next
            next = self.nextVert()
#Takes the index of the next vertex to check
            nIndex = self.__verts.index(next)
#Sets te next vertex to finished
            self.__finished[nIndex] = True
#Loops through each sub-vertex
            for uert in self.__verts:
#Takes the index value of the new vertex
                uIndex = self.__verts.index(uert)
                self.dijkstra(nIndex, uIndex, next)
#The method used to correctly display the shortest routes is called
        self.displayShortest(startV)

#Method to carry out the core process of dijkstra's algorithm
    def dijkstra(self, curr, new, vert):
#Using the 2d array self.__matrix, first the weight from the matrix is taken for the current values
#If the weight exists, and the item has not been checked yet the main portion of dijkstras algorithm is completed
        if self.__matrix[curr][new] != "0" and self.__finished[new] != True:
#Checks if the weight to the previous item added to the new weight is smaller than the current weight
            if self.__dists[curr] + int(self.__matrix[curr][new]) < self.__dists[new]:
#If so, the current weight is replaced with the weight to the previous vertex added to the new weight
                self.__dists[new] = self.__dists[curr] + int(self.__matrix[curr][new])
#and the current previous item is replaced with the current item
                self.__prev[new] = vert

#Method used to determine which vertex to check next
    def nextVert(self):
#Sets the base distance to infinity (maxsize)
        dist = maxsize
#Loops through each vertex
        for vert in self.__verts:
#Sets an index item to the vertex index
            index = self.__verts.index(vert)
#If the current dist is smaller than the base dist and the vertex hasn't been checked yet
            if self.__dists[index] < dist and self.__finished[index] == False:
#The base distance is replaced with the current distance
                dist = self.__dists[index]
#Sets the index of the next item to the index of the new distance
                nextIndex = index
#Returns the vertex value for nextIndex
        return self.__verts[nextIndex]

#Method used to display the results from Dijkstra's algorithm
    def displayShortest(self, startV):
        dists = self.__dists
        prevs = self.__prev
#Line of Equals signs to help with testing (Distinguish between algorithm calls)
        print("============================================================")
#Prints the title of the graph
        print(self.__title)
#Prints the vertex that the user wants to compare
        print("Start Item:", startV, "\n")
#For every vertex
        for item in self.__verts:
#If the vertex is equal to the comparison vertex nothing happens
            if item == startV:
                pass
#Otherwise
            else:
#The method used to determine the route of the shortest path is called
                thePath = self.findPath(prevs,item)
#The shortest distance is set to the vertex item within the dists list
                theDistance = dists[self.__verts.index(item)]
#Prints all of the data
                print("From", startV, "to", item)
                print("Shortest Path :", " to ".join(list(thePath)))
                print("Distance :", theDistance,"\n")

#Method used to determine the route of the shortest path using recursion
    def findPath(self, list, vert):
#Sets the path to an empty list
        path = ""
#Recursion terminating condition, if the reached item is the comparison vertex
        if list[self.__verts.index(vert)] == "SI":
#The start vertex is added to the path
            path = path + (vert)
        else:
#Recursive call, if the vertex is not the comparison vertex then the findPath method is called on the vertex
            path = path + (self.findPath(list, list[self.__verts.index(vert)]))
#The vertex is added to the path to create the chain
            path = path + (vert)
#Returns the path each time to allow for recursion
        return path


#TESTING - GRAPH VISUALISATION CAN BE FOUND N THE REPOSITORY
myVerts = ["A", "B", "C", "D"]
myMatrix = [["0","1","7","0"], ["1","0","4","2"], ["7","4","0","1"], ["0", "2", "1", "0"]]
myG = graph(myVerts, myMatrix, "Graph 1 (4 Vertices)")
myG.shortestPath("A")

myVerts2 = ["A", "B", "C", "D", "E"]
myMatrix2 = [["0","1","3","0","11"], ["1","0","0","0","2"], ["3","0","0","0","7"], ["0","0","0","0","1"], ["11","2","7","1","0"]]
myG2 = graph(myVerts2, myMatrix2, "Graph 2 (5 Vertices)")
myG2.shortestPath("A")


myVerts3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
myMatrix3 = [["0","4","0","0","0","0","0","8","0"],["4","0","8","0","0","0","0","11","0"],["0","8","0","7","0","4","0","0","2"],["0","0","7","0","9","14","0","0","0"],["0","0","0","9","0","10","0","0","0"],["0","0","4","0","10","0","2","0","0"],["0","0","0","14","0","2","0","1","6"],["8","11","0","0","0","0","1","0","7"],["0","0","2","0","0","0","6","7","0"]]
myG3 = graph(myVerts3, myMatrix3, "Graph 3 (9 Vertices)")
myG3.shortestPath("A")
