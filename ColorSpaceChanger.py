import os
import glob
import cv2 as cv

import streamlit as st
#from main import predict
from PIL import Image
import pandas as pd



# all images in 'images' folder
images = [image for image in glob.glob(os.path.join(r"C:\Users\admin\Desktop\projects\juggling\im", "*.jpg"))]
cs = ["bw","hsv","yuv","lab"]

st.sidebar.title("Color Space Changer")
selected_image = st.sidebar.selectbox("Pick an image.", images)
color_space = st.sidebar.selectbox("Pick a space.", cs)

#selected_model = st.sidebar.selectbox("Pick a model.", models_list)

st.write("Change the color space")

if st.sidebar.button('Changer'):
    showpred = 1
    #prediction, prob = predict(selected_model,os.path.join("images", selected_image))
                                

    #image = Image.open(os.path.join(r"C:\Users\admin\Desktop\projects\juggling\im\00tg.jpg"))
    image = Image.open(selected_image)
    # image = image.resize((128, 128))
    # st.write(prediction)
    
    src = cv.imread(selected_image) 
    if color_space == "bw":
        image = cv.cvtColor(src, cv.COLOR_BGR2GRAY ) 
    if color_space == "hsv":
        image = cv.cvtColor(src, cv.COLOR_BGR2HSV )     
    if color_space == "hsv":
        image = cv.cvtColor(src, cv.COLOR_BGR2YUV )
    if color_space == "hsv":
        image = cv.cvtColor(src, cv.COLOR_BGR2LAB )        
    st.image(image)