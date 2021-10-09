import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

videos_folder = "training_videos/"

WIDTH = 128
HEIGHT = 96

frames = []

x = 0
for video in os.listdir(videos_folder):
    if video != '.DS_Store':
        avg = 0
        cap = cv2.VideoCapture(os.path.join(videos_folder,video))
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                avg += np.average(frame)
            else:
                break
        frames.append(avg/num_frames/255)


plt.hist(frames)
plt.xlabel("Average Light Intensity")
plt.ylabel("Frequency")
plt.title("Histogram of Average Light Intensities in Videos")
plt.xlim([0,1])

plt.savefig("intensities.jpg")
