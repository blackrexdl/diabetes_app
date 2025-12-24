# 🩺 Diabetes Prediction App  

👋 Welcome to the **Diabetes Prediction System** — a Machine Learning-based web app built using **Python** and **Streamlit**.  
It predicts the likelihood of diabetes in a person based on key medical parameters and provides a clean, user-friendly interface for fast and accurate results.

---

## 📘 Project Overview  
This project applies **Logistic Regression** for diabetes prediction using the **Pima Indians Diabetes Dataset**.  
The app takes user health data such as Glucose, BMI, Blood Pressure, Insulin, and more, then predicts whether the person is likely to have diabetes.  
It’s lightweight, fast, and easy to deploy locally or online.

---

## 🧠 Key Features  
- Interactive and responsive Streamlit UI  
- Real-time prediction based on user inputs  
- Data cleaning and handling of missing values  
- Logistic Regression-based model for accuracy  
- Fast execution with minimal resource usage  
- Simple, readable, and maintainable code  

---

## 🖼️ App Screenshots  

### 🌐 Hosted Website – Home Page  
![Hosted Website Home Page](https://cvws.icloud-content.com/B/AdoV1200kTRcDt2fk6lBPok2YbKnAXUoq8FipmrJtuXhWc6yfGHov3IK/Screenshot+2025-12-24+at+12.23.51%E2%80%AFPM.png)

### 🧩 Web App Interface – Input Form  
![Web App Interface](https://cvws.icloud-content.com/B/Ad8acdgHPy7x5ZDigh6ExRq7q8IRAW8Uy116vbVE4lXdszlD8ms8CMh_/Screenshot+2025-12-24+at+12.26.52%E2%80%AFPM.png)

### 📊 Prediction Result Output  
![Prediction Result](https://cvws.icloud-content.com/B/AaXJAMD8M0YhJZapQwaojgJjCPbkAfPID9WO76h4AXd6htPxVhzBoCid/Screenshot+2025-12-24+at+12.27.03%E2%80%AFPM.png)

---

## 🧩 Tech Stack  
| Component | Technology Used |
|------------|----------------|
| Frontend | Streamlit |
| Backend | Python |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Data Handling | Pandas, NumPy |
| Styling | Custom CSS in Streamlit |
| Recommended IDE | VS Code / PyCharm |

---

## ⚙️ Requirements  
Before starting, ensure these are installed on your system:  
- Python 3.8 or higher  
- pip (Python package manager)  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  

Install all dependencies by running:  
```bash
pip install streamlit scikit-learn pandas numpy
```

---

## 🛠️ Installation & Setup  

### Step 1 — Clone or Download the Project  
If using Git:  
```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
```
If downloaded manually, extract the ZIP file and open it in your preferred IDE (like VS Code).

---

### Step 2 — Create and Activate Virtual Environment  

For macOS / Linux:  
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:  
```bash
python -m venv venv
venv\Scripts\activate
```

---

### Step 3 — Install Required Libraries  
If a requirements.txt file is included:  
```bash
pip install -r requirements.txt
```

Otherwise, install manually:  
```bash
pip install streamlit scikit-learn pandas numpy
```

---

### Step 4 — Run the Application  
Once all dependencies are installed, start the app using Streamlit:  
```bash
streamlit run diabetes_app.py
```

Then open the URL shown in the terminal (usually http://localhost:8501) to access the web app.

---

## 🧪 How It Works  
1. User enters medical details like Glucose, BMI, Blood Pressure, etc.  
2. The model preprocesses and scales the data.  
3. Logistic Regression model predicts the likelihood of diabetes.  
4. The app shows whether the user is likely diabetic or not — with a visual message.

---

## 📊 Dataset Used  
**Pima Indians Diabetes Dataset** — A well-known dataset from the UCI Machine Learning Repository used for binary classification problems.

---

## 🚀 Future Enhancements  
- Integrate Deep Learning models for higher accuracy  
- Add data visualization dashboard  
- Include user authentication  
- Support for multilingual interface  
- Cloud deployment (AWS / Azure / GCP)

---

## 🧾 License  
This project is open-source and available under the MIT License.  

---

## 💬 Acknowledgements  
Special thanks to the open-source contributors and datasets from the UCI Repository that made this project possible.  

Developed with ❤️ using Python and Streamlit.
