import pandas as pd

# Load CSV file
file_path = "emails.csv"  # Change this to your actual CSV file path
df = pd.read_csv(file_path)

valid_domains = ["@gmail.com", "@yahoo.com", "@outlook.com"] 

# Assuming the emails are in a column named 'email'
filtered_df = df[df['email'].str.endswith(tuple(valid_domains), na=False)]

# Remove duplicate emails
filtered_df = filtered_df.drop_duplicates(subset=['email'])

# Save the filtered emails to a new CSV file
filtered_df.to_csv("filtered_emails.csv", index=False)

print("Filtered emails saved to 'filtered_emails.csv'")
