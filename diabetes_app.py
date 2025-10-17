import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("diabetes.csv")
for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:
    df[col] = df[col].replace(0, df[col].median())
X = df.drop("Outcome", axis=1)
y = df["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
st.set_page_config(page_title="Diabetes Prediction", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: #0f1117;
    }
    .stApp {
        background-color: #0f1117;
    }
    h1 {
        font-size: 3rem;
        font-weight: 700;
        color: #33c9ff;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stNumberInput > div {
        background-color: #1c1e26;
        border-radius: 10px;
        padding: 10px;
        color: white;
    }
    .stButton button {
        width: 200px;
        height: 50px;
        background-color: #33c9ff;
        color: black;
        border-radius: 30px;
        font-size: 18px;
        font-weight: bold;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #1f81c7;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("<h1>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1.2, 1.2, 1.2], gap="large")

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
    insulin = st.number_input("Insulin", min_value=0, max_value=1000, value=80)

with col2:
    glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)

with col3:
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=33)
center_col = st.columns(3)[1]
with center_col:
    if st.button("Predict"):
        input_df = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness,
                                  insulin, bmi, dpf, age]], columns=X.columns)
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]

        st.markdown("---")
        if prediction == 1:
            st.error("⚠️ You may have **diabetes**. Please consult a doctor.")
        else:
            st.success("✅ You are **not likely** to have diabetes. Stay healthy!")


