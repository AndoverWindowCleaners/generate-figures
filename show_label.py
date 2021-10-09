import cv2

img = cv2.imread('images/Folder 21 W/0000.jpg')

h, w, c = img.shape

windows = []

with open('labels/Folder 21 W/labels_folder-21-w_YOLO/0000.txt') as f:
    for line in f:
        _, xcenter, ycenter, width, height = line.split(' ')
        windows.append((int((float(xcenter)-float(width)/2)*w), int((float(ycenter)-float(height)/2)*h), int((float(xcenter)+float(width)/2)*w), int((float(ycenter)+float(height)/2)*h)))

for xmin, ymin, xmax, ymax in windows:
    img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 255), 1)

cv2.imwrite('output0.jpg', img)
