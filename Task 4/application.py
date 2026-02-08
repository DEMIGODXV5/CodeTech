import streamlit as st
import joblib

model = joblib.load("spam_classifier_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.title("📧 Email Spam Detection App")
st.write("Enter an email message below to check whether it is **Spam** or **Ham**.")

user_input = st.text_area("Email Text", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text before predicting.")
    else:
        # Transform input
        input_tfidf = tfidf.transform([user_input])

        # Prediction
        prediction = model.predict(input_tfidf)[0]

        # Output
        if prediction == 1:
            st.error("🚨 This email is **SPAM**")
        else:
            st.success("✅ This email is **HAM (Not Spam)**")
