import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
duration = 120
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output2.mov',fourcc, 20.0, (1280,720))
start_time = time.time()
while(int(time.time() - start_time) < duration):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()