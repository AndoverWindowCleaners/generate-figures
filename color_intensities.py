import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

videos_folder = "training_videos/"

WIDTH = 128
HEIGHT = 96

blues = []
greens = []
reds = []

x = 0
for video in os.listdir(videos_folder):
    if video != '.DS_Store':
        avg = np.zeros(3)
        cap = cv2.VideoCapture(os.path.join(videos_folder,video))
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                avg += np.average(frame, (0,1))
            else:
                break
        avg /= 255*num_frames
        blues.append(avg[0])
        greens.append(avg[1])
        reds.append(avg[2])

fig, axs = plt.subplots(1, 3, sharey=True)

axs[0].hist(reds, color='r')
axs[0].set_title("Red")
axs[1].hist(greens, color='g')
axs[1].set_title("Green")
axs[2].hist(blues, color='b')
axs[2].set_title("Blue")

fig.suptitle('Histogram of Average Light Intensities in Videos')
fig.supxlabel('Average Light Intensity')
fig.supylabel('Frequency')
plt.setp(axs, xlim=[0,1])

fig.savefig("color_intensities.jpg")
