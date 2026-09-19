import joblib


# Load the trained model
model = joblib.load("models/spam_email_model.pkl")

print("Spam Email Detection")
print("--------------------")
print("Paste the complete email below.")
print("When you finish, type END on a new line.")
print("Type EXIT on a new line to stop.\n")


while True:
    print("Enter email:")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        if line.strip().upper() == "EXIT":
            print("Program ended.")
            exit()

        lines.append(line)

    email_text = "\n".join(lines).strip()

    if not email_text:
        print("Please enter an email.\n")
        continue

    prediction = model.predict([email_text])[0]
    probability = model.predict_proba([email_text])[0]

    if prediction == 1:
        confidence = probability[1] * 100
        print("\n🚨 Prediction: SPAM")
        print(f"Confidence: {confidence:.2f}%")
    else:
        confidence = probability[0] * 100
        print("\n✅ Prediction: NOT SPAM")
        print(f"Confidence: {confidence:.2f}%")

    print("\n" + "-" * 40 + "\n")