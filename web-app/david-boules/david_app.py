# -*- coding: utf-8 -*-
"""david_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gg9JP9Q308cnbY7LOoLTnxRCIgAi2cMP
"""

import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os

import os
with open(os.path.join(os.path.dirname(__file__), 'model.pkl'), 'rb') as file:
    model = pickle.load(file)

st.title("Student Performance Predictor")

school = st.radio('Select your School: ', ('GP', 'MS'))
sex = st.radio('Select your Sex: ', ('Male', 'Female'))
address = st.radio('Do you live in a Rural or Urban Area?', ('Rural', 'Urban'))
higher = st.radio('Do you plan on pursuing Higher Education?', ('Yes', 'No'))
internet = st.radio('Do you have Internet Access at home?', ('Yes', 'No'))
Medu = st.radio("Select your Mother's highest education level:", ('None', '4th Grade', '5th - 9th Grade', 'High School', 'Higher Education'))
Fedu = st.radio("Select your Father's highest education level:", ('None', '4th Grade', '5th - 9th Grade', 'High School', 'Higher Education'))
Mjob = st.radio("Select your Mother's job:", ('Teacher', 'Health-Care Related', 'Civil Services', 'Other', 'Stay-at-home'))
reason = st.radio("What is the reason you chose this school?", ('Close to Home', 'Reputation', 'Course Preference', 'Other'))
studytime = st.radio("What is your average weekly study-time?", ('<2 hours', '2-5 hours', '5-10 hours', '10+ hours'))
famrel = st.select_slider("On a scale from 1 to 5, what is the quality of your family relationships? (from 1-very bad to 5-excellent)", [1,2,3,4,5])
freetime = st.select_slider("On a scale from 1 to 5, how much free time do you have after school? (from 1-very low to 5-very high)", [1,2,3,4,5])
goout = st.select_slider("On a scale from 1 to 5, how frequently do you go out with friends? (from 1-very low to 5-very high)", [1,2,3,4,5])
Dalc = st.select_slider("On a scale from 1 to 5, what is your weekday alcohol consumption? (from 1-very low to 5-very high)", [1,2,3,4,5])
Walc = st.select_slider("On a scale from 1 to 5, what is your weekend alcohol consumption? (from 1-very low to 5-very high)", [1,2,3,4,5])
age = st.slider('Input your age:', 15,22)
absences = st.slider('Input your absences:', 0,93)
failures = st.radio('Input your number of past class failures:', (0,1,2,3,4))
G1 = st.slider('Input your first period grade', 0,20)
G2 = st.slider('Input your second period grade', 0,20)

features = [school, sex, address, higher, internet, Medu, Fedu, Mjob, reason, studytime, famrel, freetime, goout, Dalc, Walc, age, absences, failures, G1, G2]
for feature in features:
  print(feature)

for feature in features:
  print(type(feature))

if school == 'GP':
  school = 0
else:
  school = 1

if sex == 'Male':
  sex = 0
else:
  sex = 1

if address == 'Rural':
  address = 0
else:
  address = 1

if higher == 'No':
  higher = 0
else:
  higher = 1

if internet == 'No':
  internet = 0
else:
  internet = 1

if Medu == 'None':
  Medu = 0
elif Medu == '4th Grade':
  Medu = 1
elif Medu == '5th - 9th Grade':
  Medu = 2
elif Medu == 'High School':
  Medu = 3
elif Medu == 'Higher Education':
  Medu = 4

if Fedu == 'None':
  Fedu = 0
elif Fedu == '4th Grade':
  Fedu = 1
elif Fedu == '5th - 9th Grade':
  Fedu = 2
elif Fedu == 'High School':
  Fedu = 3
elif Fedu == 'Higher Education':
  Fedu = 4

if studytime == '<2 hours':
  studytime = 1
elif studytime == '2-5 hours':
  studytime = 2
elif studytime == '5-10 hours':
  studytime = 3
elif studytime == '10+ hours':
  studytime = 4

features = [school, sex, address, higher, internet, Medu, Fedu, Mjob, reason, studytime, famrel, freetime, goout, Dalc, Walc, age, absences, failures, G1, G2]
for feature in features:
  print(feature)

#Create Data Frame with features in the right format
X = pd.DataFrame({'school':[school], 'sex':[sex], 'address':[address], 'higher':[higher], 'internet':[internet], 'Medu':[Medu], 'Fedu':[Fedu], 'studytime':[studytime], 'famrel':[famrel], 'freetime':[freetime], 'goout':[goout], 'Dalc':[Dalc], 'Walc':[Walc], 'age':[age], 'absences':absences, 'failures':[failures], 'G1':[G1], 'G2':[G2]})
X.head()

#Can manually create encoded columns and edit the value manually
X['Mjob_health'] = 0
X['Mjob_other'] = 0
X['Mjob_services'] = 0
X['Mjob_teacher'] = 0

X['reason_home'] = 0
X['reason_other'] = 0
X['reason_reputation'] = 0


if Mjob == 'Health-Care Related':
  X['Mjob_health'] = 1
elif Mjob == 'Civil Services':
  X['Mjob_services'] = 1
elif Mjob == 'Other':
  X['Mjob_other'] = 1
elif Mjob == 'Teacher':
  X['Mjob_teacher'] = 1

if reason == 'Close to Home':
  X['reason_home'] = 1
elif reason == 'Reputation':
  X['reason_reputation'] = 1
elif reason == 'Other':
  X['reason_other'] = 1

X.head()

#Create predict button

if st.button('Predict'):
  prediction = model.predict(X)[0]
  st.success(f'Your predicted score is: {prediction}')

