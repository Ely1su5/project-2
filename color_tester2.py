import cv2 as cv
import numpy as np

azulAlto = np.array([150, 120, 150], dtype=np.uint8)
azulBajo = np.array([30, 0, 0], dtype=np.uint8)

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    mask = cv.inRange(hsv, azulBajo, azulAlto)
    
    kernel = np.ones((5, 5), np.uint8)
    eroded_mask = cv.erode(mask, kernel)
    dilated_mask = cv.dilate(eroded_mask, kernel)
    mask = dilated_mask

    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:
            M = cv.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv. circle(frame, (cx, cy), 7, (255, 255, 255), 5)
                newcontour = cv.convexHull(contour)
                cv.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()