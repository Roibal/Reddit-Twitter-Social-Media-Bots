"""

The purpose of this python script is to create a Twitter Bot using Tweepy.
The Twitter Bot will like, repost and follow accounts related to cryptocurrencies (Bitcoin, Ethereum and Steem) and
Political Twitter Accounts

Created January 19, 2018

Copyright 2018 Joaquin Roibal

"""

#import dependencies - tweepy for twitter - praw for reddit
import tweepy
import time
import random
import praw
from samplekeys import keys, keys2, keys3

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
bot = praw.Reddit(user_agent='Post_bot1 v0.1', client_id='', client_secret='',
    username='', password='')

def run():

    #Create List of Subreddits to source content
    subreddit_crypto_list = ['Bitcoin', 'Cryptocurrency', 'Ethereum', 'Ripple', 'CryptoTraderNetwork']
    sub_post_list = ['Bitcoin', 'CryptocurrencyTrading', 'BitcoinMarkets', 'CryptoTraderNetwork', 'Cryptotrader', 'Cryptomarkets', 'Crypto_currency_News', 'cryptocurrencies', 'altcoin']
    subreddit_crypto_list += sub_post_list
    #Create New List, to add people who will then be used to follow new accounts
    #api.create_list(name='Current News', description='Best Accounts on Twitter for News')

    #create 'whitelisted' words for cryptocurrency
    crypto_words = ['Bitcoin', 'Blockchain', 'Ethereum', 'BTC', 'ETH', 'Cryptocurrency', 'Crypto', 'Cryptocurrencies',
                    'BlockchainTechnology', 'cryptomarkets', 'cryptotrading', 'BlockchainEngineering', 'Tokens', 'InvestInCrypto',
                    'InvestInBlockchain', 'CryptoTraders', 'CryptoTraderBot']
    biz_word_list = ['Business', 'Politics', 'Technology', 'Tech']
    abq_list = ['ewhitmore', 'MayorKeller', 'cabq', 'kindpirates', 'CVF_NewMexico', 'swsantafe', 'goabqid',
                'RepLujanGrisham', 'SenatorTomUdall', 'KUNMNews', 'UNM', 'NMSenateDems']
    user_list_2 = ['AlexisGirlNovak', 'hardball', 'TheEllenShow', 'ESPN', 'NBA', 'Warriors',
                   'ViceNews', 'CNN', 'AntDavis23', 'boogiecousins', 'SenSanders', 'SInow', 'CBSNews', 'bpopken',
                   'MSNBC', 'espn', 'SRuhle', 'JoyAnnReid', 'Lawrence', 'maddow', 'kasie', 'AliVelshi', 'ABC', 'APPolitics',
                   'CoinDesk', 'BitcoinMagazine', 'FEhrsam', 'NFL', 'SenSchumer', 'AdamSchiffCA', 'USATODAY', 'JoeNBC', 'NBATV',
                   'AyyDubs', 'SportsCenter', 'SC_ESPN', 'CNBC', 'RevJJackson', 'RealBillRussell', 'SusanSarandon',
                   'tictoc', 'KobeBryant', 'CBSNews', 'ABC', 'HermEdwards', 'katiecouric', 'ObamaFoundation', 'StephenAtHome',
                   'WashingtonPost', 'MariaTeresa1']
    accts_unfollow_list = ['TwitterSupport', 'FoxNews', 'NRA', 'realDonaldTrump', 'DevinNunes', 'CBP', 'PrisonPlanet',
                           'VitalikButerin', 'chiefynduom', 'BreitbartNews', 'RT_News', 'Musically', 'TwitterMoments',
                           'TaiLopez', 'ProductHunt', 'Lawrence', 'blockchaindaisy']
    crypto_user_list = ['CryptoCobain', 'Cryptopathic', 'CryptOrca', 'Crypto_God', 'piggydeveloper', 'VentureCoinist',
                        'ThinkingUSD', 'caneofc', 'joezabb', 'CryptoCred', 'CommunityFundCC', 'dr_hodes', 'cryptomocho',
                        'Coin_Shark', 'SilverBulletBTC', 'crypto_rand', 'CryptoBanger', 'anambroid', 'cryptomickey',
                        'cz_binance', 'VitalikButerin', 'cointelegraph', 'aantonop', 'CryptoChoe', 'surfcoderepeat',
                        'cryptoallstarz', 'nondualnelly', 'coinyeezy', 'naval', 'AriDavidPaul', 'SatoshiLite',
                        'fluffypony', 'CryptoBully', 'notsofast', 'CryptoMessiah', 'cryptodemedici', 'needacoin',
                        'Bitfinexed', 'CryptoHustle', 'NeerajKA', 'missNatoshi', 'Crypto_Bitlord', 'loomnetwork',
                        'DecentralizedTV', 'CryptoKitties', 'jeffehh', 'whalepool', 'whalecryptogirl', 'arrington', 'ricburton',
                        'cryptoecongames', 'mindandtrading', '_tm3k', 'dwaltchack', 'VinnyVo44', 'velvet_campbell',
                        'AmandaGutterman', 'EtherealSummit', '2Sumeet', 'BlockChannel', 'Ossettia', 'justinsuntron',
                        'EvaBeylin', 'saifedean', 'annairrera', 'BITQueen_BR', 'Pacoiin', 'nondualrandy']
    blockchain_usr_list = ['StewartEsq', 'WallerMaDev', 'AppletonDave', 'PdqJones', 'Obale', 'KristovAtlas', 'jrbedard',
                           'sbetamc', 'jeremyalmond', 'Logvinov_Leon', 'iam_preethi', 'uzyn', 'NickSzabo4', 'EthereumDenver',
                           'bc_workshop', 'thebc_connector', 'PropyInc', 'ngladkikh', 'JimmySong', 'daostack',
                           'blockchaincap', 'ShapeShift_io', 'metamask_io', 'LeValleyKelly', 'davidlknott', 'BlockchainCTR',
                           'EthereumNetw', 'IBMBlockchain', 'IBMBlockchain', 'UCLA_Blockchain', 'BlockchainCTR', 'BlockchainInfos', 'ChainDynamics',
                           'CarrascosaCris_', 'BlockchainEDU', 'bc_workshop', 'iurimatias', 'atxblockcollect', 'crypto', 'Women4Blockcha1',
                           'BlockchainUG', 'cryptradr', 'TheReal_Wolf_', 'vergecurrency', 'tronfoundation']
    num_to_fav=5
    blog_url_list = ['http://www.medium.com/@BlockchainEng',
                     'https://t.co/IdDTdtSBOi',
                     'https://t.co/O0GCmlgLwT', 'https://www.youtube.com/watch?v=Y4RwD1OGz4c',
                     'https://www.youtube.com/watch?v=pjLzJcj3kV0']
    print(api.rate_limit_status())
    number_fav = 5
    num_to_follow = 3
    crypto2_user_list = blockchain_usr_list + crypto_user_list
    crypto_user_list = blockchain_usr_list + crypto_user_list + user_list_2 +abq_list
    crosspost_title_list = []
    usr_list = ['BlockchainEng']
    while 1:
        bit_url_list=[]
        #favorite(crypto2_user_list, 4, accts_unfollow_list)
        #Calls all functions (favorite/RT/Follow/Post)
        print("-------------------------------------------------------\nStarting Roibal Crypto Bot \n\n\n")
        try:
            source_urls_reddit(subreddit_crypto_list, bit_url_list)
            #repost to Reddit
            xpost_reddit(crypto_words, crosspost_title_list, sub_post_list, blog_url_list)
            time.sleep(random.randint(15, 360))
            post_twitter(bit_url_list, biz_word_list, crypto_words, crypto2_user_list)
            time.sleep(random.randint(10,120))
            #Through each infinite loop post crypto-related post from Reddit
            if len(bit_url_list)>0 and random.randint(0,100)<30:
                favorite(crypto_user_list, num_to_fav, accts_unfollow_list)
                post_twitter(bit_url_list, biz_word_list, crypto_words, crypto2_user_list)
                print("Tweeted!")
        except:
            pass

        try:
            if random.randint(0,100)<8:
                crypto_follow(crypto_words, crypto2_user_list)
                print("Follow Crypto Posted!")
                unfollow(crypto_user_list)
            else:
                fav_rt_timeline_tweets(usr_list, crypto_words, accts_unfollow_list, number_fav, crypto_user_list, blog_url_list)
                post_twitter(blog_url_list, biz_word_list, crypto_words, crypto2_user_list)
            #favorite(blockchain_usr_list, num_to_fav, accts_unfollow_list)
        except:
            pass

        try:
            xpost_reddit(crypto_words, crosspost_title_list, sub_post_list, blog_url_list)
            time.sleep(630)
        except:
            pass

        try:
            #follow_accounts(crypto_user_list, num_to_follow, accts_unfollow_list)
            xpost_reddit(crypto_words, crosspost_title_list, sub_post_list, blog_url_list)
        except:
            pass
        time.sleep(random.randint(15,120))
        #Post link to Blog every 1 in 5 loops
        if random.randint(0,100)<20:
            post_twitter(blog_url_list, biz_word_list, crypto_words, crypto2_user_list)
        else:
            fav_rt_timeline_tweets(usr_list, crypto_words, accts_unfollow_list, number_fav, crypto_user_list, blog_url_list)
        time.sleep(random.randint(60, 360))      #sleep 20-30 minutes (random) through each iteration

def favorite(username_list, fav_num, user_ban_list):
    #Using Cursor format to access tweets for given screen name
    #For each Username in List of Usernames:
    rand_usr_list =[]
    for i in range(0,3):
        rand_usr_list.append(random.choice(username_list))
    for user_list in rand_usr_list:
        if user_list in user_ban_list:
            break
        #create counter for number of tweets to favorite (fav_num)
        i = 0
        j = 0
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
                time.sleep(20)
            if i>fav_num or j>15:
                break
            print(i)

def xpost_reddit(crypto_word_list, crosspost_title_list, post_sub_lists, url_list):
    sub = random.choice(['Bitcoin', 'Ripple', 'Cardano', 'CryptoTraderNetwork', 'Cryptocurrency', 'Crypto_Currency_News', 'Ethereum'])
    subreddit1 = bot.subreddit(sub)
    posted=0
    print("XPost Bot Working")
    for post in subreddit1.top('week'):
        #Create For Loop for words in subject list
        print("TEST")
        print(post.title)
        if posted==0:
            if random.randint(0,100)<75:
                #if random.randint(0,100)<25:
                #    subreddit1.submit(title1, url=random.choice(url_list))
                #else:
                pass
            else:
                for word in crypto_word_list:
                    #check if word is contained in post title
                    if word.lower() in post.title.lower():
                        if post.title not in crosspost_title_list:
                            #If cryptocurrency-related post is found, crosspost
                            post.crosspost(random.choice(post_sub_lists))
                            print('Crossposted {}'.format(post.title))
                            crosspost_title_list.append(post.title)
                            time.sleep(5)
                            posted=1
                            break
        else:
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
        if account in user_ban_list:
            break
        for usr_id in tweepy.Cursor(api.friends_ids, screen_name=account).items(num_to_follow):
            #If user is not followed by @crypto_king2, follow:
            #if api.friends(user_account, usr_id) is False:
            api.create_friendship(id=usr_id)
            print('Friended!!', usr_id)
            time.sleep(10)

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


def fav_rt_timeline_tweets(usr_list, crypto_word_list, ban_list, num_fav, crypto_usr_list, url_list):
    #Access / Display Tweets to main page
    #display tweets on home timeline printed to console
    #public_tweets = api.home_timeline()            Switched to cursor format

    for usr_name in usr_list:
        i=0

        if usr_name in ban_list:
            break
        for tweet in tweepy.Cursor(api.home_timeline, id=usr_name).items(num_fav):
            print(tweet.text)
            #Search text of tweet for user in crypto_usr_list (described above), if found give 25% chance to retweet
            #:
            """
            if 'RT' not in tweet.text and tweet.author.screen_name not in crypto_usr_list:
                    status ='@'+str(tweet.author.screen_name) + ' Are you interested in #Cryptocurrencies ?' \
                    + ' Feel Free to Check out my blog!   ' \
                            + random.choice(url_list) + "  #Blockchain #BlockchainTechnology"
                    api.update_status(status, in_reply_to_status_id=tweet.id)
            """
            if tweet.author.screen_name in crypto_usr_list:
                if random.randint(0,100)<60:
                    api.retweet(tweet.id)
                    print("Retweeted!!!")
                    time.sleep(random.randint(5,10))

            if api.get_status(tweet.id).favorited is False:
                api.create_favorite(tweet.id)
                print('FAVORITED')
                time.sleep(random.randint(15,30))
                i+=1
                print(i)
            if i>num_fav:
                break

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
            if i>15:
                break
    return bit_url_list

def post_twitter(bit_url_list, biz_word_list, crypto_word_list, cc_list):
    #post a URL from Subreddit to twitter with 2 hashtags
    url1=random.choice(bit_url_list)
    status=url1 + "\n \n via @BlockchainEng\n \n#" + random.choice(crypto_word_list) + " #" + random.choice(crypto_word_list)
    status += "\n \ncc: @" + random.choice(cc_list) + " @" + random.choice(cc_list)
    api.update_status(status)
    print(status)

def crypto_follow(crypto_word_list, crypto_usr_list):
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
