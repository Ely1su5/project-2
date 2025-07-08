import cv2
import numpy as np

# Rangos iniciales LAB (L: 0-100, A: -127 a 127, B: -127 a 127)
l_low, a_low, b_low = 0, -128, -128
l_high, a_high, b_high = 100, 127, 127

# Función para actualizar los valores LAB
def update_lab_values():
    global l_low, a_low, b_low, l_high, a_high, b_high
    l_low = cv2.getTrackbarPos('L Low', 'Controls')
    a_low = cv2.getTrackbarPos('A Low', 'Controls') - 127
    b_low = cv2.getTrackbarPos('B Low', 'Controls') - 127
    l_high = cv2.getTrackbarPos('L High', 'Controls')
    a_high = cv2.getTrackbarPos('A High', 'Controls') - 127
    b_high = cv2.getTrackbarPos('B High', 'Controls') - 127

# Función vacía para los trackbars
def nothing(x):
    pass

# Crear ventana de controles
cv2.namedWindow('Controls', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Controls', 600, 300)

# Crear trackbars para los valores LAB
cv2.createTrackbar('L Low', 'Controls', 0, 100, nothing)
cv2.createTrackbar('A Low', 'Controls', 0, 254, nothing)
cv2.createTrackbar('B Low', 'Controls', 0, 254, nothing)
cv2.createTrackbar('L High', 'Controls', 100, 100, nothing)
cv2.createTrackbar('A High', 'Controls', 254, 254, nothing)
cv2.createTrackbar('B High', 'Controls', 254, 254, nothing)

# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Actualizar valores LAB desde los trackbars
    update_lab_values()
    
    # Convertir a espacio LAB
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    
    # Crear máscara con los valores actuales
    lower = np.array([l_low, a_low, b_low])
    upper = np.array([l_high, a_high, b_high])
    mask = cv2.inRange(lab, lower, upper)
    
    # Operaciones morfológicas para mejorar la máscara
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    
    # Aplicar máscara al frame original
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Mostrar imágenes
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    
    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()