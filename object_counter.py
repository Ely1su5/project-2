import cv2 as cv
import numpy as np

verdeAlto = np.array([180, 125, 255], dtype=np.uint8)
verdeBajo = np.array([0, 0, 0], dtype=np.uint8)
rojoAlto = np.array([190, 250, 180], dtype=np.uint8)
rojoBajo = np.array([0, 140, 110], dtype=np.uint8)

def color_detecter(frame, mask, object_count, point_color=(0,255,0), thickness=2, line_color=(0,0,255), size_object=500):
    kernel = np.ones((5, 5), np.uint8)
    eroded_mask = cv.erode(mask, kernel, iterations=1)
    dilated_mask = cv.dilate(eroded_mask, kernel, iterations=1)
    mask = dilated_mask

    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 200:
            M = cv.moments(contour)
            if M["m00"] == 0: M ["00"] = 1
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv.circle(frame, (cx, cy), 7, (255, 255, 255), 5)
            newcountor = cv.convexHull(contour)
            cv.drawContours(frame, [contour], -1, line_color, thickness)
            object_count += 1
    
    return object_count
    
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    mask_verde = cv.inRange(hsv, verdeBajo, verdeAlto)
    mask_rojo = cv.inRange(hsv, rojoBajo, rojoAlto)

    object_count = 0

    object_count = color_detecter(frame, mask_rojo, object_count, point_color=(0,255,0), thickness=2, line_color=(0,255,0), size_object=500)
    object_count = color_detecter(frame, mask_verde, object_count, point_color=(0,255,0), thickness=2, line_color=(0,0,255), size_object=500)
    
    cv.putText(frame, f"Objetos detectados: {object_count}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv.imshow("Frame", frame)
    cv.imshow("Mask Rojo", mask_rojo)
    cv.imshow("Mask Verde", mask_verde)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()