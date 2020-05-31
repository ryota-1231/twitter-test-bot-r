import csv
import datetime
import time
import tweepy
import setting


# キーの取得
CK = setting.API_KEY
CS = setting.API_SECRET_KEY
AT = setting.ACCESS_TOKEN
AS = setting.ACCESS_TOKEN_SECRET

#Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

# ツイート
# api.update_status("Hello World!!")
 
word = ["プログラミング"]
set_count = 2
results = api.search(q=word, count=set_count)

users_list = [] 

for result in results:
    user_id = result.id
    user_name = result.user.name
    tweet = result.text
    user_info = {'user_id': user_id, 'user_name': user_name, 'tweet': tweet}
    users_list.append(user_info)
 
    # username = result.user._json['screen_name']
    # try:
    #     api.create_favorite(user_id)
    #     api.create_friendship(username)
    #     print(user+"をフォローと「いいね」をしました\n\n")
    # except:
    #     print(user+"はもうフォローしてます\n\n")

now = datetime.datetime.now()

with open('tweet_data_{}.csv'.format(now.strftime('%Y%m%d%H%M%S')), 'w') as csv_file:
  fieldnames = ['UserId', 'UserName', 'Tweet']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for user in users_list:
    writer.writerow({'UserId': user['user_id'], 'UserName': user['user_name'], 'Tweet': user['tweet']})
