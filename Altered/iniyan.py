import cv2
import numpy as np 

# Read image
img = cv2.imread("./IPdataset/2.jpg")

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color ranges for ripe, unripe, and overripe bananas
ripe_lower = np.array([20, 100, 100])
ripe_upper = np.array([30, 255, 255])
unripe_lower = np.array([50, 100, 100])
unripe_upper = np.array([80, 255, 255])
overripe_lower = np.array([0, 0, 0])
overripe_upper = np.array([20, 100, 100])

# Create masks for each color range
ripe_mask = cv2.inRange(hsv, ripe_lower, ripe_upper)
unripe_mask = cv2.inRange(hsv, unripe_lower, unripe_upper)
overripe_mask = cv2.inRange(hsv, overripe_lower, overripe_upper)

# Apply masks to the original image
ripe_res = cv2.bitwise_and(img, img, mask=ripe_mask)
unripe_res = cv2.bitwise_and(img, img, mask=unripe_mask)
overripe_res = cv2.bitwise_and(img, img, mask=overripe_mask)

# Count the number of pixels for each mask
ripe_pixels = np.count_nonzero(ripe_mask)
unripe_pixels = np.count_nonzero(unripe_mask)
overripe_pixels = np.count_nonzero(overripe_mask)

# Determine the ripeness based on the percentage of pixels for each color range
total_pixels = img.shape[0] * img.shape[1]
ripe_percent = ripe_pixels / total_pixels
unripe_percent = unripe_pixels / total_pixels
overripe_percent = overripe_pixels / total_pixels

if overripe_percent > 0.1:
    print("Overripe - 8")
elif ripe_percent > unripe_percent:
    if ripe_percent > 0.2:
        print("Very Ripe - 7+")
    elif ripe_percent > 0.1:
        print("Ripe - 6")
    else:
        print("Almost Ripe - 5")
elif unripe_percent > 0.1:
    print("Raw - 3")
else:
    print("Very Raw - 2")

# # Show the original image and masked images for each color range
# cv2.imshow('Image', img)
# cv2.imshow('Ripe', ripe_res)
# cv2.imshow('Unripe', unripe_res)
# cv2.imshow('Overripe', overripe_res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
