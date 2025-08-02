# Require Libraries
import streamlit as st
import pandas as pd
import numpy as np
import time

# Title , Header , Subheader

st.title('Steamlit Title App')
st.header("Streamlit Practice App")
st.subheader('This is Subheader')
st.text('This is Simple Text')
st.markdown("** This is Bold text that we are getting using markdown**")

# Message Function

st.success('Success Messages!!!')
st.warning('Warning Messages!!!')
st.error('Error Based Messages!!!')
st.info("Informational Based Messages!!!")

# Basic Widgets

st.write("### User Input Widgets!!! ")
name = st.text_input('Enter Your Name')
age =  st.number_input('Enter Your Age', min_value=3, max_value=50)
gender = st.radio('Select Gender', ['Male', 'Female', 'None'])
hobbies = st.multiselect('Select Hobbies' , ["Reading", "Music", "Gaming", "Gardening"])
agree = st.checkbox("I Agree all terms and condition that are mentioned above")

if st.button('Submit'):
    st.write(f"Your name is  {name} . Your age is {age} Your Gender is {gender}")
    st.write("The Hobbies that are selected here is: ", hobbies)
    st.write("Agreed!!!", agree)


# Slider SelectionBox

level = st.slider('Choose your Skill Level', 0,20,3)
lang = st.selectbox("Favourite Language That you like the most is:", ["Python", "C", "C++", "JAVA", "ASSEMBLY", "MACHINE LEARNING"])
st.write('Your Skill Level Is :', level)
st.write("Your Favorite Language is:", lang)




# Display Dataframes and tabeles


st.write('### Sample DataFrames')
df = pd.DataFrame({
    'Name': ['Ali', 'Aslam', 'Charlie'],
    'score': [23,54,36]
})
st.dataframe(df)
st.table(df)




#Charts in Streamlit 

st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['Alpha', 'Bravo', 'Charlie'])
st.line_chart(chart_data)

st.header('Bar Chart')
st.bar_chart(chart_data)

st.header("Area Chart")
st.area_chart(chart_data)


# Mapping (If You have co-ordinates)

st.header("Map of the dataset")
map_data = pd.DataFrame(
    np.random.randn(100,2)/ [50,50] + [37.76 , -122.4],
    columns=['latitude', 'longitude']
)

# Adding Images, Audio and Video

st.header("All Media Files Displayed here!!!")
st.image("https://placekitten.com/200/300", caption="Cute Cat", width=200)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")


# forms in streamlit

st.header("Forms in Streamlit App")

with st.form('My Form'):
    user = st.text_input('User Name')
    password = st.text_input('Password', type='password')
    submit = st.form_submit_button('Login')
    if submit:
        st.write("Logged in as:", user)

# State Management
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button('Increment'):
    st.session_state['count'] += 1

st.write('Count =', st.session_state['count'])


# Progress Bar and Spinner in Streamlit

st.header('Progress Bar and Spinner in Streamlit')

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# Spinner Example

with st.spinner('Loading Here!!!'):
    time.sleep(5)
st.success('Done!!!')



# Slider Usage in Streamlit


st.sidebar.title('Sidebar Title')
side_name = st.sidebar.text_input('Enter Your Name:')
st.sidebar.write("Hello Mr!" , side_name)




