import re
import streamlit as st
import joblib


# Load the trained model
model = joblib.load("models/spam_email_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Spam Email Detection",
    page_icon="📧",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📧 Spam Email Detection")

st.write(
    "Paste a complete email below to check whether it is "
    "likely to be spam or not spam."
)


# --------------------------------------------------
# Email Input
# --------------------------------------------------

email_text = st.text_area(
    "Paste your complete email:",
    height=350,
    placeholder="""Subject: Example email

Dear Customer,

Paste the complete email content here...

Thank you,
Sender"""
)


# --------------------------------------------------
# Email Analysis and Prediction
# --------------------------------------------------

if st.button("🔍 Check Email"):

    if not email_text.strip():

        st.warning("Please paste an email before checking.")

    else:

        # Machine learning prediction
        prediction = model.predict([email_text])[0]
        probability = model.predict_proba([email_text])[0]

        # --------------------------------------------------
        # URL Detection
        # --------------------------------------------------

        urls = re.findall(
            r"https?://[^\s]+|www\.[^\s]+",
            email_text
        )

        # --------------------------------------------------
        # Suspicious Word Detection
        # --------------------------------------------------

        suspicious_words = [
            "urgent",
            "winner",
            "prize",
            "claim",
            "free",
            "reward",
            "congratulations",
            "limited time",
            "click here",
            "verify"
        ]

        email_lower = email_text.lower()

        detected_words = [
            word
            for word in suspicious_words
            if word in email_lower
        ]

        # --------------------------------------------------
        # Prediction Result
        # --------------------------------------------------

        st.subheader("🔍 Detection Result")

        if prediction == 1:

            confidence = probability[1] * 100

            st.error("🚨 SPAM")

            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

            st.warning(
                "This email contains patterns associated "
                "with spam. Review the sender and links carefully."
            )

        else:

            confidence = probability[0] * 100

            st.success("✅ NOT SPAM")

            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

            st.info(
                "The model did not detect strong spam patterns "
                "in this email."
            )

        # --------------------------------------------------
        # Email Analysis
        # --------------------------------------------------

        st.subheader("📊 Email Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "URLs Detected",
                len(urls)
            )

        with col2:
            st.metric(
                "Email Characters",
                len(email_text)
            )

        with col3:
            st.metric(
                "Suspicious Words",
                len(detected_words)
            )

        # --------------------------------------------------
        # Warning Signals
        # --------------------------------------------------

        if detected_words:

            st.write("**Detected warning signals:**")

            for word in detected_words:
                st.write(f"⚠️ `{word}`")

        else:

            st.write(
                "✅ No common suspicious warning words detected."
            )


# --------------------------------------------------
# Model Performance
# --------------------------------------------------

st.divider()

st.subheader("📈 Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Accuracy",
        "99.67%"
    )

with col2:
    st.metric(
        "Precision",
        "100%"
    )

with col3:
    st.metric(
        "Recall",
        "98%"
    )

with col4:
    st.metric(
        "F1-Score",
        "98.99%"
    )

st.caption(
    "Performance measured on a held-out test set of 611 emails."
)