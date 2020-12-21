import numpy as np
from matplotlib import pyplot as plt
import random as r


def Mean(k,Points,Final_points,DATA):
    xs,ys = [],[]
    Means = []
    for points in Final_points:
        xs,ys = [],[]
        for point in points:
            xs.append(point[0])
            ys.append(point[1])
        xs = np.array(xs)
        ys = np.array(ys)
        Means.append([xs.mean(),ys.mean()])
    choice = input("Type C to continue for the most accuracy,Type anything else to quit --> ")
    if choice == "C" or choice == "c":
        K_means(k,DATA[0],DATA[1],Means)
    

def cluster(k,datas,points,styles):
    Final_points = [[] for _ in range(k)]
    Vectors = []
    Lengths = []
    for data in datas:
        Lengths,Vectors = [],[]
        for point in points:
            Vectors.append((data[0]-point[0],data[1]-point[1]))
        for vector in Vectors:
            Lengths.append(np.sqrt((vector[0]**2)+(vector[1]**2)))
        for i,length in enumerate(Lengths):
            if length == min(Lengths):
                Final_points[i].append(data)
                break

    for i,point in enumerate(Final_points):
        plt.plot(points[i][0],points[i][1],styles[i][0]+"-s")
        for pts in point:
            plt.plot(pts[0],pts[1],styles[i])
    plt.show()
    return Final_points
                
                 
def K_means(k,dataX,dataY,rdn=[]):
    fig = plt.figure("K_means")
    plt.title("K-means")
    limitMax = max([max(dataX),max(dataY)])
    limitMin = min([min(dataX),min(dataY)])
    style = ["r.-","b.-","c.-","m.-","y.-","k.-","w.-"]
    assert k <= len(style),"Take a lower number for the k parameter"
    datas = list(zip(dataX,dataY))
    if rdn == []:
        for i in range(k):
            rdn.append([])
            for _ in range(2):
                rdn[i].append(r.randint(limitMin,limitMax+1))
        for i,point in enumerate(rdn):
            plt.plot(point[0],point[1],style[i][0]+"-s")
        for data in datas:
            plt.plot(data[0],data[1],"g.-")
        plt.show()
    Final_points = cluster(k,datas,rdn,style)
    Mean(k,rdn,Final_points,(dataX,dataY))

x_num,y_num = list(map(int,input("Enter the number of x and y values.\n Example : 100,100\n-->  ").split(",")))
K = int(input("Enter the K parameter,Remember the maximum value for K is 7 because\nThe function only supports 7 colors for segmentations\n--> "))
points = [np.random.randint(100,size=y_num),np.random.randint(100,size=y_num)]
K_means(K,points[0],points[1],rdn=[])
