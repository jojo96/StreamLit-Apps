import os
import glob
import cv2 as cv
import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import streamlit as st
from PIL import Image
import pandas as pd
from io import BytesIO
#chobb scrapped from site

# all images in 'images' folder
#images = [image for image in glob.glob(os.path.join(r"C:\Users\admin\Desktop\projects\juggling\im", "*.jpg"))]
cs = ["xkcd","Calvin and Hobbes"]

st.sidebar.title("The Free Comic Foundation")
#selected_image = st.sidebar.selectbox("Pick an image.", images)
color_space = st.sidebar.selectbox("Pick a comic.", cs)


st.write("Your favorite comic")
ind = 1
if st.sidebar.button('Load Comic'):
    if color_space == "Calvin and Hobbes":
        url = "https://www.gocomics.com/comics/lists/1643242/calvin-and-hobbes-bedtime?page="+str(random.randint(1, 20))                          
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.findAll('img')
        url = images[(random.randint(1, 5))]['src']
        urllib.request.urlretrieve(url, r"C:\Users\admin\Desktop\MEXT\r.jpg")
        image = Image.open(r"C:\Users\admin\Desktop\MEXT\r.jpg")
        st.image(image)
    if color_space == "xkcd":
        url = "https://xkcd.com/"+str(random.randint(1, 1000))+"/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.findAll('img')
        i = 0
        for image in images:
            i = i+1
            if i==3:
                gg = image['src']
                #print(image['src'])
        urllib.request.urlretrieve("https:"+gg, r"C:\Users\admin\Desktop\MEXT\r.jpg")
        image = Image.open(r"C:\Users\admin\Desktop\MEXT\r.jpg")
        st.image(image)
    