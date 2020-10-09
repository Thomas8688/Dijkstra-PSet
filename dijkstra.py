#Sys is a system module which can be used to determine the largest number usable by the system
from sys import maxsize
#Creates a class to be used for the graph
class graph:
#Class Initialisation
    def __init__(self, verts, matrix, title):
#Sets class variables for the vertices of the graph, the graph adjacency matrix, and the title of the graph
        self.__verts = verts
        self.__matrix = matrix
        self.__title = title

#Method used to call dijkstra's algorithm and properly display the results (Takes the initial vertex as an argument)
    def shortestPath(self, vert):
#Uses the .index() function to find the index of the vertex
        vertIndex = self.__verts.index(vert)
#Creats a list to contain all of the weights for the vertices (Initialised to the highest possible value)
        self.__dist = [maxsize for item in self.__verts]
#Sets the weight from the intitial vertex to 0 (Because there is no distance to get to itself)
        self.__dist[vertIndex] = 0
#Creates a list to contain all of the previous vertex (The previous vertex in the shortest path)
        self.__prev = ["-" for item in self.__verts]
#Sets the previous vertex for the initial vertex to SI (Starting Itemm)
        self.__prev[vertIndex] = "SI"
#Creats a list to contain boolean values which can tell the user if a value has been checked yet
        self.__finished = [False for item in self.__verts]
#Calls other methods within the class to carry out the main portion of dijkstra's algorithm
        self.recurseThrough(vert)
        self.displayShortest(vert)

#Method that uses recursion to move through the graph and carry out Dijkstra's algorithm
    def recurseThrough(self, startVert):
#Calls the method that carries out Dijkstra's algorithm on all of the directly adjacent vertices
        self.doLayer(startVert)
#Sets the vertex to True in finished to indicat that the vertex has already had the algorithm applied to it
        self.__finished[self.__verts.index(startVert)] = True
#Calls the method that determines the order of adjacent vertices that need to have the algorithm applied to them
        adjacent = self.order(self.__matrix[self.__verts.index(startVert)])
#Uses recursion to carry out the algorithm on the adjacent items
        for item in adjacent:
            if not self.__finished[self.__verts.index(item)]:
                self.recurseThrough(item)

#Method used to carry out the algorithm on all of the adjacent items to the passed "vert"
    def doLayer(self, vert):
#Uses the .index() function to find the index of the vertex
        vertIndex = self.__verts.index(vert)
#Calls the method that determines the order in which the adjacent vertices need to have the algorithm applied to
        order = self.order(self.__matrix[vertIndex])
#Carries out the algorithm on the adjacent vertices in order
        for item in order:
            self.dijkstra(item, vert)

#Method used to determine the order in which the vertices in an array need to be traversed
    def order(self, array):
#Creates a local array (Otherwise the class variable is altered) from the line taken from the matrix
        localarray = [item for item in array]
#Sorts the matrix line
        newArray = sorted(localarray)
#Creates an empty list to have the index values of items appended to
        indexes = []
#For loop to append the index values
        for i in range(len(newArray)):
#Only appends the index if the value is more than zero (indicating a link between the vertices in the graph)
            if newArray[i] != "0":
                index = localarray.index(newArray[i])
                indexes.append(index)
                localarray[index] = "-"
#Creats an empty list to have the letter values of the indices appended to
        letterOrder = []
#Appends the letter value of each of the indices to the list
        for index in indexes:
            letterOrder.append(self.__verts[index])
        return letterOrder

#Method used to carry out the main portion of dijkstra's algorithm
    def dijkstra(self, curr, comp):
#Sets the distance between the two passed vertices using the 2d matrix array matrix[current vertex][comparison vertex]
        dist = int(self.__matrix[self.__verts.index(comp)][self.__verts.index(curr)])
#If the distance is zero, nothing happens
        if dist != 0:
#Otherwise, if the distance to the comparison item + the distance between the items being compared is less than the current smallest distance
            if dist + self.__dist[self.__verts.index(comp)] < self.__dist[self.__verts.index(curr)]:
#The current smallest distance is updated
                self.__dist[self.__verts.index(curr)] = dist + self.__dist[self.__verts.index(comp)]
#and the current previous vertex is updated to the comparison item
                self.__prev[self.__verts.index(curr)] = comp

#Method used to display the results from Dijkstra's algorithm
    def displayShortest(self, startV):
        dists = self.__dist
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
                thePath = self.findPath(self.__prev,item)
#The shortest distance is set to the vertex item within the dists list
                theDistance = self.__dist[self.__verts.index(item)]
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


#TESTING
myVerts = ["A", "B", "C", "D"]
myMatrix = [["0","1","7","0"], ["1","0","4","2"], ["7","4","0","1"], ["0", "2", "1", "0"]]
myG = graph(myVerts, myMatrix, "Graph 1 (4 Vertices)")
myG.shortestPath("A")

myVerts2 = ["A", "B", "C", "D", "E"]
myMatrix2 = [["0","1","3","0","11"], ["1","0","0","0","2"], ["3","0","0","0","7"], ["0","0","0","0","1"], ["11","2","7","1 ","0"]]
myG2 = graph(myVerts2, myMatrix2, "Graph 2 (5 Vertices)")
myG2.shortestPath("A")


myVerts3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
myMatrix3 = [["0","4","0","0","0","0","0","8","0"],["4","0","8","0","0","0","0","11","0"],["0","8","0","7","0","4","0","0","2"],["0","0","7","0","9","14","0","0","0"],["0","0","0","9","0","10","0","0","0"],["0","0","4","0","10","0","2","0","0"],["0","0","0","14","0","2","0","1","6"],["8","11","0","0","0","0","1","0","7"],["0","0","2","0","0","0","6","7","0"]]
myG3 = graph(myVerts3, myMatrix3, "Graph 3 (9 Vertices)")
myG3.shortestPath("A")
