import joblib
import streamlit as st

st.set_page_config(page_title="Email Phishing Detector")

# Load the trained machine-learning model.
model = joblib.load("models/phishing_model.pkl")

st.title("Email Phishing Detector")
st.write("Paste an email below to check whether it may be phishing.")

sender = st.text_input("Sender email address")
subject = st.text_input("Email subject")
body = st.text_area("Email body", height=250)

if st.button("Analyze Email"):
    if not body.strip():
        st.warning("Please paste an email message first.")
    else:
        # Combine the information in the same format used for training.
        email_text = f"{sender} {subject} {body}"

        # Make a prediction and calculate the phishing probability.
        prediction = model.predict([email_text])[0]
        probabilities = model.predict_proba([email_text])[0]
        phishing_index = list(model.classes_).index("phishing")
        phishing_risk = probabilities[phishing_index] * 100

        if prediction == "phishing":
            st.error(f"⚠️ Likely phishing — Risk score: {phishing_risk:.0f}%")
            st.write("Do not click links or share personal information until you verify the sender.")
        else:
            st.success(f"Likely legitimate — Phishing risk: {phishing_risk:.0f}%")

        st.subheader("Email analyzed")
        st.write("Sender:", sender)
        st.write("Subject:", subject)