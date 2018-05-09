"""
The Purpose of this Reddit Bot is to collect replies to a particular thread, then save to a .txt file

"""

import time
import random
import praw
from samplekeys import rkey

c_id = rkey['client_id']
c_secret = rkey['client_secret']
usr_name = rkey['username']
passw = rkey['password']

#Create Reddit Bot with login and private key - username - password
bot = praw.Reddit(user_agent='Collecting Replies into Spreadsheet bot1 v0.1', client_id=c_id, client_secret=c_secret,
    username=usr_name, password=passw)

def run():
    #Collect Recent Thread, Collect Comments, Format Comment, Save to .txt file
    print("-----------------\n\nHello and Welcome to A Reddit Bot which collects replies into spreadsheet")
    print("This Bot will collect thread replies and save as text file with author and comment")
    print("-----------------\n\n")
    time.sleep(2)
    subreddit1 = 'd100'      #Subreddit to collect replies
    num_threads = 10        #Number of Threads to collect replies (number of files will be made)
    comment_list = []       #New Comment List will be created for each 'thread'/file
    for submission in bot.subreddit(subreddit1).top(limit=num_threads):
        print("Submission Title:    ", submission.title)   #Submission Title will become FileName
        file_name = str(submission.title.replace(" ", "_"))+".txt"
        print(file_name)
        print("Submission URL:      ", submission.url)                           #Save URL just in case
        #print(submission.date)
        comment_list.append(['URL', str(submission.url)])       #Append URL to List
        comment_list.append([str(submission.author), submission.selftext.replace("\n", " ")])
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print("Comment:     ", comment.body)
            print("Author:      ", comment.author)
            comment_list.append([str(comment.author), comment.body.replace("\n", " ")])
            print(comment_list)
            #time.sleep(15)
        write_file(comment_list, file_name)
        time.sleep(30)

def write_file(list1, filename):
    #Submit format in list form: ['Author', 'Comment']
    with open(filename, 'w') as f:
        for msg in list1:
            f.write("\n"+msg[0] +", " + msg[1])

if __name__=="__main__":
    run()
