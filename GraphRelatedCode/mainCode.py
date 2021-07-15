import matplotlib.pyplot as plt
from matplotlib.transforms import BboxBase
import numpy as np
import os

xval = np.arange(1,101,1)
x = np.array(xval)

technWorstTime = {
    "Insertation Sort" : "N2",
    "Bubble Sort" : "N2",
    "Selection Sort" : "N2",
    "Merge Sort" : "NlogN",
    "Quick Sort" : "N2",
    "Heap Sort" : "NlogN"
}

def makingY(a_x,pType):
    if pType == "1":
        y = 1
    elif pType == "logN":
        y = log(a_x)
    elif pType == "N":
        y = a_x
    elif pType == "NlogN":
        y = a_x * np.log2(a_x)
    elif pType == "N2":
        y = a_x ** 2
    return y

def compare(first,second):
    for z in technWorstTime.keys():
        if z == first:
            t1 = z
            Func1 = technWorstTime.get(z)
        if z == second:
            t2 = z
            Func2 = technWorstTime.get(z)
    return t1,t2,Func1,Func2

def makefigure(a,b):
    topTechName,botTechName,valY1,valY2 = compare(a,b)

    fig, axs = plt.subplots(2,1, sharey=True)
    fig.suptitle(topTechName+" vs "+botTechName)
    fig.set_size_inches(7,9)

    for i,ax in enumerate(axs.flat):
        titles = []
        titles.append(topTechName)
        titles.append(botTechName)
        ax.set_title(titles[i])

    plt.setp(axs[0], xlabel='Input Size', ylabel='CPU Operation Cycle')
    plt.setp(axs[1], xlabel='Input Size', ylabel='CPU Operation Cycle')

    axs[0].plot(x,makingY(x,valY1),'tab:green')
    axs[1].plot(x,makingY(x,valY2),'tab:red')

    SaveFileName = topTechName+"_"+botTechName+".png"
    imgLoc = os.path.join(os.path.dirname(os.path.dirname(__file__)),"Documentation")
    SaveFile = os.path.join(imgLoc,SaveFileName)

    plt.savefig(SaveFile,dpi=100)