import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API details
API_KEY = '6f426ec4db4712036d3080d867006512'
BASE_URL = 'http://ws.audioscrobbler.com/2.0/'

# Function to fetch data
def get_top_artists():
    params = {
        'method': 'chart.gettopartists',
        'api_key': API_KEY,
        'format': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        artists = [artist['name'] for artist in data['artists']['artist'][:10]]
        listeners = [int(artist['listeners']) for artist in data['artists']['artist'][:10]]
        return pd.DataFrame({'Artist': artists, 'Listeners': listeners})
    else:
        st.error("Error fetching data!")
        return pd.DataFrame()

# Streamlit app layout
st.title("Real-Time Music Trends Dashboard")
st.markdown("**Visualizing the most popular artists right now!**")

# Fetch and display data
df = get_top_artists()
if not df.empty:
    st.dataframe(df)  # Show raw data
    st.bar_chart(df.set_index('Artist'))  # Create bar chart

    # Optional: Add matplotlib visualizations
    fig, ax = plt.subplots()
    ax.pie(df['Listeners'], labels=df['Artist'], autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)
