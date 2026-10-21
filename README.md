# Email Phishing Detector

A Python machine-learning prototype that analyzes an email sender, subject, and body to classify the message as likely phishing or legitimate with a percentage score.

## Features

- Web interface built with Streamlit
- Accepts sender address, subject line, and email body
- Produces a phishing-risk score
- Trains a TF-IDF and logistic-regression model from labeled sample emails

## Technologies

- Python
- Streamlit
- pandas
- scikit-learn
- joblib

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
streamlit run app.py
