import seaborn as sns
import pandas as pd
import numpy as np

# Load and Explore the Data

# /Load data/trends_clean.csv into a Pandas DataFrame
df = pd.read_csv("data/trends_cleaned.csv")

# Display the first 5 rows of the DataFrame to understand its structure
print(f" Displaying First 5 Rows:\n {df.head(5)}")

# Now i'm going to find out the number of rows and columns in the DataFrame
print(f"\n No of Rows:  {df.shape[0]}\n No of columns: {df.shape[1]}")

# finding the average score and average num_comments across all stories
Avg_score = df['score'].mean()
Avg_num_comments = df['num_comments'].mean()
print(f"\n Average Score :{Avg_score:.2f}\n Average Num_comments: {Avg_num_comments:.2f}")

#  Basic Analysis with NumPy
# What is the mean, median, and standard deviation of score?
mean_score = np.mean(df['score'])
median_score = np.median(df['score'])
std_deviation_score = np.std(df['score'])

print(f"\n Mean Score: {mean_score:.2f}\n Median Score: {median_score:.2f}\n Standard Deviation of Score: {std_deviation_score:.2f}")

# What is the highest score and lowest score?
max_score = np.max(df['score'])
min_score = np.min(df['score'])
print(f"\n Highest score :{max_score}\n Lowest score :{min_score}")

# Which category has the most stories?
Most_stories_category = df['subreddit'].value_counts().idxmax()
print(f"\n Category with the most stories: {Most_stories_category}")

# Which story has the most comments? Print its title and comment count.
most_comments_story = df.loc[df['num_comments'].idxmax()]
print(f"\n Story with the most comments Got: {most_comments_story['title']} with {most_comments_story['num_comments']} comments..")

# Now i'm adding New columns to the DataFrame
df["engagement"] =df["num_comments"] / (df['score'] + 1)
print(f"\n Added a new column 'engagement' to the DataFrame:\n{df.head(3)}")

df["is_popular"] = df.apply(lambda row: row['score'] > Avg_score, axis=1)
print(f"\n Added a new column 'is_popular' to the DataFrame:\n {df.head(3)}")


# Save the Resulting DataFrame with the new columns to a new CSV file
df.to_csv("data/trends_analyzed.csv", index=False)
print("\n Analyzed data saved to data/trends_analyzed.csv\n")
