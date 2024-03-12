import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Stars! :star2:")
st.header("Welcome!:sparkles:", divider='rainbow') ## display the header of the page
stars = pd.read_csv('Stars.csv') ## import stars database


if st.button('Show me 50 stars!'): ##button to display the top 50 stars in the database
    st.container().write(stars.head(50),border= True)

## selection for a specific category to show
selection= st.selectbox('What category would you like to look at?',
             ('Brown Dwarf', 'Red Dwarf', 'White Dwarf', 'Main Sequence',
       'Supergiant', 'Hypergiant'))
filter = stars[stars['Star category']==selection]
st.write(filter)
st.caption(f'there are {len(filter)} stars in this category')

# display Radius differences for each category
expand = st.expander("Look at a graph")
expand.scatter_chart(data=stars,x ='Star category', y='Radius (R/Ro)', color ='Star category')
expand.caption(f'Hypergiants are MASSIVE compared to the {selection}!  :fearful:')

# st.caption(f'Have a look at the count of {selection} category in the spectral classes:')
# if st.button('Show me a graph!:star2:'):
    


# side bar
st.subheader('Select a colour to have a look at from the side bar')
colour = st.sidebar.selectbox(
    "Select a colour",
    ('Red', 'Blue White', 'White', 'Yellowish White', 'Blue white',
       'Pale yellow orange', 'Blue', 'Blue-white', 'Whitish',
       'yellow-white', 'Orange', 'White-Yellow', 'white', 'Blue ',
       'yellowish', 'Yellowish', 'Orange-Red', 'Blue white ',
       'Blue-White')
)
new_filter = stars[stars['Star color'] == colour]
st.write(new_filter)
