from collections import defaultdict

# main class initialize edges and graph///////////////////////////////////


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return (i)
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # main call///////////////////////////////////////////////////
    def KruskalMST(self):

        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        wr = open("./Output/output.txt", "w")

        print("\n\nConstructed MST for cities:\n")
        count2 = 0
        sumDis = 0
        for u, v, weight in result:
            count2 = count2+1
            sumDis = sumDis + weight
            # print tree////////////////////////////////////////////////////////////
            c1 = mapIdtoKey.get(u)
            c2 = mapIdtoKey.get(v)
            wrt = c1 + '     \t' + c2 + '    \t  ' + \
                "==    " + str(weight/1000) + ' km.'
            wr.write(wrt + "\n")
            print(c1 + '     \t' + c2 + '    \t  ' +
                  "==    " + str(weight/1000) + ' km.')

        print("\nCost of spanning tree: " +
              str(sumDis/1000) + " Km.")
        wr.write("\n\nCost of spanning tree: " +
                 str(sumDis/1000) + " Km.")
        wr.close()
        if(count2 < noCity-1):
            print(
                "Can't create a spanning tree!!\nRemove some of the non selected edges!!!\n")
        # ///////////////////////////////////////////////////////////////////////////


# # Driver code
# //////////////////////////////////////////////////////////////////
# take edges list
file1 = open("edgesList.txt", "r+")
edges = 0

# print("Output of Readlines function is ")
edgeli = []
s = file1.readline()
while s:
    edges = edges + 1
    edgeli.append(s.split())
    s = file1.readline()

# print(edges)

file1.close()

# dictionary to map city to id///////////////////////////////

mapIdDict = {}
mapIdtoKey = {}
noCity = 0
read = open("./inputs/cities.txt", "r+")
line = []
s = read.readline()
while s:
    noCity = noCity + 1
    line = s.split()
    mapIdtoKey[int(line[0])] = line[1]
    mapIdDict[line[1]] = int(line[0])
    s = read.readline()

# print(mapIdDict)
# print(mapIdtoKey)
read.close()
# print("city" + str(noCity))

# end dict maping////////////////////////////////////////////////////////

g = Graph(noCity)
cnt1 = 0
while(cnt1 < edges):
    # city1 = edgeli[i][0]
    # city2 = edgeli[i][1]
    c1 = mapIdDict.get(edgeli[cnt1][0])
    c2 = mapIdDict.get(edgeli[cnt1][1])
    weight1 = edgeli[cnt1][2]

    # print(c1, c2, int(weight1))

    cnt1 = cnt1 + 1
    # print(cnt1)

    g.addEdge(c1, c2, int(weight1))


g.KruskalMST()

print()
