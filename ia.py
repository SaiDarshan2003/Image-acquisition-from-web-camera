1.import numpy as np
import cv2
Capture=cv2.VideoCapture(0)
while(True):
    R,Frame=Capture.read()
    Width=int(Capture.get(3))
    Height=int(Capture.get(4))
    image=np.zeros(Frame.shape,np.uint8)
    smaller_frame=cv2.resize(Frame, (0,0), fx=0.5, fy=0.5)
    image[:Height//2,:Width//2]=smaller_frame
    image[Height//2:,:Width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[:Height//2,Width//2:]=smaller_frame
    image[Height//2:,Width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    cv2.imshow("Frame",image)
    if cv2.waitKey(1)==ord('q'):
        break
Capture.release()
cv2.destroyAllWindows()
2.import numpy as np
import cv2
Capture=cv2.VideoCapture(0)
while(True):
    R,Frame=Capture.read()
    Width=int(Capture.get(3))
    Height=int(Capture.get(4))
    image=np.zeros(Frame.shape,np.uint8)
    smaller_frame=cv2.resize(Frame, (0,0), fx=0.5, fy=0.5)
    image[:Height//2,:Width//2]=smaller_frame
    image[Height//2:,:Width//2]=smaller_frame
    image[:Height//2,Width//2:]=smaller_frame
    image[Height//2:,Width//2:]=smaller_frame
    cv2.imshow("Frame",image)
    if cv2.waitKey(1)==ord('q'):
        break
Capture.release()
cv2.destroyAllWindows()
3.import cv2
Capture=cv2.VideoCapture(0)
while(True):
    R,Frame=Capture.read()
    cv2.imshow("Frame",Frame)
    if cv2.waitKey(1)==ord('q'):
        break
Capture.release()q
cv2.destroyAllWindows()q
4.import cv2
Capture=cv2.VideoCapture(0)
while(True):
    R,Frame=Capture.read()
    cv2.imwrite("Current Pic.jpg",Frame)
    result=False
    if cv2.waitkey(1)==ord('q'):
        break
Capture.release()q
cv2.destroyAllWindows()