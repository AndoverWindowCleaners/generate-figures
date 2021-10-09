import matplotlib.pyplot as plt
import os

labels_folder = "labels/"

WIDTH = 128
HEIGHT = 96

ws, hs = [], []

counts = {}
x = 0
for folder in os.listdir(labels_folder):
    if folder != '.DS_Store':
        for filename in os.listdir(f"{labels_folder}{folder}"):
            x += 1
            max_imgs = 0
            w_bests = []
            h_bests = []
            if filename.endswith("YOLO"):
                for _file in os.listdir(f"{labels_folder}{folder}/{filename}"):
                    with open(f"{labels_folder}{folder}/{filename}/{_file}") as f:
                        num_lines = 0
                        w_temps = []
                        h_temps = []
                        for line in f:
                            num_lines += 1
                            line = line.split()
                            label, rest = int(line[0]), line[1:]
                            xcenter, ycenter, w, h = map(float, rest)
                            # lines.append([int((xcenter-w/2)*WIDTH), int((ycenter-h/2)*HEIGHT), int((xcenter+w/2)*WIDTH), int((ycenter-h/2)*HEIGHT)])
                            w_temps.append(int(w*WIDTH))
                            h_temps.append(int(h*HEIGHT))
                        if num_lines > max_imgs:
                            max_imgs = num_lines
                            w_bests = w_temps.copy()
                            h_bests = h_temps.copy()
            ws += w_bests
            hs += h_bests
            if max_imgs in counts:
                counts[max_imgs] += 1
            else:
                counts[max_imgs] = 1

print(counts)

plt.scatter(ws, hs, c='b')

plt.tick_params(which='both', left=False, labelleft=False, bottom=False, labelbottom=False)
plt.xlabel('Width')
plt.ylabel('Height')

plt.title("Widths and Heights of Windows")
plt.savefig('wh.jpg')