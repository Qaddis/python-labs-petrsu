import cv2
import numpy as np

image = cv2.imread("./lab6/test_green.png")

img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Границы зелёного
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Маска
mask = cv2.inRange(img, lower_green, upper_green)

# Алгоритм для уменьшения шума
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

# Получить координаты контуров объекта
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Обвести зелёные объекты
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

cv2.imshow("Task 4 Lab6 Image:", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
