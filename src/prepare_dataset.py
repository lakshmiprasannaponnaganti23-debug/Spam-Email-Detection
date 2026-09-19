import os
import email
import pandas as pd
from email import policy
from email.parser import BytesParser


def extract_email_text(file_path):
    """Read an email file and return its subject + body as text."""

    try:
        with open(file_path, "rb") as file:
            message = BytesParser(policy=policy.default).parse(file)

        subject = message.get("subject", "")

        body = ""

        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()

                if content_type == "text/plain":
                    try:
                        body = part.get_content()
                        break
                    except Exception:
                        pass
        else:
            try:
                body = message.get_content()
            except Exception:
                body = ""

        return f"{subject}\n{body}".strip()

    except Exception as error:
        print(f"Could not read {file_path}: {error}")
        return ""


def load_emails(folder_path, label):
    """Read all emails from a folder and assign a label."""

    emails = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            text = extract_email_text(file_path)

            if text:
                emails.append({
                    "email_text": text,
                    "label": label
                })

    return emails


# Project data folders
ham_folder = os.path.join("data", "easy_ham")
spam_folder = os.path.join("data", "spam")

print("Reading normal emails...")
ham_emails = load_emails(ham_folder, 0)

print("Reading spam emails...")
spam_emails = load_emails(spam_folder, 1)

# Combine both types of emails
all_emails = ham_emails + spam_emails

# Create a DataFrame
dataset = pd.DataFrame(all_emails)

# Shuffle the dataset
dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the dataset
output_path = os.path.join("data", "spam_email_dataset.csv")
dataset.to_csv(output_path, index=False)

print("\nDataset created successfully!")
print(f"Total emails: {len(dataset)}")
print(f"Normal emails: {(dataset['label'] == 0).sum()}")
print(f"Spam emails: {(dataset['label'] == 1).sum()}")
print(f"Saved to: {output_path}")