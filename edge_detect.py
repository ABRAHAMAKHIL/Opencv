import cv2
import  numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    laplacian = np.uint8(laplacian)
    cv2.imshow("frame",laplacian)
    edges = cv2.Canny(frame,100,100)
    cv2.imshow("frame2",edges)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
