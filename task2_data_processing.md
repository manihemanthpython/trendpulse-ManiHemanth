Task 2 — Clean the Data & Save as CSV

TrendPulse: What's Actually Trending Right Now

Marks: 20 | File: task2_data_processing.py

Submission: Push your file to the same public GitHub repo and share the direct link: https://github.com/<username>/trendpulse-<name>/blob/main/task2_data_processing.py


⚠️ Anti-AI Policy: Write your own code. Comments explaining your logic count in your favour.

Needs: The JSON file from Task 1 (data/trends_YYYYMMDD.json)

What to Build

The raw JSON from Task 1 may have messy data — duplicate stories, missing values, wrong types. Your job is to load it with Pandas, clean it up, and save it as a tidy CSV file.

Tasks

1 — Load the JSON File (4 marks)

Load the JSON file from the data/ folder into a Pandas DataFrame

Print how many rows were loaded

2 — Clean the Data (10 marks)

Fix the following issues:

Duplicates — remove any rows with the same post_id

Missing values — drop rows where post_id, title, or score is missing

Data types — make sure score and num_comments are integers

Low quality — remove stories where score is less than 5

Whitespace — strip extra spaces from the title column

Print the number of rows remaining after cleaning.

3 — Save as CSV (6 marks)

Save the cleaned DataFrame to data/trends_clean.csv

Print a confirmation message with the number of rows saved

Also print a quick summary: how many stories per category

Expected Output

Loaded 122 stories from data/trends_20240115.json


After removing duplicates: 120
After removing nulls: 118
After removing low scores: 114

Saved 114 rows to data/trends_clean.csv

Stories per category:
  technology      22
  worldnews       24
  sports          21
  science         24
  entertainment   23


Submission Checklist

 Script runs without errors
 data/trends_clean.csv exists
 Console shows row count at each step
 Stories-per-category summary printed
 Code is commented


Marks Breakdown

Description	Marks
1	Load JSON into a Pandas DataFrame	4
2	Clean the data	10
3	Save as CSV and print summary	6

Total	20

Next: Task 3 will load this CSV and do analysis using Pandas and NumPy.