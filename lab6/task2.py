import cv2

img = cv2.imread("test_img.png")

# Увеличение в 1.5 раза
img = cv2.resize(
    img,
    (int(img.shape[1] * 1.5), int(img.shape[0] * 1.5)),
    interpolation=cv2.INTER_AREA,
)

# Отразить зеркально
img = cv2.flip(img, 1)  # cv2.flip(img, -1)

# Поворот на 10 градусов против часовой стрелки
(h, w, d) = img.shape
c = (w // 2, h // 2)

rm = cv2.getRotationMatrix2D(c, 10, 1.0)

img = cv2.warpAffine(img, rm, (w, h))

# Сохранение и вывод
cv2.imwrite("task2_img.png", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
