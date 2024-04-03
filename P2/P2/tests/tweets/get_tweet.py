 #!/usr/bin/env python3  

'''
NAME
    get_tweet - Script to extract tweets from a file

SYNOPSIS
    python3 get_tweet.py

DESCRIPTION
    This script reads a file containing tweet data and extracts the tweet texts, it's content.

FILES
    - [Input file]: File containing tweet data to be analyzed
    - extracted_tweets.txt: File where extracted tweets will be saved
'''

import sys

def read_tweets(file_path):
    tweets = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(';')
            #tweet_id = data[0]
            tweet_text = data[1]
            #tweet_date = data[2]
            #sentiment = data[3]
            #query_used = data[4]
            tweets.add(tweet_text)
    return tweets

if __name__ == "__main__":
    file_path = sys.argv[1] # File that we are analysing
    tweets = read_tweets(file_path)
    
    # Displaying the extracted tweets
    with  open("extracted_tweets.txt",'w',encoding="UTF-8") as file:
        for tweet in tweets:
            print("Text:", tweet)
            print()
            file.write(f"{tweet}\n")

