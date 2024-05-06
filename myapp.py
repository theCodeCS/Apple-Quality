import streamlit as st
import pandas as pd
from joblib import load
import pyautogui
 

# Load the dataset
st.title("""
         **Is your Apple Good or Bad Quality? Lets find out!**
         """)

df = pd.read_csv('apple_quality.csv')

################## Preprocessing ##################
df.drop(['A_id', 'Quality'], axis=1, inplace=True)

target = {0: 'Bad Quality', 1: 'Good Quality'}

# Remove last row
df.drop(df.tail(1).index, inplace=True)

# Change typing of Acidity to float
df['Acidity'] = df['Acidity'].astype(float)

################## Sidebar ##################
st.dataframe(df, height=250)

# # Add a selectbox to the sidebar:
st.sidebar.header('User Input Features')

# Collects user input features into dataframe
def user_input_features():
    size = st.sidebar.slider('Size', df['Size'].min(), df['Size'].max(), df['Size'].mean())
    weight = st.sidebar.slider('Weight', df['Weight'].min(), df['Weight'].max(), df['Weight'].mean())
    sweetness = st.sidebar.slider('Sweetness', df['Sweetness'].min(), df['Sweetness'].max(), df['Sweetness'].mean())
    crunchiness = st.sidebar.slider('Crunchiness', df['Crunchiness'].min(), df['Crunchiness'].max(), df['Crunchiness'].mean())
    juciness = st.sidebar.slider('Juiciness', df['Juiciness'].min(), df['Juiciness'].max(), df['Juiciness'].mean())
    ripeness = st.sidebar.slider('Ripeness', df['Ripeness'].min(), df['Ripeness'].max(), df['Ripeness'].mean())
    acidity = st.sidebar.slider('Acidity', df['Acidity'].min(), df['Acidity'].max(), df['Acidity'].mean())
    data = {'Size': size,
            'Weight': weight,
            'Sweetness': sweetness,
            'Crunchiness': crunchiness,
            'Juiciness': juciness,
            'Ripeness': ripeness,
            'Acidity': acidity
            }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

if st.sidebar.button("Reset"):
    pyautogui.hotkey('ctrl', 'r')

st.write('The user input features are:', input_df)

################## Model Prediction ##################

# Load xgboost pipeline model from joblib file
xgb_new = load('apple_quality_xgb.joblib')

# Apply model to make predictions
st.subheader('Prediction')

# Apply model to make predictions
prediction = xgb_new.predict(input_df)

if prediction[0] == 0:
    st.write('This apple is of bad quality.')
    st.image('images/bad_apple.png', use_column_width=True)
else:
    st.write('This apple is of good quality.')
    st.image('images/good_apple.jpg', use_column_width=True)

