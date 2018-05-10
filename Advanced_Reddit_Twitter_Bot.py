"""
The purpose of this python script (Bot) is to create a Twitter Bot using Tweepy.
Also Interacts on Reddit to promote links, gain Karma
The Twitter Bot will like, repost and follow accounts related to cryptocurrencies (Bitcoin, Ethereum and Steem) and
Political Twitter Accounts

Created January 19, 2018
Modified May 5, 2018

Copyright 2018 Joaquin Roibal
"""

#import dependencies - tweepy for twitter - praw for reddit
import tweepy
import time
import random
import praw
from samplekeys import keys, keys2, keys3, rkey
import urllib.request

c_id = rkey['client_id']
c_secret = rkey['client_secret']
usr_name = rkey['username']
passw = rkey['password']

list_of_accts = [keys, keys2, keys3]
#Oauth consumer key/secret and token/secret from twitter application
consumer_key = keys3['consumer_key']
consumer_secret = keys3['consumer_secret']

access_token = keys3['access_token']
access_token_secret = keys3['access_token_secret']

#Authorization for Tweepy format
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Create Reddit Bot with login and private key - username - password
bot = praw.Reddit(user_agent='Post_bot1 v0.2', client_id=c_id, client_secret=c_secret,
    username=usr_name, password=passw)

def run():
    print("-------------------------------------------")
    print("Initializing Advanced Reddit/Twitter Bot - Loading Lists of Accounts/URL's\n")
    i=0         #Counter For Number of Loops Iterated
    try:
        #Create List of Subreddits to source content
        subreddit_list = read_file('Subreddits_List.txt') #Load List from Text File which will be used for Subreddits
        print("Subreddit List: ", subreddit_list)
        #create 'whitelisted' words for cryptocurrency & Business/Politics
        crypto_words = read_file('Crypto_Words_List.txt')
        print("Crypto Words: ", crypto_words)
        biz_word_list = read_file('Biz_Words_List.txt')
        print("Biz Word List: ", biz_word_list)
        #Create Lists of Popular Twitter Accounts to Follow, Retweet, Favorite (Interact)
        pop_users = read_file('Popular_Twitter_List.txt')
        print("Popular Users: ", pop_users)
        #Create 'Blacklist' of Twitter Accounts
        accts_unfollow_list = read_file('Unfollow_Twitter_List.txt')
        print("Accounts Unfollow List: ", accts_unfollow_list)
        #Create List of Cryptocurrency/Blockchain Related Accounts
        crypto_user_list = read_file('Crypto_User_List.txt')
        print("Crypto User List: ", crypto_user_list)
        #Create List of URL's to Promote
        blog_url_list = read_file('Blog_URL_List.txt')
        print("Blog URL List: ", blog_url_list)
        #print(api.rate_limit_status())
        number_fav = 20
        num_to_follow = 5

        usr_list = ['BlockchainEng']        #Enter Twitter Account to Promote
        print("Successfully Loaded Accounts & URL's. Continuing to Bot Functionality.\n\n")
    except:
        print("Loading of Accounts & URL's Failed")

    while 1:
        #Infinite Loop which Calls all functions (favorite/RT/Follow/Post)
        print("-------------------------------------------------------\nStarting Roibal Crypto Bot \n\n\n")
        time.sleep(15)
        i+=1
        bit_url_list=[]
        crosspost_title_list = []
        try:
            usr_list1 = crypto_user_list+pop_users
            source_urls_reddit(subreddit_list, bit_url_list)        #Collect URLs from Reddit
            if i ==1:
                for i in range(0,len(blog_url_list)):
                    blog_url_list.append(random.choice(bit_url_list))     #Create list 50% blog, 50% collected URLs
            print(blog_url_list)
            #post to Reddit - Limit once every 10 minutes - Post Blog URL's
            post_to_reddit(subreddit_list, blog_url_list)
            follow_accounts(usr_list1, num_to_follow, accts_unfollow_list)
            #xpost_reddit(subreddit_list)
            favorite(usr_list1, number_fav, accts_unfollow_list)
            time.sleep(240)
            fav_rt_timeline_tweets(accts_unfollow_list, number_fav, crypto_user_list)
            #Through each infinite loop post crypto-related post from Reddit (30% Chance of each occurring)
            rand_int = random.randint(0,100)
            if rand_int<60:
                post_twitter(bit_url_list, biz_word_list, crypto_words, crypto_user_list)
                print("Tweeted URL from Reddit!")
            elif rand_int>90:
                crypto_follow(crypto_words, crypto_user_list)
                print("Follow Crypto Posted!")
                #unfollow(crypto_user_list)
            else:
                post_twitter(blog_url_list, biz_word_list, crypto_words, crypto_user_list)
                print("Posted Blog URL to Twitter!")
            time.sleep(15)
        except:
            print("ERROR!!\n\n")
            time.sleep(5)

def write_file(list1, filename):
    with open(filename, 'a') as f:
        for user in list1:
            f.write("\n"+user)

def read_file(filename1):
    list1=[]
    with open(filename1, 'r') as f1:
        list1=list(f1.read().split('\n'))
    return list1

def findTitle(url):
    webpage = urllib.request.urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

def favorite(username_list, fav_num, user_ban_list):
    #Using Cursor format to access tweets for given screen name
    #For each Username in List of Usernames:
    rand_usr_list =[]
    j = 0
    for i in range(0,3):
        rand_usr_list.append(random.choice(username_list))
    for user_list in rand_usr_list:
        if user_list in user_ban_list:
            break
        #create counter for number of tweets to favorite (fav_num)
        i = 0
        #For Each status
        for status in tweepy.Cursor(api.user_timeline, id=user_list).items():
            #Print Status and Print ID of Tweet (for Favoriting)
            print(status.text)
            j+=1
            time.sleep(1)
            #Check if status has been favorited previously, if not, favorite
            if api.get_status(status.id).favorited is False:
                api.create_favorite(status.id)
                i+=1
                time.sleep(15)
            if i>fav_num or j>15:
                break
            print(i)

def post_to_reddit(sub_list, url_list):
    sub = random.choice(sub_list)
    subr = bot.subreddit(sub)
    url1 = random.choice(url_list)
    title1 = findTitle(url1)
    print(title1)
    subr.submit(title=title1, url=url1)
    print("Submitted to Reddit - Sub: {} Link: {}".format(sub, url1))
    time.sleep(5)

def xpost_reddit(post_sub_lists):
    print("XPost Bot Working")
    source_sub = random.choice(post_sub_lists)
    post_sub = random.choice(post_sub_lists)
    print(source_sub, post_sub)
    if source_sub == post_sub:
        post_sub=random.choice(post_sub_lists)
    subreddit1 = bot.subreddit(source_sub)
    for post in subreddit1.top('week'):
        #Create For Loop for posts in Subreddit Lists
        print(post.title)
        time.sleep(2)
        if random.randint(0,100)<10:
            post.crosspost(post_sub)
            print('Cross-posted {} from {} to {}'.format(post.title, source_sub, post_sub))
            time.sleep(5)
            break

def trending():
    trends_avail = api.trends_available()
    print(trends_avail)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("Limit Handle Exceeded. Sleeping for 7 minutes.")
            time.sleep(7 * 60)

def unfollow(safe_list):
    bceng = api.get_user(screen_name='BlockchainEng')
    if bceng.friends_count>4965:
        #friend_list = api.friends_ids(screen_name='BlockchainEng')
        #for friend in friend_list:
        # NOTE: Switched to Cursor Format
        for friend_info in limit_handled(tweepy.Cursor(api.friends).items()):
            print(friend_info)
            #friend_info = api.get_user(friend)
            #print(friend_info)
            time.sleep(3)
            print("LANGUAGE: ", friend_info.lang)
            print("Info on", friend_info.screen_name, "\n friends: ", friend_info.friends_count, ' followers: ', friend_info.followers_count)
            print("\n Status Count: ", friend_info.statuses_count)

            if friend_info.screen_name in safe_list:
                break
            elif not str(friend_info.lang) == 'en' or not str(friend_info.lang) == 'en-gb':
                api.destroy_friendship(friend_info)
                print(friend_info.screen_name, " was unfollowed!!    LANGUAGE\n \n")
            elif int(friend_info.followers_count)<100 or friend_info.statuses_count<50:
                api.destroy_friendship(friend_info)
                print(friend_info.screen_name, " was unfollowed!! \n \n")
            elif int(friend_info.followers_count)<1000 and friend_info.statuses_count>10000:
                api.destroy_friendship(friend_info)
                print(friend_info.screen_name, " was unfollowed!! \n \n")


def follow_accounts(list_of_accounts, num_to_follow, user_ban_list):
    rand_list =[]
    for i in range(0,3):
        rand_list.append(random.choice(list_of_accounts))
    for account in rand_list:
        #print(list_friends)
        api.create_friendship(screen_name=account)
        print("Friended!!", account)
        time.sleep(10)
        if account in user_ban_list:
            break
        for usr_id in tweepy.Cursor(api.friends_ids, screen_name=account).items(num_to_follow):
            #If user is not followed by @crypto_king2, follow:
            #if api.friends(user_account, usr_id) is False:
            usr1=api.get_user(id=usr_id)
            if usr1.screen_name not in list_of_accounts:
                if usr1.screen_name == '':
                    pass
                else:
                    usr_sn_list=[]
                    usr_sn_list.append(usr1.screen_name)
                    print(usr_sn_list)
                    write_file(usr_sn_list, 'Popular_Twitter_List.txt')
                    print(usr1.screen_name, "Added to Popular User List Text File!")
            api.create_friendship(id=usr_id)
            print('Friended!!', usr_id, usr1.screen_name)
            time.sleep(15)

        """i=0
        if account is not 'BarackObama':
            for acct in api.friends_ids(account):
                usr_screen_name = api.get_user(acct).screen_name
                print(usr_screen_name)
                #If user is not followed by @crypto_king2, follow:
                if api.friends(user_account, usr_screen_name) is False:
                    api.create_friendship(id=acct)
                    print('Friended!!')
                    i+=1
                    time.sleep(5)
                        #Append followed accounts to list 20% of time
                if random.randint(0,100)<20:
                    #list_of_accounts.append(usr_screen_name)
                    pass
                print(acct)

                if i>num_to_follow:
                    break
        #if len(list_of_accounts)>10:
            #break
            """


def fav_rt_timeline_tweets(ban_list, num_fav, crypto_usr_list):
    #Access / Display Tweets to main page
    #display tweets on home timeline printed to console
    #public_tweets = api.home_timeline()            Switched to cursor format
    for tweet in tweepy.Cursor(api.home_timeline).items(num_fav):
        print(tweet.text)
        #Search text of tweet for user in crypto_usr_list (described above), if found give 25% chance to retweet
        #:

        if tweet.author.screen_name in crypto_usr_list:
            api.retweet(tweet.id)
            print("Retweeted!!!")
            time.sleep(random.randint(5,10))

        if api.get_status(tweet.id).favorited is False:
            if tweet.author.screen_name in ban_list:
                pass
            else:
                api.create_favorite(tweet.id)
                print('FAVORITED')
                time.sleep(random.randint(10,20))


def source_urls_reddit(subreddit_crosspost_list, bit_url_list):
    #A function to source popular content from Reddit (URL's)
    for sub in subreddit_crosspost_list:
        i=0
        subreddit1 = bot.subreddit(sub).top('week')

        for post in subreddit1:
            #print(post.url)
            #Create List of 15 URL's Containing Cryptocurrency Words
            if '.com' in post.url and post.url not in bit_url_list:
                bit_url_list.append(post.url)
                i+=1
            if i>5:
                break
    return bit_url_list

def post_twitter(bit_url_list, biz_word_list, crypto_word_list, cc_list):
    #post a URL from previously collected list to twitter with 2 hashtags & 2 Accounts CC'd
    url1=random.choice(bit_url_list)
    status=url1 + "\n \n via @BlockchainEng\n \n#" + random.choice(crypto_word_list) + " #" + random.choice(crypto_word_list)
    status += "\n \ncc: @" + random.choice(cc_list) + " @" + random.choice(cc_list)
    api.update_status(status)
    print(status)

def crypto_follow(crypto_word_list, crypto_usr_list):
    #This Function posts a collection of high-value twitter accounts with 'Follow' statement attached
    usr_list = []
    while len(usr_list)<6:
        rand_usr = random.choice(crypto_usr_list)
        if rand_usr not in usr_list:
            usr_list.append(rand_usr)
    status = "Follow Best #Cryptocurrency & #Blockchain Related Accounts on @Twitter: \n \n"
    status += "@" + usr_list[0] + "\n@"+ usr_list[1] + "\n@" + usr_list[2] + "\n@"+ usr_list[3] + "\n@"+ usr_list[4] \
              + "\n@" + usr_list[5] + "\n \n#" + random.choice(crypto_word_list)
    status += "\n \nFollow, Favorite & RT to support!"
    api.update_status(status)
    print(status)

if __name__ == '__main__':
    run()
