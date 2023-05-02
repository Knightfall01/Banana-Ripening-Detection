import streamlit as st
import cv2
import numpy as np 

st.title("Banana Ripeness Detector")

st.write("A Image Classification Web App That Detects the Ripeness Stage of Banana")

# Allow user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

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
    
    st.image(img, channels="BGR", caption="Original Image")
    
    # Display the ripeness result
    if overripe_percent > 0.1:
        st.write("Overripe - 8")
    elif ripe_percent > unripe_percent:
        # if ripe_percent > 0.2:
        #     st.write("Very Ripe - 7+")
        if ripe_percent > 0.2:
            st.write("Ripe - 6")
        else:
            st.write("Almost Ripe - 5")
    elif unripe_percent > 0.1:
        st.write("Raw - 3")
    else:
        st.write("Very Raw - 2")

    # Show the original image and masked images for each color range
    # st.image(img, caption="Original Image")
    # st.image(ripe_res, caption="Ripe Bananas")
    # st.image(unripe_res, caption="Unripe Bananas")
    # st.image(overripe_res, caption="Overripe Bananas")

