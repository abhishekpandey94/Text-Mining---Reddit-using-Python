# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:45:00 2019

@author: abhishekpandey
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:15:22 2018

@author: abhishekpandey
"""


import praw
import os
os.chdir("C:\\Users\\abhishekpandey\\Desktop")



# creating and authenticating Python Reddit Connection
reddit = praw.Reddit(client_id='xxxxxxxx',
                     client_secret='xxxxxx',
                     password='xxxxxxx',
                     user_agent= 'app name by /u/username',
                     username=' reddit username')


print(reddit.user.me())

#Creating placeholder files to write posts filtered by categories  - #Hot/top posts, New post, comments, etc 

file1= "reddit_hot_post.txt"
file2= "reddit_new_post.txt"
file3= "reddit_comments.txt"

# Extracting 200 hot / trending posts

with open(file1,'w+') as post_file:
    for submissions in reddit.subreddit('Subreddit_name').top(limit=200):
        print(submissions.title)
        try:
            {
              post_file.write(submissions.title)
            }
        except:
            {
              print("error")
            }
        post_file.write("\n")

post_file.close()

# Extracting 200 new posts
    
with open(file3,'w+') as newpost_file:
    for new_submissions in reddit.subreddit('Subreddit_name').new(limit=200):
        print(new_submissions.title) 
        try:
            {
              newpost_file.write(new_submissions.title)
            }
        except:
            {
              print("error")
            }
        newpost_file.write("\n")
        
newpost_file.close()    

# Extracting Comments for a specific posts
with open(file2,'w+') as comment_file:
    
    urls = {'A list of URL for the posts for which comments have to be extracted'} 
            
            
    for link in urls:
        
        submission =reddit.submission(url=link)
      
        for top_level_comment in submission.comments:
            
                 i=i+1   
                 print(top_level_comment.body)
                 
                 try:
                     {
                                        comment_file.write(top_level_comment.body)                      
                     }
                 
                 except Exception :
                      print("error")
                      pass
                     
          
    print("no of comments for the post: ",i)

    
comment_file.close()

# For extracting all comments/ trees for a particular subreddit
for comments in reddit.subreddits('subreddit_name').comments(limit=1000):
    with open(file3,'w+') as comment_file:
        try:
            {
              comment_file.write(comments)
            }
        except:
            {
              print("error")
            }
        comment_file.write("\n")
    comment_file.close()    
