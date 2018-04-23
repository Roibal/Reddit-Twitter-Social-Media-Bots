"""
Example Reddit Bot Functionality
Learn More: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
Created April 5, 2018

step 1: download pycharm for python 3.6
step 2: install PRAW library
step 3: Follow praw quickstart to get new client id/client secret for app
step 4: Put client id/secret on line 18 below
Step 5: run this python script using PyCharm or Upload to Cloud Service
"""

import praw
import time
import random

def run():
    print('Logging Into Reddit...')
    #Create Bot with login and private key - username - password
    bot = praw.Reddit(user_agent='Example Bot 1', client_id='', client_secret='',
        username='', password='')
    print('Logged in')

    subreddit = bot.subreddit('')                          #Enter Subreddit
    for submission in subreddit.stream.submissions():
        print(submission.title)
        author = str(submission.author)
        reply_text = 'hello! u/' + author + ' Welcome to the XYZ sub!  \n \n ' 
        #print(reply_text)
        submission.reply(reply_text)
        time.sleep(3)

if __name__ == '__main__':
    run()
