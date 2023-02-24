import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image
import io

product_df = np.loadtxt("/Users/tanyapaauesongthum/Downloads/product_images.csv",delimiter=",",skiprows=1)
labelspred_df = np.loadtxt("/Users/tanyapaauesongthum/Downloads/labels_pred.csv",delimiter=",",skiprows=1, usecols=(1))

# Title
st.title("Online Retail Store")

if 'randomidx' not in st.session_state:
    st.session_state.randomidx = random.randint(0, 9999)

#randomise user 
# random_user = random.randint(0, 9999)
generate_button=st.button('Generate Random product')

if generate_button:
    st.write(f'product Number: {st.session_state.randomidx}')
    st.session_state.randomidx = random.randint(0, 9999)

random_img = product_df[st.session_state.randomidx].reshape((28, 28))
print(random_img)
fig, ax = plt.subplots()
plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
plt.imshow(random_img)
st.pyplot(fig)

# Generate recommendations
def get_recommendations(randomindex):
    user_cluster = labelspred_df[randomindex]
    cluster_group = labelspred_df==user_cluster
    same_cluster = product_df[cluster_group]
    idx = np.random.randint(len(same_cluster), size=5)
    recommendations = same_cluster[idx,:]
    return recommendations


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show similar items"):
 
    # display the text if the checkbox returns True value
    rec_first = get_recommendations(st.session_state.randomidx)[0,:].reshape((28, 28))
    fig, ax = plt.subplots()

    rec_second = get_recommendations(st.session_state.randomidx)[1,:].reshape((28, 28))
    fig, ax = plt.subplots()
   

    rec_third = get_recommendations(st.session_state.randomidx)[2,:].reshape((28, 28))
    fig, ax = plt.subplots()
   

    rec_fourth = get_recommendations(st.session_state.randomidx)[3,:].reshape((28, 28))
    fig, ax = plt.subplots()
   

    rec_fifth = get_recommendations(st.session_state.randomidx)[4,:].reshape((28, 28))
    fig, ax = plt.subplots()
  

    cols = st.columns(5)
    recommendations =[]
    recommendations.append(rec_first)
    recommendations.append(rec_second)
    recommendations.append(rec_third)
    recommendations.append(rec_fourth)
    recommendations.append(rec_fifth)

    for i in range (5):
        fig, ax = plt.subplots()
        plt.tick_params(left = False, right = False , labelleft = False ,
                    labelbottom = False, bottom = False)
        plt.imshow(recommendations[i])
        cols[i].pyplot(fig)

