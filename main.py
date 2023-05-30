import cv2 as cv

imagen = cv.imread('contorno.png')
grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
_, umbral = cv.threshold(grises, 100, 255, cv.THRESH_BINARY)
contornos, jerarquia = cv.findContours(umbral, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(imagen, contornos, -1, (65, 105, 255), 3)

# Mostrar
cv.imshow('Imagen original', imagen)
# cv.imshow('Imagen en grises', grises)
# cv.imshow('Imagen en Umbral', umbral)
cv.waitKey(0)
cv.destroyAllWindows()
