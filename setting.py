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