# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:05:16 2022

@author: T430s
"""

# streamlit covid-19 analysis app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Covid-19 Analysis
###### This app analyze the covid-19 case/death by country till mid May, 2022--by A. Maharjan
#### Choose the options from the left sidebar 
""")
st.write('---')


import pickle
# opening the file, the date_reported column is already converted to date-time format
with open('df_covid', 'rb') as f: # wb = write binary file
    df = pickle.load(f)
   
    
# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Select the Country')

country_case = st.sidebar.selectbox('Select Country For Cases', df['Country'].unique())
if st.sidebar.button('Covid Cases over Time'):
    df_country_case = df[df.Country == country_case]
# New cases by country
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    plt.figure()
    plt.plot(df_country_case['Date_reported'],df_country_case['New_cases'],'bo')
    plt.ylabel('New Covid Cases')
    plt.xticks(rotation=90)
    plt.title(country_case)
    plt.show()
    st.pyplot()
    
st.sidebar.write('---')

country_death = st.sidebar.selectbox('Select Country For Deaths', df['Country'].unique())
if st.sidebar.button('Covid Deaths over Time'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    df_country_death = df[df.Country == country_death]
    #plt.figure()
    plt.plot(df_country_death['Date_reported'],df_country_death['New_deaths'],'r-')
    plt.ylabel('New Deaths')
    plt.title(country_death)
    plt.xticks(rotation=90)
    plt.show()
    st.pyplot()
 
st.sidebar.write('---')

country = st.sidebar.selectbox('Select', df['Country'].unique())
# correlation between cases and deaths
if st.sidebar.button('Press for Case vs Deaths by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    df_country = df[df.Country == country]
    #plt.figure()
    plt.plot(df_country['New_cases'],df_country['New_deaths'],'bo')
    plt.xlabel('New_cases')
    plt.ylabel('New_deaths')
    plt.title(country)
    plt.show()
    st.pyplot()


st.sidebar.write('---')

# top 20 deaths by country
if st.sidebar.button('Top 20 Deaths by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    df_mostdeaths = df.groupby('Country')['New_deaths'].sum()
    df_mostdeaths = df_mostdeaths.sort_values(ascending=False)[0:20]
    df_mostdeaths.plot(kind='bar')
    plt.ylabel('No of deaths')
    plt.title('Top deaths by country')
    
    st.pyplot()
    df_mostdeaths

st.sidebar.write('---')

# top case vs deaths correlation on a single plot
# subplots together
df_confirmed = df.groupby('Country')['New_cases'].sum().sort_values(ascending=False)[0:20]
df_deaths = df.groupby('Country')['New_deaths'].sum().sort_values(ascending=False)[0:20]

if st.sidebar.button('Top 20 Cases/Deaths by Country'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.bar(df_confirmed.index, df_confirmed, color='g')
    ax2.plot(df_confirmed.index, df_deaths, color='blue', lw=6)
    ax1.set_xlabel('Country',size = 20)
    ax1.set_ylabel('Total Cases', color='g',size = 20)
    ax2.set_ylabel('Total Deaths', color='b',size = 20)
    ax1.set_xticks(df_confirmed.index)
    ax1.set_xticklabels(df_confirmed.index, rotation='vertical', size=12)
    plt.title('Top 20 Case/Deaths by Country')
    plt.show() 
    st.pyplot()

st.sidebar.write('---')
import pickle
# opening the file, the date_reported column is already converted to date-time format
with open('dfUSA_covid', 'rb') as f: # wb = write binary file
    df_usa = pickle.load(f)


df_usa_case = df_usa.groupby('state')['new_case'].sum()
df_usa_death = df_usa.groupby('state')['new_death'].sum()
    

if st.sidebar.button('USA Cases and Deaths by States'):
    st.set_option('deprecation.showPyplotGlobalUse', False) # not to print the error message
    fig, ax3 = plt.subplots()
    ax4 = ax3.twinx()
    ax3.bar(df_usa_case.index, df_usa_case, color='b')
    ax4.plot(df_usa_case.index, df_usa_death, color='green', lw=3)
    ax3.set_xlabel('State',size = 12)
    ax3.set_ylabel('Total Cases', color='b',size = 12)
    ax4.set_ylabel('Total Deaths', color='g',size = 12)
    ax3.set_xticks(df_usa_case.index)
    ax3.set_xticklabels(df_usa_case.index, rotation='vertical', size=6)
    plt.show()
    st.pyplot()














































