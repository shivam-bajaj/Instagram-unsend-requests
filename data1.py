from selenium import webdriver
from selenium.webdriver.common.by import By

# path = path of extract zip folder
from credentials import path
import pandas as pd
driver = webdriver.Chrome()
#path of folder
driver.get('file:///'+path+'/followers_and_following/pending_follow_requests.html')
users=[]
data = driver.find_elements(By.CLASS_NAME,'_a6-p')
for i in data:
    u = i.text.split('\n')
    u.append('requested')
    users.append(u)
df = pd.DataFrame(users,columns=['username','request datetime','status'])
df['unsend datetime']=""
df.to_csv('users.csv',index=False)