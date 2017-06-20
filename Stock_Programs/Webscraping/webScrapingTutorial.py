#importing libraries for websraping data

#beautiful soup
import bs4 as bs
#this serializes any python object
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import time
#api key, quandl: ZHafX6HMyxi4K9mcdAEM

#example code to get the data for the sp500 list tickers
def save_sp500_tickers():
    resp=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    #creating a bs object
    #resp.txt is the source code txt
    #standard html parser 
    soup=bs.BeautifulSoup(resp.text, 'html.parser')
    #finds the specific table tag in the script
        #specifies a specific class to narrow search
    table =soup.find('table', {'class': 'wikitable sortable'})
    tickers =[]
    #[1:] specifies that we are not searching for the first table header row
    #tr is for table-row
    for row in table.findAll('tr')[1:]:
        #zeroth column
        ticker =row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        #this opens a file and dumps the data in the file
        pickle.dump(tickers, f)
    #tests if the tickers got sent out correctly
    print(tickers)
    return tickers
save_sp500_tickers()

def get_data_from_google(reload_sp500=False):
    
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    #this loads in the data frame if it does not already exist
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    start=dt.datetime(2005, 1, 1)
    end =dt.datetime(2017, 6, 16)
    total=0
    
    for ticker in tickers:
        #prints where the data file is in copying it to the data format
        total+=1
        
        print('Printing Google Finance results for ' ,ticker)
##        if ticker=='LMT' or ticker=='NWL':
##            print('Shit dont work')

        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
##            if total%5 ==0:
                #print('Pausing...')
                #time.sleep(5)
            if ticker =='LMT' or ticker=='NWL':
                print(ticker, ' is not reading data')
##                df=web.DataReader(ticker, 'yahoo', start, end)
##                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            else:
                df=web.DataReader(ticker, 'google', start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))
            
get_data_from_google()

def compiledata():
    with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    #begin dataframe
    main_df=pd.DataFrame()
    #begin iterating through the tickers
    tickers_that_dont_work ={'ALGN','RE','HLT','LMT' ,'NWL' ,'NBL','NSC', 'NOC'}
    for count, ticker in enumerate(tickers):
##        if ticker in tickers_that_dont_work:
##            print('Shit dont work')
##        else:
        #count allows for us to know where we are in the list
        df=pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        #renames adj close to the ticker symbol
        df.rename(columns ={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'] ,1,inplace=True)

        if main_df.empty:
            main_df =df
        else:
            main_df =main_df.join(df, how='outer')
        if count % 10  == 0:
            print(count)
    print (main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')
            
compiledata()





    
        
