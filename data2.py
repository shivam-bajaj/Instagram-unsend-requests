from selenium import webdriver
from selenium.webdriver.common.by import By

# path of extracted zip folder
from credentials import path
import pandas as pd
driver = webdriver.Chrome()
driver.get('file:///'+path+'/followers_and_following/pending_follow_requests.html')
data = driver.find_elements(By.TAG_NAME,'a')
users=[user.text for user in data]
status = ['requested']*len(users)
user_dict ={'username':users,'status':status}
df = pd.DataFrame(user_dict)
df['unsend datetime']=""
df.to_csv('users.csv',index=False)
print(df.head())