# Imported Needed Libraries
import requests, time, json, os
from datetime import datetime

# What we Needed to collect from Hacker News API or URLS
Top_storys_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
Story_Details_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Now we needed headers to my requests to the Api key
header = {"User=Agent": "TrendPulse/1.0"}

# Category	Keywords to match (case-insensitive)
CATEGORIES ={
    "technology": ["AI", "Software", "Tech", "Code", "Computer", "Data", "Cloud", "API", "GPU", "LLM", "Machine Learning", "Deep Learning", "Programming", "Cybersecurity", "Blockchain", "Cryptocurrency"],
    "worldnews": ["War", "Government", "Country", "President", "Election", "Climate", "Attack", "Global", "Diplomacy", "Conflict", "International", "Policy", "United Nations"],
    "sports": ["NFL", "NBA", "FIFA", "Sport", "Game", "Team", "Player", "League", "Championship", "Tennis", "Cricket", "Olympics", "Soccer", "Baseball"],
    "science": ["Research", "Study", "Space", "Physics", "Biology", "Discovery", "NASA", "Genome", "Astronomy", "Chemistry", "Environment", "Health", "Medicine", "Innovation"],
    "entertainment": ["Movie", "Film", "Music", "Netflix", "Game", "Book", "Show", "Award", "Streaming", "TV", "Celebrity", "Hollywood", "Box Office", "Concert", "Festival", "Theater"]
}
# Now I'm going to creating a function to get the category of the story based on the title
def get_category(title):
    title_lower = title.lower()
    return next((category for category, keywords in CATEGORIES.items() if any(keyword in title_lower for keyword in keywords)), None)

def fatch_hacker_news_trends():
    all_collected_posts = []
    counts = {cat: 0 for cat in CATEGORIES}
    print("Fetching top story IDs.....")
    
    # Now I'm going to fetch the top story IDs from the Hacker News API
    try:
        response = requests.get(Top_storys_url, headers=header)
        # Now I'm going to check if the response is successful or not
        if response.status_code != 200:
            print(f"You can't reach the Hacker News ApI. Status Code: {response.status_code}")
            return
        # Now I'm going to get the first 500 story IDs from the response
        story_ids = response.json()[:500]
    except Exception as e:
        print(f"Error fetching story IDs: {e}")
        return
    # Now I'm going to loop through each story ID to get the details and categorize them
    for story_id in story_ids:
        # Now I'm going to check if we have collected 25 stories for each category or not
        if all(count >= 25 for count in counts.values()):
            break
        try:
            item_response = requests.get(Story_Details_url.format(id=story_id), headers=header)
            if item_response.status_code == 200:
                story = item_response.json()
                
                if story and story.get("type") == "story" and "title" in story:
                    title = story.get("title")
                    category = get_category(title)
                    
                    # Now I'm going to check if the story belongs to a category and if we have collected less than 25 stories for that category
                    if category and counts[category] < 25:
                        post_data = {
                            "post_id"    : story.get("id"),
                            "title"      : title,
                            "category"   : category,
                            "score"      : story.get("score", 0),
                            "num_comments": story.get("descendants", 0),
                            "author"     : story.get("by"),
                            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        all_collected_posts.append(post_data)
                        counts[category] += 1
                        print(f"Found {counts[category]}/25 for {category}: {title[:40]}....")
                        
                        # Now I'm going to wait for 2 seconds after each category loop completion to respect the API rate limits
                        if all(counts[category] == 25 for category in CATEGORIES):
                            print("Waiting for 2 seconds to respect API rate limits...")
                            time.sleep(2)
                            
        except Exception as e:
            print(f"Error fetching story details for ID {story_id}: {e}")
            continue
    # Now I'm going to save the collected posts
    save_data(all_collected_posts)

# Now I'm going to create a function to save the collected data in a JSON file
def save_data(data):
    if not os.path.exists("data"):
        os.makedirs("data")
        
    data_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/trends_{data_str}.json"
    try:
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)
            print("_!_"*23)
            print(f"Data Saved Successfully in {filename}")
    except Exception as e:
        print("_!_"*20)
        print(f"Error Saving Data: {e}")
        print("_!_"*20)
if __name__ == "__main__":
    fatch_hacker_news_trends()