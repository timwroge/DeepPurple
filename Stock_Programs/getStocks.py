# This program basically just gets stocks or currencies
# if you change the companies variable, the autoStockCheck
# function will check those companies for you
# You don't really need to use getStocks, since the autoStockCheck
# can be called like so --> autoStockCheck(1,1) and the program
# will check the stocks once
# The variables entered are:
# numTimes - the number of times to check the stock
# interval - the time (in seconds) between checks
# companies - a dictionary {} that has the names of the companies and their codes
# (see the companies variable to get the idea)
# You don't have to always call it as
# autoStockCheck(variable,variable,variable), because
# interval defaults to 1 second and companies defaults to the companies variable
# this means you can just call autoStockCheck(30) and it will check 30 times
# with an interval of 1 second, and using the default companies specified at the top
# of this program

# So, autoStockCheck will get the stocks automatically,
# and getCurrencies will show you a list of the current currency
# conversion factors, though its a bit complex to look at right now
# I will update that later if we need it, it was just a small thing
# to do so I thought I might as well add it

# VALUES FOR RETURNED STOCK QUOTE DATA (INCOMPLETE)
# l_cur     current price, this is what we really care about
# ccol      ?
# pcls_fix  previous close
# id        id
# e         Exchange (NASDAQ etc)
# s         ?
# c_fix     ?
# cp_fix    ?
# t         ?
# lt        ? Time queried
# ltt       ?

import urllib.parse,urllib.request,json,ast,time
global companies
companies = {"Nvidia":"NVDA","Intel":"INTC","Apple":"AAPL"}

def autoStockCheck(numTimes,interval=1,comps=companies):
    for i in range(numTimes):
        print("Checking...")
        x = getStocks(comps)
        time.sleep(interval)
        print()
    return x

def getCurrencies():
    webData = urllib.request.urlopen("http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
    webData = webData.read().decode('utf-8')
    print(webData)
    data = ast.literal_eval(webData)
    return data

def getStocks(companies={"Nvidia":"NVDA","Google":"GOOG"}):
    searchUrl= "http://finance.google.com/finance/info?client=ig&q=NASDAQ%3A"
    c = 0
    for key in companies:
        searchUrl += urllib.parse.quote(companies[key],"")
        if c < len(companies.keys()) -1 :
            searchUrl+= ","
        c+=1
    print(searchUrl)
    httpRequest = urllib.request.urlopen(searchUrl)
    data = str(str(httpRequest.read()))[7::] # turn into a string from bytes
    data = data.replace("\\n","").replace("\'","") # clean it up
    data = ast.literal_eval(data) # turn it into a list
    data = dict(zip([comp for comp in list(companies.keys())],data)) # turn it into a dictionary
    for key in data:
        print(key,data[key]["l_cur"])
    return data


        
