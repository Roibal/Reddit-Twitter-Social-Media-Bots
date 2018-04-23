"""
The purpose of this bot is to repost high-quality content to various subreddits


"""

import praw
import time
import random

#Create Bot1 with login and private key - username - password
bot1 = praw.Reddit(user_agent='crosspost_bot1 v0.1', client_id='', client_secret='',
    username='', password='')


#Create List of topics to search for (cryptocurrency)
crypto_subject_list = ['Bitcoin', 'BTC', 'Binance', 'Ethereum', 'Litecoin', 'Cryptocurrency', 'Bitconnect']
#Create List of Subreddits to post content from
subreddit_crosspost_list = ['Bitcoin+Cryptocurrency+Cryptomarkets+Cryptotrading']

#Create List of crossposted titles
crosspost_title_list = []

#Time in seconds to pause between crossposts - 10 minutes each acct
pause_time = 60*10

#Go through posts in popular tech subreddit, if matches 'list' of words, crosspost

#Choose dedicated Subreddit (Technology/Business/Politics)
source_sub_lists = ['Cryptocurrency', 'Cryptomarkets']


def run():
    for sub in subreddit_crosspost_list:
        subreddit1 = bot1.subreddit(sub)

        for post in subreddit1.submissions():
            #Create For Loop for words in subject list
            print(post.title)
            for word in crypto_subject_list:
                #check if word is contained in post title
                if word.lower() in post.title.lower():
                    if post.title not in crosspost_title_list:
                        #If cryptocurrency-related post is found, crosspost
                        post.crosspost(random.choice(source_sub_lists))
                        print('crossposted')
                        crosspost_title_list.append(post.title)
                        time.sleep(pause_time)
            time.sleep(1)
            print(crosspost_title_list)

if __name__=='__main__':
    run()
