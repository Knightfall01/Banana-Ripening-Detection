import cv2
import numpy as np 
import streamlit as st

st.title("Banana Ripeness Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Load the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    cap = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Apply image processing
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

    # Display the result
    if overripe > 5000:
        result = "Overripe - 8 Days of Harvest"
    elif yellow > green:
        if yellow-green > 12000:
            result = "Very Ripe - 7 Days of Harvest"
        elif yellow-green > 6500:
            result = "Ripe - 6 Days of Harvest"
        elif yellow-green > 6000:
            result = "Almost Ripe - 5 Days of Harvest"
        elif yellow-green > 3500:
            result = "Ripening - 4 Days of Harvest"
        elif yellow-green > 350:
            result = "Raw - 3 Days of Harvest"
        elif yellow-green > 15:
            result = "Very Raw - 2 Days of Harvest"
    else:
        result = "Very Raw - 1 Day of Harvest"

    st.image(cap, caption='Input Image', use_column_width=True)
    st.write(result)

