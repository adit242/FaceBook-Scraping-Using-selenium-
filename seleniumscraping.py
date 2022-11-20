from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from bs4 import BeautifulSoup
import regex as re
import streamlit as st

import http.cookiejar
# import urllib.request
from urllib.request import urlparse,urljoin
import urllib

import requests
import yake
# import bs4

from webdriver_manager.chrome import ChromeDriverManager


st.title("Facebook Popular Topic Extraction")

mail = st.text_input("Email",)

pwrd = st.text_input("Password",type='password')

# topicNo = st.number_input("Enter no. of topics")


url = 'https://mbasic.facebook.com/profile'
if st.button("Submit") and mail!="" and pwrd:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(2)
    email = driver.find_element("name","email")
    pswrd = driver.find_element("name","pass")
    email.send_keys(mail)
    time.sleep(1)
    pswrd.send_keys(pwrd)
    time.sleep(3)
    email.submit()
    # time.sleep(10)
    # driver.get()
    element = driver.find_element(By.XPATH,"//*[@id='root']/table/tbody/tr/td/div/form/div/input")
    driver.execute_script("arguments[0].click();", element)

    # time.sleep(10)

    # print(.submit())
    
    data_set = ""
    limit = 5


    for i in range (limit):
        pageContent = driver.page_source
        soup = BeautifulSoup(pageContent,"html.parser")
        # content = soup.find_all('p')

        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        for para in soup.find_all('p')+soup.find_all('header'):
            data_set+=para.get_text()
        # time.sleep(5)
        driver.execute_script("arguments[0].click();",driver.find_element(By.LINK_TEXT,"See more stories"))

    # time.sleep(10)
    # data = ""

    # res = [idx for idx in data_set if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]

    print(data_set)
    # print(res)

    # print(type(data_set))


    kwSet = []
    ans=[]
    prevscore = 0
    kw_extractor = yake.KeywordExtractor(top=25, stopwords=None)
    keywords = kw_extractor.extract_keywords(data_set)
    for kw, v in keywords:
        if (v not in kwSet) and v-prevscore>0.001 : 
            ans.append(kw)
            kwSet.append(v)
            prevscore=v
            print("Keyphrase: ",kw, ": score", v)
    

    st.subheader("Popular Words On Your Feed : ")
    st.write(ans[:4])
    # print(keywords)
    driver.close()
    # for kw,v in keywords :
        # if(kw[0] )
