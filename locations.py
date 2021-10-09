import matplotlib.pyplot as plt
import os

labels_folder = "labels/"

WIDTH = 128
HEIGHT = 96

xs, ys = [], []

counts = {}
x = 0
for folder in os.listdir(labels_folder):
    if folder != '.DS_Store':
        for filename in os.listdir(f"{labels_folder}{folder}"):
            x += 1
            max_imgs = 0
            x_best = []
            y_best = []
            if filename.endswith("YOLO"):
                for _file in os.listdir(f"{labels_folder}{folder}/{filename}"):
                    with open(f"{labels_folder}{folder}/{filename}/{_file}") as f:
                        num_lines = 0
                        x_temps = []
                        y_temps = []
                        for line in f:
                            num_lines += 1
                            line = line.split()
                            label, rest = int(line[0]), line[1:]
                            xcenter, ycenter, w, h = map(float, rest)
                            # lines.append([int((xcenter-w/2)*WIDTH), int((ycenter-h/2)*HEIGHT), int((xcenter+w/2)*WIDTH), int((ycenter-h/2)*HEIGHT)])
                            x_temps.append(int(xcenter*WIDTH))
                            y_temps.append(int(ycenter*HEIGHT))
                        if num_lines > max_imgs:
                            max_imgs = num_lines
                            x_best = x_temps.copy()
                            y_best = y_temps.copy()
            xs += x_best
            ys += y_best
            if max_imgs in counts:
                counts[max_imgs] += 1
            else:
                counts[max_imgs] = 1

print(counts)

plt.scatter(xs, ys, c='b')

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.title("Centers of Windows")
plt.savefig('output.jpg')