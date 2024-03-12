import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import MinMaxScaler
# import requirements.txt

st.title("Stars! :star2:")
st.header("Welcome!:sparkles:", divider='rainbow') ## display the header of the page
stars = pd.read_csv('Stars.csv') ## import stars database

## selection for a specific category to show
selection= st.selectbox('What category would you like to look at?',
                ('Brown Dwarf', 'Red Dwarf', 'White Dwarf', 'Main Sequence',
        'Supergiant', 'Hypergiant'))

if st.button('Show me stars!'): ##button to display the top 50 stars in the database
    # st.container().write(stars.head(50),border= True)
    filter = stars.loc[stars['Star category']==selection]
    catContain = st.container()
    with  catContain:
        st.write(filter)
        st.caption(f'there are {len(filter)} {selection} stars')


# display Normalised Radius differences for each category
        ##Scaling the Data
stars_copy = stars[['Radius (R/Ro)']]
minmax = MinMaxScaler()
minmax.fit(stars_copy)
star_scale = minmax.transform(stars_copy)

expand = st.expander("Have a look at the Radius of each type:")
expand.bar_chart(data=stars,x ='Star category', y=stars_copy, color ='Star category',height=3000)
expand.caption(f'Hypergiants are MASSIVE compared to the {selection}!  :fearful:')
# catContain()
# st.caption(f'Have a look at the count of {selection} category in the spectral classes:')
# if st.button('Show me a graph!:star2:'):
st.image('https://images.unsplash.com/photo-1504805572947-34fad45aed93?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')  
## ask user to enter a number and display the temperature of that star 

## Add in ML here for classification prediciton

# side bar
# st.subheader('Select a colour from the side bar to filter the table below')
# colour = st.sidebar.selectbox(
#     "Select a colour",
#     ('Red', 'Blue White', 'White', 'Yellowish White', 'Blue white',
#        'Pale yellow orange', 'Blue', 'Blue-white', 'Whitish',
#        'yellow-white', 'Orange', 'White-Yellow', 'white', 'Blue ',
#        'yellowish', 'Yellowish', 'Orange-Red', 'Blue white ',
#        'Blue-White')
# )
# new_filter = stars.loc[stars['Star color']== colour]
# st.write(new_filter)
# st.caption(f'there are {len(new_filter)} stars whose colour is {colour}')

## Sidebar to change pages to ML
# page2_path = 'Digital Futures/Streamlit exercise/myapp_pg2.py'
# if st.sidebar.button('Machine Learning Model'):
#     st.switch_page(page='Streamlit exercise/myapp_pg2.py')
# st.page_link('Streamlit exercise/myapp_pg2.py')
