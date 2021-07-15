import os
import googlemaps
from itertools import combinations


read = open('./inputs/remove.txt', 'r+')

ne = []
rem = []
rem1 = []
s = read.readline()
while s:
    ne = list(s.split())
    tup = ne[0], ne[1]
    tup1 = ne[1], ne[0]
    rem.append(tup)
    rem1.append(tup1)
    s = read.readline()

# print(rem)
# print(rem1)
read.close()


# ///////////////////////////////////////////////////////

read = open("./inputs/cities.txt", "r+")
write = open("edgesList.txt", "w")


# print("Output of Readlines function is ")

li = []
rec = []
city = []
s = read.readline()
while s:
    rec = list(s.split())

    li.append(s.split())
    city.append(rec[1])
    s = read.readline()

# print()
# print(li)
# print(city)
# print()

print("\nGenerating list of edges:\n")
comb = combinations(city, 2)
for i in list(comb):

    f = 0
    j = 0
    k = 0
    for j in rem:
        if(i == j):
            rem.remove(i)
            f = 1

    if(f == 0):
        for k in rem1:
            if(i == k):
                rem1.remove(k)
                f = 1
                break

        if(f == 0):
            gmaps = googlemaps.Client(
                key='Enter_google_API_KEY_here')

            # Requires cities name
            my_dist = gmaps.distance_matrix(i[0], i[1])[
                'rows'][0]['elements'][0]['distance']['value']

            # print(gmaps.distance_matrix('nagpur', 'hyderabad')[
            #     'rows'][0]['elements'][0])

            wrt = str(i[0]) + ' ' + str(i[1]) + ' ' + str(my_dist)
            write.write(wrt + " \n")
            # print(i[0], i[1], my_dist)
            print(wrt)


read.close()
write.close()

os.system('python kruskal.py')
