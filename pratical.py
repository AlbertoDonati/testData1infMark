#I made this document with Colab.

max_results = 1500

pip install snscrape

import os
import pandas as pd
from datetime import date

today = date.today()
end_date = today

search_term = 'covid'
from_date = '2019-01-01'

extracted_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-search '{search_term} until:{end_date}' > extracted-tweets.txt"
os.system(extracted_tweets)
df = pd.read_csv('extracted-tweets.txt', names=['content'])
for row in df['content'].iteritems():
  print(row)

df2 = pd.read_csv('extracted-tweets.txt', names=['content'])

cS = df2['content']
a = ""
for x in cS:
      a = x + a

print(a)

d = a.split(' ')
print(d)

file2write=open("users1.txt",'w')

for words in d:
  if(words.startswith('@')):
    print(words)
    file2write.write(words + '\n')

file2write.close()

dfu1 = pd.read_csv('users1.txt', names=['users1'])

#I have extracted some users with snscrape.
#I have not access to twitter API at now.
#I write the other code like pseudo Python code.

userExtracted1 = dfu1

#Check which users have at least 1000 followers
  #I take 50 of them

counterOfMyUser = 0

for user in userExtracted1:
  if twitterAPI.GET_NUMBER_OF_FOLLOWERS(user) > 1000:
    listOfMyUser = listOfMyUser + user
    counterOfMyUser = counterOfMyUser + 1
    if counterOfMyUser > 50:
      break

#I take the detail from users
for user in listOfMyUser:
      usersDetails['user'] = user
      usersDetails['name'] = twitterAPI.GET_NAME(user)
      usersDetails['description'] = twitterAPI.GET_DESCRIPTION(user)
      usersDetails['number_of_followers'] = twitterAPI.GET_NUMBER_OF_FOLLOWERS(user)
      usersDetails['number_of_following'] = twitterAPI.GET_NUMBER_OF_FOLLOWING(user)
      usersDetails['date_of_birthday'] = twitterAPI.GET_DATE_OF_BIRTHDAY(user)
      usersDetails['date_of_creation'] = twitterAPI.GET_DATE_OF_CREATION(user)
      usersDetails['url'] = twitterAPI.GET_URL(user)

#I take the IDs of the posts
for user in listOfMyUser:
    usersPostIdList['user'] = user
    usersPostIdList['post_id'] = twitterAPI.GET_LIST_OF_ID_POST(user)

usersPostIdList50['user'] = usersPostIdList['user'].iloc[50]
usersPostIdList50['post_id'] = usersPostIdList['post_id'].iloc[50]

#I take details from posts
for post_id in usersPostIdList50['post_id']:
      postDetails['user'] = usersPostIdList50['user']
      postDetails['post_id'] = usersPostIdList50['post_id']
      postDetails['number_of_favorites'] = users.twitterAPI.GET_NUMBER_OF_FAVORITES(post_id)
      postDetails['number_of_retweets'] = users.twitterAPI.GET_NUMBER_OF_RETWEETS(post_id)
      postDetails['number_of_replies'] = users.twitterAPI.GET_NUMBER_OF_REPLIES(post_id)

#sum, mean and median of posts
usersPostIdListOther = usersPostIdList

for post_id in usersPostIdListOther['post_id']:
  userPostIdListOther['date'] = users.twitterAPI.GET_DATE_POST(post_id)

numberOfTweetsPerDay = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='D')).sum()
numberOfTweetsPerWeek = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='W')).sum()
numberOfTweetsPerMonth = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='M')).sum()

meanOfTweetsPerDay = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='D')).mean()
meanOfTweetsPerWeek = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='W')).mean()
meanOfTweetsPerMonth = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='M')).mean()

medianOfTweetsPerDay = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='D')).median()
medianOfTweetsPerWeek = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='W')).median()
medianOfTweetsPerMonth = usersPostIdListOther.groupby(pd.Grouper(key='date', freq='M')).median()

#I think it is important the median of tweet per week, because per day is not enough to evaluate a behaviour of a user and per month is too much.
#I think median is the correct parameter to catch for determinate a realistic behaviour of a user about posting.
