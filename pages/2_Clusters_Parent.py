# import streamlit as st
# import time
# import os

# # Function to display an image for a specific age
# def display_image(container, age):
#     # Define the image path
#     image_path = f"img/gif/age_{age}.png"
    
#     # Check if the file exists and display the image if it does
#     if os.path.exists(image_path):
#         container.image(image_path, caption=f"Age: {age}", use_column_width=True)
#         return True
#     return False

# # Function to loop images as a GIF
# def loop_images(container, frequency):
#     while True:  # Infinite loop to keep cycling through images
#         for age in range(50, 101):
#             if display_image(container, age):
#                 time.sleep(1 / frequency)  # Delay based on the frequency

# # Streamlit app
# st.title(f"Clusters")

# # Placeholder for displaying images
# image_container = st.empty()

# # Default to show age 20
# if "default_age_shown" not in st.session_state:
#     st.session_state["default_age_shown"] = True
#     if not display_image(image_container, 20):
#         st.warning("Default image for age 20 is not available.")

# # Age selection
# age = st.sidebar.number_input("Select an age to display", min_value=50, max_value=100, step=1)
# if st.sidebar.button("Show Image"):
#     st.write(f"Displaying image for age: {age}")
#     if not display_image(image_container, age):
#         st.warning("The selected age does not have an image.")

# # GIF loop
# frequency = st.sidebar.slider("Frequency (images per second)", min_value=1, max_value=10, step=1, value=2)
# if st.sidebar.button("Start Loop"):
#     loop_images(image_container, frequency)



# import streamlit as st

# # HTML content with larger and bold text
# html_content = """
# <div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: bold;">
#     <span style="text-align: left;">Left-aligned text</span>
#     <span style="text-align: right;">Right-aligned text</span>
# </div>
# """

# # Render the HTML using st.markdown with unsafe_allow_html=True
# st.markdown(html_content, unsafe_allow_html=True)

# import pandas as pd
# import streamlit as st
# from io import StringIO
# import numpy as np

# # CSV data as a string
# csv_data = """id,x,y,gender
# 45G,-0.9829594802925735,-0.9828579146719195,female
# amy,-0.8916632355433085,-0.9011813535816751,female
# betty,-0.869335137566432,-0.6446537565838804,female
# chuck,-0.9703637105786528,-0.9711503864595149,male
# doug,-0.7942375748360203,-0.796769993005097,male
# ed,-0.9375489478360365,-0.9365054947654636,male
# frank,-0.9482299072087317,-0.9485686132627362,male
# hank,-0.29400029875761186,-0.7960832592382031,male
# ivy,-0.7962462896779148,-0.7979072440006707,female
# keith,-0.970247649025494,-0.9709564746444578,male
# kent,-0.8823721444836035,0.1759498931419558,male
# linda,-0.3045493301652009,-0.3066028903759098,female
# mandy,-0.9455187270950723,-0.9461613030463336,female
# nan,-0.7345318887340221,-0.7344189632037068,female
# olivia,0.023279151590418268,0.02312116219802296,female
# paula,0.3063395041194579,-0.7910336946590485,female
# pete,0.4692616387208435,0.4724279150404511,male
# ruth,0.05294339607850468,0.05208477936279082,female
# steve,-0.96896590743563,-0.9685771717894636,male
# sue,0.9411546141067458,0.9388419195969412,female
# zeke,-0.48259849393556886,-0.4966319344800373,male
# """

# # Read the CSV data into a pandas DataFrame
# df = pd.read_csv(StringIO(csv_data))

# # Display the DataFrame in Streamlit
# st.write("### Data Table")
# st.dataframe(df)
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# # Create and display the scatter plot
# st.write("### Scatter Plot of X vs Y Grouped by Gender")

# pivot_df = df.pivot(index="x", columns="gender", values="y")
# st.write(pivot_df)
# st.scatter_chart(pivot_df)



# import streamlit as st
# import pandas as pd
# import time
# import os

# st.title("Clusters")

# html_content1 = """
# <div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: bold; margin-bottom: 28px;">
#     <span style="text-align: left;">Caterpillar Story</span>
#     <span style="text-align: right;">Daily Activities</span>
# </div>
# """

# html_content2 = """
# <div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: bold; margin-top: 0px;">
#     <span style="text-align: left;">Food and Drink</span>
#     <span style="text-align: right;">Communication Words</span>
# </div>
# """
# st.markdown(html_content1, unsafe_allow_html=True)

# column_colors = {
#     "female": "#FF69B4",                  # Example hex color for "female"
#     "male": "#1E90FF",                    # Example hex color for "male"
#     "female w/o transcripts": "#FFB6C1", # Example hex color for "female w/o transcripts"
#     "male w/o transcripts": "#ADD8E6"    # Example hex color for "male w/o transcripts"
# }

# def display_image(container, age):
#     # Define the image path
#     path = f"results/All/scatter/child/{age}.csv"
    
#     if os.path.exists(path):
#         df = pd.read_csv(path)
#         pivot_df = df.pivot_table(index="x", columns="gender", values="y", aggfunc="mean")
#         container.scatter_chart(pivot_df, x_label=f'Ages in Months: {age}', color=[column_colors[col] for col in pivot_df.columns])
#         return True
#     return False

# # Function to loop images as a GIF
# def loop_images(container, frequency):
#     while True:  # Infinite loop to keep cycling through images
#         for age in range(20, 144):
#             if display_image(container, age):
#                 time.sleep(1 / frequency)  # Delay based on the frequency

# # Placeholder for displaying images
# image_container = st.empty()

# # Default to show age 20
# if "default_age_shown" not in st.session_state:
#     st.session_state["default_age_shown"] = True
#     if not display_image(image_container, 20):
#         st.warning("Default image for age 20 is not available.")

# # Age selection
# age = st.sidebar.number_input("Select an age to display", min_value=20, max_value=144, step=1)
# if st.sidebar.button("Show"):
#     if not display_image(image_container, age):
#         st.warning("The selected age does not have an image.")

# # GIF loop
# frequency = st.sidebar.slider("Frequency (images per second)", min_value=1, max_value=10, step=1, value=4)
# if st.sidebar.button("Start Loop"):
#     loop_images(image_container, frequency)



# st.markdown(html_content2, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
import os

st.title("Clusters")
study = st.selectbox("Choose Study", ['Champaign', 'HSLLD'])

html_content1 = """
<div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: bold; margin-bottom: 28px;">
    <span style="text-align: left;">Caterpillar Story</span>
    <span style="text-align: right;">Daily Activities</span>
</div>
"""

html_content2 = """
<div style="display: flex; justify-content: space-between; font-size: 24px; font-weight: bold; margin-top: 0px;">
    <span style="text-align: left;">Food and Drink</span>
    <span style="text-align: right;">Communication Words</span>
</div>
"""
st.markdown(html_content1, unsafe_allow_html=True)

column_colors = {
    "female": "#FF69B4",                  # Example hex color for "female"
    "male": "#1E90FF",                    # Example hex color for "male"
    "female w/o transcripts": "#FFB6C1", # Example hex color for "female w/o transcripts"
    "male w/o transcripts": "#ADD8E6"    # Example hex color for "male w/o transcripts"
}

def display_image(container, age):
    # Define the image path
    path = f"results/{study}/scatter/{age}.csv"
    
    if os.path.exists(path):
        df = pd.read_csv(path)
        pivot_df = df.pivot_table(index="x", columns="gender", values="y", aggfunc="mean")
        container.scatter_chart(pivot_df, x_label=f'Ages in Months: {age}', color=[column_colors[col] for col in pivot_df.columns])
        return True
    return False

# Placeholder for displaying images
image_container = st.empty()

# Default to show age 20
if study == "Champaign":
    if "current_age" not in st.session_state:
        st.session_state["current_age"] = 20

    if "previous_age" not in st.session_state:
        st.session_state["previous_age"] = 20
else:
    if "current_age" not in st.session_state:
        st.session_state["current_age"] = 44

    if "previous_age" not in st.session_state:
        st.session_state["previous_age"] = 44

min_value = 20 if study == "Champaign" else 44

# Sidebar age selection
age = st.sidebar.number_input("Select an age to display", min_value=min_value, max_value=144, step=1)

# Check if the age has changed
if age != st.session_state["current_age"]:
    st.session_state["previous_age"] = st.session_state["current_age"]
    st.session_state["current_age"] = age
    if not display_image(image_container, age):
        st.warning("The selected age does not have an data.")

# Show button to trigger the current image
if st.sidebar.button("Show"):
    if not display_image(image_container, st.session_state["current_age"]):
        st.warning("The selected age does not have data.")

# GIF loop
frequency = st.sidebar.slider("Frequency (images per second)", min_value=1, max_value=10, step=1, value=2)
if st.sidebar.button("Start Loop"):
    while True:  # Infinite loop to keep cycling through images
        for age in range(20, 144):
            if display_image(image_container, age):
                time.sleep(1 / frequency)  # Delay based on the frequency

st.markdown(html_content2, unsafe_allow_html=True)

