import pandas as pd

# Load CSV file
file_path = "emails.csv"  # Change this to your actual CSV file path.
df = pd.read_csv(file_path)

# Assuming the emails are in a column named 'email'
gmail_df = df[df['email'].str.endswith('@gmail.com', na=False)]  # Keep Gmail emails
non_gmail_df = df[~df['email'].str.endswith('@gmail.com', na=False)]  # Keep non-Gmail emails

# Remove duplicates from both datasets
gmail_df = gmail_df.drop_duplicates(subset=['email'])
non_gmail_df = non_gmail_df.drop_duplicates(subset=['email'])

# Save filtered emails to separate CSV files
gmail_df.to_csv("filtered_emails1.csv", index=False)
non_gmail_df.to_csv("non_gmail_emails.csv", index=False)

print(f"Filtered Gmail emails saved to 'filtered_emails.csv'. Total unique Gmail emails: {len(gmail_df)}")
print(f"Non-Gmail emails saved to 'non_gmail_emails.csv'. Total unique non-Gmail emails: {len(non_gmail_df)}")
