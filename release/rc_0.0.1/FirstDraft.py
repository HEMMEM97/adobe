import numpy as np
import matplotlib.pyplot as plt
import check

art = 3

def read_csv(csv_path):
    np_path_XYs = np.genfromtxt(csv_path, delimiter=',')
    path_XYs = []
    for i in np.unique(np_path_XYs[:, 0]):
        npXYs = np_path_XYs[np_path_XYs[:, 0] == i][:, 1:]
        XYs = []
        for j in np.unique(npXYs[:, 0]):
             XY = npXYs[npXYs[:, 0] == j][:, 1:]
             XYs.append(XY)
            #  print(XY)
        path_XYs.append(XYs) 
        # print(len(path_XYs))
    return path_XYs


def getCoordinates(num : int, path_XYs):
    XYs = path_XYs[num] #list of list, inner list x,y.
    for i, XY in enumerate(XYs):
        L = []
        for i in range(len(XY)):
            L.append([XY[:, 0][i], XY[:, 1][i]])
    return L

def plot(paths_XYs, colours):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    
    # for i, XYs in enumerate(paths_XYs):
    #     c = colours[i % len(colours)]
    #     for XY in XYs:
    #         ax.plot(XY[:, 0], XY[:, 1], c=c, linewidth=2)



    XYs = path_XYs[art] #list of list, inner list x,y.
    for i, XY in enumerate(XYs) :
            # ax.plot(XY[:, 0], XY[:, 1], c=colours[0], linewidth=2)     
            for i in range(len(XY)):
                 plt.scatter(XY[:, 1][i] * 10, XY[:, 0][i] * 10,c='black', s=0.05)
            
    # print(XYs)

    ax.set_aspect('equal')
    plt.show()
    


path_XYs = read_csv("problems/frag01_sol.csv")    
plot(path_XYs,['red'])



L = getCoordinates(art , path_XYs)
print(L)
accuracy = check.straight_line(L)
print(accuracy)

