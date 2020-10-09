from sys import maxsize
class graph:
    def __init__(self, verts, matrix, title):
        self.__verts = verts
        self.__matrix = matrix
        self.__title = title

    def shortestPath(self, vert):
        vertIndex = self.__verts.index(vert)
        self.__dist = [maxsize for item in self.__verts]
        self.__dist[vertIndex] = 0
        self.__prev = ["-" for item in self.__verts]
        self.__prev[vertIndex] = "SI"
        self.__finished = [False for item in self.__verts]
        self.recurseThrough(vert)
        self.displayShortest(vert)

    def recurseThrough(self, startVert):
        self.doLayer(startVert)
        self.__finished[self.__verts.index(startVert)] = True
        adjacent = self.order(self.__matrix[self.__verts.index(startVert)])
        for item in adjacent:
            if not self.__finished[self.__verts.index(item)]:
                self.doLayer(item)
        for item in adjacent:
            if not self.__finished[self.__verts.index(item)]:
                self.recurseThrough(item)

    def doLayer(self, vert):
        vertIndex = self.__verts.index(vert)
        order = self.order(self.__matrix[vertIndex])
        for item in order:
            self.dijkstra(item, vert)

    def order(self, array):
        localarray = [item for item in array]
        newArray = sorted(localarray)
        indexes = []
        for i in range(len(newArray)):
            if newArray[i] != "0":
                index = localarray.index(newArray[i])
                indexes.append(index)
                localarray[index] = "-"
        letterOrder = []
        for index in indexes:
            letterOrder.append(self.__verts[index])
        return letterOrder

    def dijkstra(self, curr, comp):
        if curr == comp:
            dist = 0
        else:
            dist = int(self.__matrix[self.__verts.index(comp)][self.__verts.index(curr)])
        if dist != 0:
            if dist + self.__dist[self.__verts.index(comp)] < self.__dist[self.__verts.index(curr)]:
                self.__dist[self.__verts.index(curr)] = dist + self.__dist[self.__verts.index(comp)]
                self.__prev[self.__verts.index(curr)] = comp

    def displayShortest(self, startV):
        dists = self.__dist
        prevs = self.__prev
        print("============================================================")
        print(self.__title)
        print("Start Item:", startV, "\n")
        for item in self.__verts:
            if item == startV:
                pass
            else:
                thePath = self.findPath(self.__prev,item)
                theDistance = self.__dist[self.__verts.index(item)]
                print("From", startV, "to", item)
                print("Shortest Path :", " to ".join(list(thePath)))
                print("Distance :", theDistance,"\n")

    def findPath(self, list, vert):
        path = ""
        if list[self.__verts.index(vert)] == "SI":
            path = path + (vert)
        else:
            path = path + (self.findPath(list, list[self.__verts.index(vert)]))
            path = path + (vert)
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
