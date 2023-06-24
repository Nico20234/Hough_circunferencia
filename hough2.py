import cv2
import numpy as np

# Cargar la imagen en color
image = cv2.imread('aro_3.jpg')

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el filtro de Canny para detectar los bordes
edges = cv2.Canny(gray, 50, 130)

# Aplicar la transformada de Hough para detectar las rectas
lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

# Filtrar las rectas detectadas
filtered_lines = []
for line in lines:
    rho, theta = line[0]
    if abs(theta - np.pi/2) > np.pi/6:  # Filtrar rectas que no sean verticales (±30 grados)
        filtered_lines.append(line)

# Aplicar la transformada de Hough para circunferencias
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=20, maxRadius=100)

# Dibujar las circunferencias detectadas en la imagen original
if circles is not None:
    circles = np.round(circles[0, :]).astype(int)
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# Mostrar la imagen original con las rectas y circunferencias detectadas
cv2.imshow("Detected Lines and Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


