Task 4 — Visualizations
TrendPulse: What's Actually Trending Right Now
Marks: 20 | File: task4_visualization.py

Submission: Push your file to the same public GitHub repo and share the direct link: https://github.com/<username>/trendpulse-<name>/blob/main/task4_visualization.py

⚠️ Anti-AI Policy: Write your own code. Comments explaining your logic count in your favour.

Needs: data/trends_analysed.csv from Task 3

What to Build
Load the CSV from Task 3 and create 3 charts using Matplotlib. Then combine them into a single dashboard figure. Save everything as PNG files.

Tasks
1 — Setup (2 marks)

Load data/trends_analysed.csv into a DataFrame
Create a folder called outputs/ if it doesn't exist
Use plt.savefig() before any plt.show() on all charts


2 — Chart 1: Top 10 Stories by Score (6 marks)

Create a horizontal bar chart showing the top 10 stories by score
Use the story title on the y-axis (shorten titles longer than 50 characters)
Add a title and axis labels
Save as outputs/chart1_top_stories.png


3 — Chart 2: Stories per Category (6 marks)

Create a bar chart showing how many stories came from each category
Use a different colour for each bar
Add a title and axis labels
Save as outputs/chart2_categories.png


4 — Chart 3: Score vs Comments (6 marks)

Create a scatter plot with score on the x-axis and num_comments on the y-axis
Colour the dots differently for popular vs non-popular stories (use the is_popular column)
Add a legend, title, and axis labels
Save as outputs/chart3_scatter.png

Bonus — Dashboard (+3 marks)

Combine all 3 charts into one figure:

Use plt.subplots(1, 3) or plt.subplots(2, 2) to lay them out together

Add an overall title: "TrendPulse Dashboard"

Save as outputs/dashboard.png

Expected Output Files

outputs/
├── chart1_top_stories.png
├── chart2_categories.png
├── chart3_scatter.png
└── dashboard.png  (bonus)


Submission Checklist

 Script runs without errors

 3 chart PNG files saved in outputs/

 All charts have a title and axis labels

 Scatter plot uses different colours for popular vs non-popular stories

 Code is commented


Marks Breakdown

        Description	                        Marks
1	Load data and setup	                    2
2	Chart 1 — top stories horizontal bar	6
3	Chart 2 — stories per category bar	    6
4	Chart 3 — score vs comments scatter	    6
    Bonus	    Combined dashboard	        +3
                    Total	                20 (+3)

Pipeline complete!
 All 4 files together — collect → clean → analyse → visualise — make a working data pipeline.