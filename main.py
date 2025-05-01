import streamlit as st
import numpy as np
import cv2
from utils.functions import *

st.write("## Image Processing with Python")

enable = st.checkbox("Enable Camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    file_bytes = np.asarray(bytearray(picture.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, channels="BGR", caption="Original Image")

    processed_image = image.copy()

    st.write("### Add Noise")
    col1, col2, col3, col4, _ = st.columns([1, 1, 1, 1, 1])
    if col1.button("Gaussian Noise", use_container_width = True):
        processed_image = add_noise(processed_image, option = 1)
    if col2.button("S&P Noise", use_container_width = True):
        processed_image = add_noise(processed_image, option = 2)
    if col3.button("Poisson Noise", use_container_width = True):
        processed_image = add_noise(processed_image, option = 3)
    if col4.button("Speckle Noise", use_container_width = True):
        processed_image = add_noise(processed_image, option = 4)

    st.write("### Remove Noise")
    col1, col2, col3, _, _ = st.columns([1, 1, 1, 1, 1])
    if col1.button("Gaussian Blur", use_container_width = True):
        processed_image = remove_noise(processed_image, mode = 1)
    if col2.button("Median Blur", use_container_width = True):
        processed_image = remove_noise(processed_image, mode = 2)
    if col3.button("Normal Blur"):
        processed_image = remove_noise(processed_image, mode = 3)

    st.write("### Flip Image")
    if st.button("Flip Image"):
        processed_image = flip_image(processed_image)

    st.write("### Rotate Image")
    col1, col2, col3, _, _ = st.columns([1, 1, 1, 1, 1])
    if col1.button("Rotate 90", use_container_width = True):
        processed_image = rotate_image(processed_image, angle=90)
    if col2.button("Rotate 180", use_container_width = True):
        processed_image = rotate_image(processed_image, angle=180)
    if col3.button("Rotate 270", use_container_width = True):
        processed_image = rotate_image(processed_image, angle=270)

    st.image(processed_image, channels="BGR", caption="Processed Image")
