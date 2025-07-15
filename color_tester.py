import cv2
import numpy as np

# Crear ventana de controles
cv2.namedWindow('Controls', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Controls', 400, 300) 

# Trackbars para umbrales bajos y altos en cada canal LAB
cv2.createTrackbar('L Low', 'Controls', 0, 255, lambda x: None)
cv2.createTrackbar('L High', 'Controls', 255, 255, lambda x: None)
cv2.createTrackbar('A Low', 'Controls', 0, 255, lambda x: None)
cv2.createTrackbar('A High', 'Controls', 255, 255, lambda x: None)
cv2.createTrackbar('B Low', 'Controls', 0, 255, lambda x: None)
cv2.createTrackbar('B High', 'Controls', 255, 255, lambda x: None)

# Iniciar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a espacio LAB
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    # Obtener umbrales desde trackbars
    l_low = cv2.getTrackbarPos('L Low', 'Controls')
    l_high = cv2.getTrackbarPos('L High', 'Controls')
    a_low = cv2.getTrackbarPos('A Low', 'Controls')
    a_high = cv2.getTrackbarPos('A High', 'Controls')
    b_low = cv2.getTrackbarPos('B Low', 'Controls')
    b_high = cv2.getTrackbarPos('B High', 'Controls')

    # Crear máscara binaria basada en umbrales LAB
    lower = np.array([l_low, a_low, b_low])
    upper = np.array([l_high, a_high, b_high])
    mask = cv2.inRange(lab, lower, upper)

    # Aplicar máscara a la imagen original
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Dividir canales LAB
    l_channel, a_channel, b_channel = cv2.split(lab)

    # Convertir canales individuales a imágenes de 3 canales
    l_3ch = cv2.merge([l_channel, l_channel, l_channel])
    a_3ch = cv2.merge([a_channel, a_channel, a_channel])
    b_3ch = cv2.merge([b_channel, b_channel, b_channel])

    # Concatenar imágenes para visualización
    combined = np.hstack((frame, masked_frame, l_3ch, a_3ch, b_3ch))

    # Redimensionar combinado
    scale_percent = 70
    width = int(combined.shape[1] * scale_percent / 100)
    height = int(combined.shape[0] * scale_percent / 100)
    resized = cv2.resize(combined, (width, height), interpolation=cv2.INTER_AREA)

    # Mostrar resultados
    cv2.imshow('Original | Masked | L | A | B', resized)
    cv2.imshow('Mascara Binaria', mask)

    # Guardar máscara si presionas 's'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite('mascara_binaria.png', mask)
        print("Máscara binaria guardada como 'mascara_binaria.png'")
    elif key == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
