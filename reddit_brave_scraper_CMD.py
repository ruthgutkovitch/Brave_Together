import praw
import pandas as pd
from datetime import datetime as dt
import sys

"""
Ahalan!
this little program scrapes posts from reddit.
it use's API accses information which you can get in our WhatsApp group.
if you don't know it - you probebly shouldn't use it :) .
when you have that info, just print it insted of the line 'enter API info here' (line 25).
after that you can use it thrue the cmd like that:
python brave_scraper.py output_csv_file_name.csv serach_vale_1 serach_vale_2 ...
all the post's data export to a .csv file. 
goodluck!
"""

def get_reddit_search_data(reddit, keyowrd, max_results_amount = 10):
    posts_list = []

    for word in keyowrd:
        search_posts = reddit.subreddit('all').search(word, limit = max_results_amount)
        for post in search_posts: 
            if post not in posts_list:
                posts_list.append([post.title, post.id, post.subreddit, post.url, post.selftext, dt.fromtimestamp(post.created)]) # fromtimestamp convert timestamp to regular type`

    return posts_list

def main():

    reddit = praw.Reddit('enter API info here')

    posts = get_reddit_search_data(reddit, sys.argv[2:])
    posts = pd.DataFrame(posts,columns=['title','id', 'subreddit', 'url', 'body', 'created'])
    
    posts.to_csv(sys.argv[1], index=False)
    
    print('done with', len(posts), 'results')
    
    return 0
    
if __name__ == "__main__":
    main()
