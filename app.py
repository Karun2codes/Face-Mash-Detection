import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mask_model.h5")

model = load_model()

# -------------------------------
# UI
# -------------------------------
st.title("😷 Face Mask Detection App")
st.write("Upload an image to check if a person is wearing a mask.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# -------------------------------
# Processing
# -------------------------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to numpy
    img = np.array(image)

    # 🔥 Convert grayscale → RGB
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    # 🔥 Convert RGBA → RGB
    if img.shape[-1] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    # Resize + normalize
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(img)[0][0]

    # Debug
    st.write(f"Confidence: {prediction:.4f}")

    # Output
    if prediction > 0.5:
        st.error("❌ No Mask Detected")
    :
        st.success("✅ Mask Detected")
