import matplotlib.pyplot as plt
import os

labels_folder = "labels/"

WIDTH = 128
HEIGHT = 96

xs, ys = [], []

for folder in os.listdir(labels_folder):
    if folder != '.DS_Store':
        for filename in os.listdir(f"{labels_folder}{folder}"):
            if filename.endswith("YOLO"):
                for _file in os.listdir(f"{labels_folder}{folder}/{filename}"):
                    with open(f"{labels_folder}{folder}/{filename}/{_file}") as f:
                        lines = []
                        for line in f:
                            line = line.split()
                            label, rest = int(line[0]), line[1:]
                            xcenter, ycenter, w, h = map(float, rest)
                            # lines.append([int((xcenter-w/2)*WIDTH), int((ycenter-h/2)*HEIGHT), int((xcenter+w/2)*WIDTH), int((ycenter-h/2)*HEIGHT)])
                            xs.append(int(xcenter*WIDTH))
                            ys.append(int(ycenter*HEIGHT))
                    break

plt.scatter(xs, ys, c='b')

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.title("Centers of Windows")
plt.savefig('output.jpg')