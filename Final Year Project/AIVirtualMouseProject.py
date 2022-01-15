import cv2
import numpy as np
import HandTrackingModule as htm
import time 
import autopy

cap = cv2.VideoCapture(0)
################################
Wcam, Hcam = 640, 480
frameR = 100 # frame reduction
smoothening = 5
#################################

cap.set(3, Wcam)
cap.set(4, Hcam)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScrn, hScrn = autopy.screen.size()

plocX, plocY = 0, 0
clocX, clocY = 0, 0


while True:
    # 1. Find Hand LandMarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList)!=0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check ehich fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (Wcam - frameR, Hcam - frameR),(255, 0, 255), 2)
        # 4. Only Index Finger : Moving mode
        if fingers[1] == 1 and fingers[2] == 0:

            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, Wcam-frameR),(0, wScrn))
            y3 = np.interp(y1, (frameR, Hcam-frameR),(0, hScrn))
            # 6. Smoothen values
            clocX = plocX + (x3-plocX)//smoothening
            clocY = plocY + (y3-plocY)//smoothening

            # 7. Move Mouse
            autopy.mouse.move(wScrn - clocX, clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255), cv2.FILLED)
            plocX, plocY = clocX, clocY
        # 8. Both Index and middle fingers are up : Cicking mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img,(lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()

    # 11. Frame rate
    cTime = time.time()
    fps = 1//(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(fps), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)


