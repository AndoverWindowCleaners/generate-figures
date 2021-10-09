import matplotlib.pyplot as plt
import os
import cv2

videos_folder = "training_videos/"

WIDTH = 128
HEIGHT = 96

frames = []

x = 0
for video in os.listdir(videos_folder):
    if video != '.DS_Store':
        cap = cv2.VideoCapture(os.path.join(videos_folder,video))
        frames.append(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

plt.style.use('seaborn-white')
plt.hist(frames)
plt.xlabel("Frames in Video")
plt.ylabel("Frequency")
plt.title("Histogram of Number of Frames in Videos")

plt.savefig("times.jpg")
