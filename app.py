import streamlit as st
from tensorflow import keras
from PIL import Image
import numpy as np

model = keras.models.load_model("mnist_cnn_model.keras")

st.title("Digit Classifier")

uploaded = st.file_uploader("Upload digit image", type=["png","jpg","jpeg"])

if uploaded:
    image = Image.open(uploaded).convert('L')
    image = image.resize((28,28))

    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = img_array.reshape(1,28,28,1)

    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    st.image(image, caption="Uploaded Image")
    st.write("Predicted Digit:", predicted_digit)