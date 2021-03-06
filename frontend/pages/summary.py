import streamlit as st
from data import accidents
import seaborn as sns
from matplotlib import pyplot as plt
import pydeck as pdk
from conf import mapbox_key


def write():
    st.title('General overview of the accidents in Bogotá')

    accidents_by_year = accidents.sample(frac=0.2)
    # st.table(data)

    COLOR_BREWER_BLUE_SCALE = [
        [240, 249, 232],
        [204, 235, 197],
        [168, 221, 181],
        [123, 204, 196],
        [67, 162, 202],
        [8, 104, 172],
    ]

    # print(accidents_by_year.info())

    layer = pdk.Layer(
            "HeatmapLayer",
            accidents_by_year[['x','y','severity_numeric']],
            opacity=0.9,
            get_position=["x", "y"],
            aggregation='"MEAN"',
            color_range=COLOR_BREWER_BLUE_SCALE,
            threshold=1,
            get_weight="severity_numeric",
            pickable=True
        )

    st.pydeck_chart(pdk.Deck(
      map_style='mapbox://styles/mapbox/dark-v9',
      mapbox_key=mapbox_key,
      initial_view_state=pdk.ViewState(
          latitude=4.654335,
          longitude=-74.083644,
          zoom=11,
        #   pitch=50,
      ),
      layers=[layer],
    ))

    st.text('Please note that plots were calculated using 2015 - 2019 accident data.')
    # st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
    st.write("select a category to view.")

    ############################################# by year
    by_year = accidents['year'].value_counts(sort=True).rename_axis('year').reset_index(name='accident_count').sort_values(by='year').reset_index(drop=True)
    by_year
    #st.header('Yearly accidents.')
    if st.button('Yearly accidents'):
        placeholder1 = st.empty()
        if not st.checkbox("Hide"):  # st.checkbox("Hide Yearly accidents"):
            f, ax = plt.subplots(figsize=(27, 16))
            sns.set(style="whitegrid",font_scale=2)
            ticks = [x for x in range(2015, 2020)]
            sns.lineplot(by_year.year, by_year.accident_count, color='red')
            plt.xlabel('Year', fontsize=40)
            plt.xticks( ticks, rotation=90, fontsize=30)
            plt.yticks(fontsize=30)
            plt.ylabel('Number of Accidents', fontsize=40)
            st.pyplot()
    else:
        st.write(' ')   

    #############################################
    # st.header('Percent change in yearly accidents.')
    if st.button('Percent change in yearly accidents'):
        placeholder1 = st.empty()
        if not st.checkbox("Hide"):  # st.checkbox("Hide Percent change in yearly accidents"):
            # st.subheader('Percent change in yearly accidents')
            by_year['percent_change'] = by_year.accident_count.pct_change()
            f, ax = plt.subplots(figsize=(28, 16))
            sns.set(style="whitegrid",font_scale=2)
            ticks2 = [x for x in range(2015, 2020)]              
            sns.lineplot(by_year.year, by_year.percent_change, color='b')
            # plt.title('Percent change in yearly accidents', fontsize =20)
            plt.xlabel('Year', fontsize=40)
            plt.xticks( ticks2, rotation=90, fontsize=30)
            plt.yticks(fontsize=30)
            plt.ylabel('Number of Accidents', fontsize=40)
            st.pyplot()
    else:
        st.write(' ') 
    ###############################################

    ############################################# by month
    by_month = accidents['month'].value_counts(sort=True).rename_axis('month').reset_index(name='accident_count').sort_values(by='month').reset_index(drop=True)
    months={1:'January',2:'February',3:'March',4:'April',
        5:'May',6:'June',7:'July',8:'August',
        9:'September',10:'October',11:'November',12:'December'}
    #st.header('month accidents.')
    if st.button('Monthly accidents'):
        placeholder1 = st.empty()
        if not st.checkbox("Hide"):  # st.checkbox("Hide monthly accidents"):
            f, ax = plt.subplots(figsize=(27, 28))
            sns.set(style="whitegrid",font_scale=2)
            ticks = [months[x] for x in range(1, 13)]
            sns.lineplot(by_month.month, by_month.accident_count, color='red')
            plt.xlabel('Month', fontsize=40)
            plt.xticks(range(1, 13), ticks, rotation=90, fontsize=30)
            plt.yticks(fontsize=30)
            plt.ylabel('Number of Accidents', fontsize=40)
            st.pyplot()
    else:
        st.write(' ')   
    
    ###############################################
    ############################################# by month
    by_day_of_week = accidents['day_of_week'].value_counts(sort=True).rename_axis('day_of_week').reset_index(name='accident_count').sort_values(by='day_of_week').reset_index(drop=True)
    day_of_weeks={1:'Monday',2:'Tuesday',3:'Wednesday',
        4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    #st.header('day_of_week accidents.')
    if st.button('Accidents by day of the week'):
         placeholder1 = st.empty()
         if not st.checkbox("Hide"):  # st.checkbox("Hide day_of_weekly accidents"):
            f, ax = plt.subplots(figsize=(27, 29))
            sns.set(style="whitegrid",font_scale=2)
            ticks2 = [day_of_weeks[x] for x in range(1, 8)]
            sns.lineplot(by_day_of_week.day_of_week, by_day_of_week.accident_count, color='red')
            plt.xlabel('Day of the Week', fontsize=40)
            plt.xticks(range(0, 8), ticks2, rotation=90, fontsize=30)
            plt.yticks(fontsize=30)
            plt.ylabel('Number of Accidents', fontsize=40)
            st.pyplot()
    else:
        st.write(' ') 

    ############################################# by hour
    by_hour = accidents['hour'].value_counts(sort=True).rename_axis('hour').reset_index(name='accident_count').sort_values(by='hour').reset_index(drop=True)

    #st.header('hour accidents.')
    if st.button('Accidents by hour'):
         placeholder2 = st.empty()
         if not st.checkbox("Hide"):  # st.checkbox("Hide hourly accidents"):
            f, ax = plt.subplots(figsize=(27, 12))
            sns.set(style="whitegrid",font_scale=2)
            sns.lineplot(by_hour.hour, by_hour.accident_count, color='red')
            plt.xlabel('Hour', fontsize=40)
            plt.ylabel('Number of Accidents', fontsize=40)
            plt.xticks(fontsize=30)
            plt.yticks(fontsize=30)
            st.pyplot()
    else:
        st.write(' ') 




