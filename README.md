# 🎬 Movie Success Predictor

A simple ML-powered Streamlit web app that predicts whether a movie will be a success or flop based on various input features.
 
---
## Dataset : 

  https://drive.google.com/file/d/1BIyhH9icwlQKmlUc9sPeVTcEN7hZgyEe/view?usp=drive_link

 ![image](https://github.com/user-attachments/assets/a1a745e7-76c3-46a7-8943-ff11dd463dc9)

-Sucess:![image](https://github.com/user-attachments/assets/44c6320e-83d2-4055-8c08-7af8df2ad63d)

-Flop:![image](https://github.com/user-attachments/assets/f9cf4ba1-f854-4025-b8c6-02f30d7229f7)


## 🚀 Features

- User-friendly web interface
- Predict movie success using trained ML model
- Interactive inputs for budget, ratings, votes, popularity, etc.
- Success/Failure animations using Lottie
- Fully customizable

---

## 📦 Tech Stack

- Python 3.x
- Streamlit
- Scikit-learn
- NumPy
- Joblib
- Requests
- streamlit-lottie

---

## 🛠️ Setup Instructions

### 1️⃣ Clone this repository

```bash
 git clone https://github.com/rahulp00/movie-success-predictor.git
 cd movie-success-predictor
```

2️⃣ Install dependencies

pip install streamlit scikit-learn numpy joblib requests streamlit-lottie

3️⃣ Make sure your trained model file model.pkl is present in project directory.

    You can train your model using your dataset and save using joblib:

import joblib
joblib.dump(model, 'model.pkl')

4️⃣ Run the Streamlit app

streamlit run app.py

🎯 Input Features

    Budget (in $)

    Runtime (minutes)

    Popularity score

    Average rating

    Total votes

    Release year

    Number of genres

📝 Author

Made with ❤️ by Rahul Prajapati
