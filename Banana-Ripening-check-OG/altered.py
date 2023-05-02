import cv2
import numpy as np 

cap = cv2.imread("./IPdataset/6e721aea-b1cb-4ddb-8995-acc1b3903ee3.jpeg")

while(1):       
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    lower_ripe = np.array([20, 100, 100])
    upper_ripe = np.array([30, 255, 255])
    lower_unripe = np.array([50, 100, 100])
    upper_unripe = np.array([80, 255, 255])
    lower_overripe = np.array([0, 0, 0])
    upper_overripe = np.array([20, 100, 100])

    mask1 = cv2.inRange(hsv, lower_ripe, upper_ripe)
    res1 = cv2.bitwise_and(cap, cap, mask=mask1)
    mask2 = cv2.inRange(hsv, lower_unripe, upper_unripe)
    res2 = cv2.bitwise_and(cap, cap, mask=mask2)
    mask3 = cv2.inRange(hsv, lower_overripe, upper_overripe)
    res3 = cv2.bitwise_and(cap, cap, mask=mask3)

    yellow = np.count_nonzero(mask1)
    green = np.count_nonzero(mask2)
    overripe = np.count_nonzero(mask3)

    if overripe > 5000:
        print("Overripe - 8 Days of Harvest")
    elif yellow > green:
        if yellow-green > 12000:
            print("Very Ripe - 7 Days of Harvest")
        elif yellow-green > 6500:
            print("Ripe - 6 Days of Harvest")
        elif yellow-green > 6000:
            print("Almost Ripe - 5 Days of Harvest")
        elif yellow-green > 3500:
            print("Ripening - 4 Days of Harvest")
        elif yellow-green > 350:
            print("Raw - 3 Days of ")
        elif yellow-green > 15:
            print("Very Raw - 2 Days of Harvest")
    else:
        print("Very Raw - 1 Day of Harvest")

    # cv2.imshow('Image', cap)
    # cv2.imshow('res1', res1)
    # cv2.imshow('res2', res2)
    # cv2.imshow('res3', res3)

    # cv2.waitKey(0)
    break

# cv2.destroyAllWindows()
