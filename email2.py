import pandas as pd
import re

# Load CSV file
file_path = "emails.csv"  # Change this to your actual CSV file path
df = pd.read_csv(file_path, dtype=str)  # Read as string to prevent data type issues

# Ensure the email column is treated as a string
df['email'] = df['email'].astype(str)

# Function to extract valid email from messy data
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

# Apply the function to clean emails
df['cleaned_email'] = df['email'].apply(extract_email)

# Remove rows where no valid email was found
df = df.dropna(subset=['cleaned_email'])

# Define the list of domains to exclude
excluded_domains = [
    "@icloud.com", "@gmai.com", "@i.softbank.jp", "@qq.com", "@protonmail.com", "@mgmail.com", 
    "@GMAIL.COM", "@mail.com", "@gmail.con", "@first-land.co.jp", "@incentiv.net", "@tomi.com", 
    "@yahoo.co.jp", "@jcom.zaq.ne.jp", "@proton.me"
]

# Filter Gmail emails only
gmail_df = df[df['cleaned_email'].str.endswith("@gmail.com", na=False)]

# Filter emails that end with any of the excluded domains
excluded_df = df[df['cleaned_email'].str.endswith(tuple(excluded_domains), na=False)]

# Save excluded emails
excluded_df.to_csv("excluded_emails.csv", index=False, columns=['cleaned_email'])

# Remove excluded emails from the original dataset
filtered_df = df[~df['cleaned_email'].str.endswith(tuple(excluded_domains), na=False)]

# Remove duplicates
filtered_df = filtered_df.drop_duplicates(subset=['cleaned_email'])

# Save the cleaned Gmail emails
filtered_df.to_csv("filtered_emails.csv", index=False, columns=['cleaned_email'])

print(f"Filtered Gmail emails saved to 'filtered_emails.csv'. Total unique Gmail emails: {len(filtered_df)}")
print(f"Excluded emails saved to 'excluded_emails.csv'. Total unique excluded emails: {len(excluded_df)}")
