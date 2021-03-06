### Lesson 3
import cv2
import numpy as np

cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,60.0,(640,480))
while True:
    ret , frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow("Web Cap2",ret)
    cv2.imshow("Web Cap",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
