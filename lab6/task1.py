import cv2
import numpy as np

size = 100

img = np.zeros((size, size), dtype=np.uint8)

for i in range(size):
    for j in range(size):
        if j >= i:
            img[i, j] = int(255 * (1 - ((j / 2) / size)))
        else:
            img[i, j] = int((255 / 2) * (1 - (j / size)))

cv2.imwrite("./lab6/task1_img.png", img)

cv2.imshow("Task 1 Lab6 Image:", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
