import cv2
import numpy as np

img = cv2.imread("./lab6/test_img.png")

avg_b, avg_g, avg_r, _ = cv2.mean(img)
avg_color = (int(avg_b), int(avg_g), int(avg_r))

square = np.full((100, 100, 3), avg_color, dtype=np.uint8)

cv2.imshow("Average Color Square", square)
cv2.waitKey(0)
cv2.destroyAllWindows()
