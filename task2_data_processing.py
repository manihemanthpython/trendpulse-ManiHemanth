import json
import pandas as pd
import seaborn as sns

# Now I'm going to create a function to load the collected data from the JSON file

df = pd.read_json("data/trends_20260402.json")
total_records = len(df)


# Duplicates — remove any rows with the same post_id

df.drop_duplicates(subset=['post_id'], keep='first', inplace=True)

# Missing values — drop rows where post_id, title, or score is missing

df.dropna(subset=['post_id', 'title', 'score'], inplace=True)

# Data types — make sure score and num_comments are integers
# fillna(0) is used to replace any missing values in the 'num_comments' columns with 0 before converting them to integers. This ensures that we don't encounter errors when trying to convert NaN values to integers.
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].fillna(0).astype(int)

# Low quality — remove stories where score is less than 5
df = df[df['score'] >= 5]

# Whitespace — strip extra spaces from the title column
df['title'] = df['title'].str.strip()


print(f"\nTotal no of records Loaded: {total_records} file data/trends_20260402.json")
print(f"Total no of records after removing duplicates and missing values: {df.shape[0]}")
print(f"Total no of records after cleaning: {len(df)}\n")

# Now I'm going to save the cleaned data in a new CSV file
df.to_csv("data/trends_cleaned.csv", index=False)
print("Cleaned data saved to data/trends_cleaned.csv\n")
print(f"Columns in the cleaned DataFrame labels:\n {df.columns}\n")
print(f"A Quick Summary of stories per category:\n {df['subreddit'].value_counts()}\n")

