import streamlit as st
import time
import os

# Function to display an image for a specific age
def display_image(container, age):
    # Define the image path
    image_path = f"img/gif/age_{age}.png"
    
    # Check if the file exists and display the image if it does
    if os.path.exists(image_path):
        container.image(image_path, caption=f"Age: {age}", use_column_width=True)
        return True
    return False

# Function to loop images as a GIF
def loop_images(container, frequency):
    while True:  # Infinite loop to keep cycling through images
        for age in range(50, 101):
            if display_image(container, age):
                time.sleep(1 / frequency)  # Delay based on the frequency

# Streamlit app
st.title("Clusters")

# Placeholder for displaying images
image_container = st.empty()

# Default to show age 20
if "default_age_shown" not in st.session_state:
    st.session_state["default_age_shown"] = True
    if not display_image(image_container, 20):
        st.warning("Default image for age 20 is not available.")

# Age selection
age = st.sidebar.number_input("Select an age to display", min_value=50, max_value=100, step=1)
if st.sidebar.button("Show Image"):
    st.write(f"Displaying image for age: {age}")
    if not display_image(image_container, age):
        st.warning("The selected age does not have an image.")

# GIF loop
frequency = st.sidebar.slider("Frequency (images per second)", min_value=1, max_value=10, step=1, value=2)
if st.sidebar.button("Start Loop"):
    loop_images(image_container, frequency)
