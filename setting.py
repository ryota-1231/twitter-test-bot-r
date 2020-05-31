# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数の値をAPに代入
API_KEY= os.environ.get("API_KEY") 
API_SECRET_KEY = os.environ.get("API_SECRET_KEY") 
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN") 
ACCESS_TOKEN_SECRET =os.environ.get("ACCESS_TOKEN_SECRET") 













# import csv
# import datetime
# import time
# import tweepy
# import setting


# # # キーの取得
# # CK = setting.API_KEY
# # CS = setting.API_SECRET_KEY
# # AT = setting.ACCESS_TOKEN
# # AS = setting.ACCESS_TOKEN_SECRET

# # #Twitterオブジェクトの生成
# # auth = tweepy.OAuthHandler(CK, CS)
# # auth.set_access_token(AT, AS)

# # api = tweepy.API(auth)

# # # ツイート
# # # api.update_status("Hello World!!")

# # # for status in api.search(q='プログラミング', count=5):
# # #     print('-------------------------------------------')
# # #     #ユーザ名表示
# # #     print('name:' + status.user.name)
# # #     #内容表示
# # #     print(status.text)

 
# # word = ["プログラミング"]
# # set_count = 2
# # results = api.search(q=word, count=set_count)

# # users_list = [] 

# # for result in results:
# #     username = result.user._json['screen_name']
# #     user_id = result.id
# #     # print("ユーザーID："+str(user_id))
# #     user_name = result.user.name
# #     # print("ユーザー名："+user)
# #     tweet = result.text
# #     # print("ユーザーのコメント："+tweet)

# #     user_info = {'user_id': user_id, 'user_name': user_name, 'tweet': tweet}
# #     users_list.append(user_info)
 
# #     # try:
# #     #     api.create_favorite(user_id)
# #     #     api.create_friendship(username)
# #     #     print(user+"をフォローと「いいね」をしました\n\n")
# #     # except:
# #     #     print(user+"はもうフォローしてます\n\n")

# now = datetime.datetime.now()
# s = "tweet_data_{}.csv".format(now.strftime('%Y%MM%DD%HH%SS')

# # with open('tweet_data_{}.csv'.format(now.strftime('%Y%MM%DD%HH%SS')), 'w') as csv_file:
# #   fieldnames = ['UserId', 'UserName', 'Tweet']
# #   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# #   writer.writeheader()
# #   for user in users_list:
# #     writer.writerow({'UserId': user['user_id'], 'UserName': user['user_name'], 'Tweet': user['Tweet']})
