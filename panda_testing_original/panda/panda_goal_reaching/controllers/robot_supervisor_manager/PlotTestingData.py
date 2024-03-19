from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def plot_data(text_path="./exports/", dest_path="./exports/"):
    file=open(text_path+"Episode-score.txt", "r")
    lines = file.read().splitlines()
    scores = list(map(float, lines))
    episode = list(range(1, 1+len(scores)))
    plt.figure()
    plt.title("Episode scores over episode")
    plt.plot(episode, scores, label='Raw data')
    average_score = np.mean(scores)
    average_list = []
    for n in range(1000):
        average_list.append(average_score)
    plt.plot(average_list, label='Average')
    plt.xlabel("episode")
    plt.ylabel("episode score")
    
    plt.legend()
    plt.savefig(dest_path+'trend.png')
    print("Last SMA500:",np.mean(scores))

def heatmap(text_path="./exports/", dest_path="./exports/"):
    file=open(text_path+"Episode-score.txt", "r")
    lines = file.read().splitlines()
    scores = list(map(float, lines))
    file=open(text_path+"Target-position.txt", "r")
    lines = file.read().splitlines()
    target_position = list(map(float, lines)) # [x, y, z, x, y, z, ...]
    x = []
    y = []
    z = []
    for n in range(int(len(target_position)/3)):
        index = n*3
        x.append(target_position[index])
        y.append(target_position[index+1])
        z.append(target_position[index+2])

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c=scores)
    ax.scatter(0, 0, 0, c='red')

    ax.set_title("Position-Score Heatmap")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    plt.savefig(dest_path + "Position-Score.png")
    plt.show()

if __name__ == '__main__':
    plot_data()
    heatmap()
