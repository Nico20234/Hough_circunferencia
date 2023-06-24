import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('aro.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar desenfoque para reducir el ruido
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Aplicar la transformada de Hough de circunferencias
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Verificar si se detectaron círculos
if circles is not None:
    # Redondear y convertir las coordenadas a enteros
    circles = np.round(circles[0, :]).astype(int)

    # Dibujar los círculos encontrados
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

    # Mostrar la imagen con los círculos detectados
    cv2.imshow('Detected Circles', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se detectaron círculos en la imagen.")
