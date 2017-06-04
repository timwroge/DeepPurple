#this will preform sum basic statistical analysis of data as specified as user input
#this should give a starting date

import datetime as dt
import numpy
#this allows us to make plots

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
#makes the graphs look better:
from datetime import timedelta

from matplotlib import style

#good data analysis library

import pandas as pd

#inports more libraries
#this makes it easy to grab data from the yahoo finance api
#will return a "pandas data frame"

import pandas_datareader.data as web
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    
    

company = 'GOOG'
current_t=dt.date.today()


##current_time_array=[endY,endM,endD]
##time_in_year=timedelta(weeks=40, days=85)
def makeDatePretty(dateArray):
    year=str(dateArray[0])
    month=str(dateArray[1])
    day=str(dateArray[2])
    slash='/'
    string=month+slash+day+slash+year
    return string

def findStockTrends(comp=company, years=10, months=0, days=0):
    current_time=dt.date.today()
    endY=current_time.year
    endM=current_time.month
    endD=current_time.day
    current_time_array=[endY,endM,endD]
    x=makeDatePretty(current_time_array)
    startDate=[endY-years,endM-months,endD-days]
    if startDate[1]<0:
        while (startDate[1]<0):
            startDate[0]-=1
            startDate[1]+=12
            
    if startDate[2]<0:
        while (startDate[2]<0):
            startDate[1]-=1
            startDate[2]+=30
    
    
    style.use('ggplot')
    #start the data on jan 1st 2000
    start=dt.datetime(startDate[0], startDate[1], startDate[2])
    end=dt.datetime(current_time_array[0],current_time_array[1],current_time_array[2])
    print(comp)

    #dataframe
    df=web.DataReader(comp, 'google', start, end)
    #converting the data to a csv
    #df.to_csv('google.csv')
    '''
        user_response=input('Do you want to create a file for the data? (Y/N)')
        if user_response.lower() =='y':
            #reading in a csv
            name_of_file=company + '.csv'
            df=pd.read_csv(name_of_file, parse_dates=True, index_col=0)
        print(df.head(10))
    '''
    print(df.head(10))

    ##df['Low'].plot()
    ##plt.show()
    ##df['High'].plot()
    ##plt.show()

    #adding a rolling average
    df['100 M.Avg']=df['Close'].rolling(window=100, min_periods=0).mean()
    df.dropna(inplace=True)
    #print(df.head())
    plt.figure(1)

    
    #using matplotlib to plot
    ax1= plt.subplot2grid((12,1), (0,0), rowspan=5, colspan=1)


    
    x=makeDatePretty(current_time_array)
    y=makeDatePretty(startDate)
    title_of_graph=' Stock Price of ' +comp+' from ' +y+' to ' +x
    plt.title(title_of_graph)

    
    ax2= plt.subplot2grid((12,1), (5,0), rowspan=5, colspan=1, sharex=ax1)
    ax1.plot(df.index, df['100 M.Avg'])
    ax1.plot(df.index, df['Close'])
    ax2.bar(df.index, df['Volume'])
    
    

    #finds the mean of data over 10 days
    df_ohlc=df['Close'].resample('10D').ohlc()
    df_volume =df['Volume'].resample('10D').sum()

    df_ohlc.reset_index(inplace=True)
    df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)


    #print(df_ohlc.head())
    
    ax3= plt.subplot2grid((12,1), (6,0), rowspan=5, colspan=1, sharex=ax1)
    ax4= plt.subplot2grid((12,1), (11,0), rowspan=5, colspan=1, sharex=ax1)
    ax3.xaxis_date()
    candlestick_ohlc(ax3, df_ohlc.values, width=2, colorup='g')
    ax4.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
    
    plt.show()


















