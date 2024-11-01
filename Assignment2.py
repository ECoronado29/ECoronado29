import requests
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#Fetch top stories
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = requests.get(top_stories_url).json()

story_ids = story_ids[:5]

for story_id in story_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story = requests.get(story_url).json()
    
    #Add the story author as a node if it exists
    story_author = story.get("by")
    if story_author:
        G.add_node(story_author, label="story_author")
    
    #Fetch comments for the story
    if "kids" in story:
        for comment_id in story["kids"]:
            comment_url = f"https://hacker-news.firebaseio.com/v0/item/{comment_id}.json"
            comment = requests.get(comment_url).json()
            comment_author = comment.get("by")
            
            #Add comment author as a node if it exists
            if comment_author:
                G.add_node(comment_author, label="comment_author")
                G.add_edge(story_author, comment_author)

#Visualize network
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Simplified Hacker News Interaction Network")
plt.show()

