import streamlit as st
import pandas as pd

# Define the data
data = {
    "Bates": {
        "transcripts": {
            "male": 40,
            "female": 44,
        },
        "words": {
            "child": 10861,
            "parent": 34732
        },
        "ages": {
            "age": ["A", "B", "C", "D", "E"],
            "transcripts": [10, 20, 15, 30, 25]
        },
        "gender": {
            "male": 48,
            "female": 52,
            "unsp": 0
        },
        "pca": {
            "child": [0.17134255, 0.07910432, 0.06104795, 0.0396524, 0.03415983, 0.03120775, 0.02875815, 0.02508611],
            "parent": [0.17315044, 0.05814859, 0.05053763, 0.03775561, 0.03439426, 0.03018443, 0.02937335, 0.02556794]
        }
    },
    "Champaign": {
        "transcripts": {
            "male": 29,
            "female": 12
        },
        "words": {
            "child": 378054,
            "parent": 300537
        },
        "ages": {
            "age": ['20', '21', '22', '23', '24', '25', '27', '28', '30', '31', '32', '33', '34', '36', '37'],
            "transcripts": [1, 73, 10, 2, 79, 8, 78, 10, 68, 17, 1, 70, 12, 53, 26]
        },
        "gender": {
            "male": 48,
            "female": 52,
            "unsp": 0
        },
        "pca": {
            "child": [0.10953319, 0.07184249, 0.03679039, 0.03596078, 0.03007334, 0.02303825, 0.01913307, 0.01761913],
            "parent": [0.15225318, 0.05381482, 0.04261236, 0.03371845, 0.03302722, 0.02663543, 0.02545507, 0.02044268]
        }
    },
    "Garvey": {
        "transcripts": {
            "male": 29,
            "female": 12
        },
        "words": {
            "child": 378054,
            "parent": 300537
        },
        "ages": {
            "age": ['34', '35', '36', '37', '38', '39', '42', '43', '45', '48', '49', '53', '55', '57', '58', '60', '61', '62', '63', '64', '67'],
            "transcripts": [2, 2, 1, 4, 2, 1, 4, 1, 1, 3, 1, 2, 1, 3, 1, 2, 6, 3, 2, 1, 2]
        },
        "gender": {
            "male": 48,
            "female": 52,
            "unsp": 0
        },
        "pca": {
            "child": [0.10124855, 0.0814149,  0.05861131, 0.05434228, 0.04431017, 0.04152925, 0.0408812, 0.03527427],
            "parent": [0.15225318, 0.05381482, 0.04261236, 0.03371845, 0.03302722, 0.02663543, 0.02545507, 0.02044268]
        }
    }
}

st.title("Results")
study = st.selectbox("Choose Study", ['Bates', 'Champaign', 'Garvey', 'Hall', 'HSLLD'])

# Calculate percentages
total_transcripts = data[study]["transcripts"]["male"] + data[study]["transcripts"]["female"]
percent_male = (data[study]["transcripts"]["male"] / total_transcripts) * 100
percent_female = (data[study]["transcripts"]["female"] / total_transcripts) * 100

total_words = data[study]["words"]["child"] + data[study]["words"]["parent"]
percent_child_words = (data[study]["words"]["child"] / total_words) * 100

col1, col2 = st.columns(2)

with col1:
    st.subheader("Transcripts")
    st.dataframe([
        {"": "Male", "Count": data[study]["transcripts"]["male"], "Percentage": f"{percent_male:.0f}%"},
        {"": "Female", "Count": data[study]["transcripts"]["female"], "Percentage": f"{percent_female:.0f}%"}
    ], use_container_width=True)

with col2:
    st.subheader("Words")
    st.dataframe([
        {"": "Child", "Count": data[study]["words"]["child"], "Percentage": f"{percent_child_words:.0f}%"},
        {"": "Parent", "Count": data[study]["words"]["parent"], "Percentage": f"{100 - percent_child_words:.0f}%"}
    ], use_container_width=True)



st.subheader("Transcript Counts by Age")
df = pd.DataFrame(data[study]["ages"])
df = df.set_index("age")
st.bar_chart(df, x_label="Number of Transcripts", y_label="Age (months)", horizontal=True)


st.subheader("Child - Explained Variance by Principal Component")
st.line_chart(data[study]["pca"]["child"], x_label="Principal Component", y_label="Explained Variance Ratio")

st.subheader("Parent - Explained Variance by Principal Component")
st.line_chart(data[study]["pca"]["child"], x_label="Principal Component", y_label="Explained Variance Ratio")








