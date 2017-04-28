# This program basically works by calling
# the function websiteRate()
# like this --> websiteRate("http://www.example.com")
# or this --> websiteRate(["http://www.example.com","http://www.otherexample.com",...])
# It returns the number of positive words minus the number of negatives words
# and the number of keywords like this [30,3]
# a positive first number (like 30) means its a good website, because more good words were found
# a negative first number indicates the opposite
# 0 means it might be good or bad, depending
# and a high number of keywords found is helpful for finding whether
# the website you're scanning is actually relevant or not. 
# This program is useful if you want to quickly scan a few articles you've found and
# see whether they are good for your company or not.
# In the future it could be used with a search api so that we can automatically
# check whether a company is doing well or poorly.

import urllib.request, html.parser,re,http.cookiejar

badWords = ["bad","stolen","fraud","criminal","upset","cheat","fake","theft","attack",
            "break-in","worse","unfortunate(?:ly)?","regress","unhealthy","sad","accussed",
            "terrible","loss(?:es)?","lose","fail(?:ing)?","down","detiorating","fear(?:ing)?",
            "scary","unlucky","unfavorable","unstable","disabling","crippling",
            "cripples?","unstatisfactory","unpopular","losing","dwindling","dissolve",
            "dissolving","bankrupt","uncertain(?:ty)","downward","falling","lower","lowering",
            "sick","less","lessening","loosening","struggle","struggling","limp(ing)*",
            "lost","poor","disadvantage","lagging","behind","lackluster","crumbl(ing)*",
            "falling apart","scared","intimidated","worried","worrying","threatening",
            "threats?","dark","endure","terror","terrorist","hack(?:er)?","crude","cancel","withhold","end"]

goodWords = ["good","boost(?:ed)?","improves?","healthy?","gain(?:ing|ed)?","win(?:ning)?","happy","fortunate(?:ly)?","lucky",
             "succeed","success","improving","favorable","secure","stable","approve",
             "exciting","beneficial","thriving","thrive","terrific","great","wonderful","super",
             "productive","popular(?:ity)?","incredible","novel","stunning","safe",
             "quality","high","raise","rise+n*","promising","excellent","extraordinary",
             "cutting edge","innovative","positive","advantage","forward","ahead",
             "progress","of tomorrow","bright"]

imWords = ["shock(?:ing)*","big","important","chang[e|(?:ing)]","sell","buy","false","crazy","money","opportunity","profit"]

for i in range(len(badWords)): badWords[i] = "[ \"\'\.]"+ badWords[i] + "[ \.\?,\"\']"       #\ 
for i in range(len(goodWords)): goodWords[i] = "[ \"\'\.]"+ goodWords[i] + "[ \.\?,\"\']"    #| adjust words for regular expressions
for i in range(len(imWords)): imWords[i] = "[ \"\'\.]"+ imWords[i] + "[ \.\?,\"\']"

#######################
#                     # 
#    MAIN FUNCTION    #
#                     #
#       Modes:        # 
# 0 - Good/Bad        # 
# 1 - Company Search  #
# 2 - Important Info  #
#                     #
#                     # 
#######################




def websiteRate(urls,mode=0,extrainfo = ""):
    if type(urls) != type(["list"]): urls = [ urls ] # in case you just want to look at one website
    
    class customParser(html.parser.HTMLParser): #parser for html
        def handle_data(self, data):
            pageData.append(data) # just get data, tags not needed
    returnList = []
    for url in urls: # for each url
        print(url)
        try:
            pageData = []       #\
            foundBWords = []    #|   
            foundGWords = []    #|
            foundIWords = []    #|       #| Reset everything
            numbers = []        #/

            
            cj = http.cookiejar.CookieJar() #Holder for cookies, needed for websites like nytimes
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
            request = urllib.request.Request(url) # get the webpage
            webpage = opener.open(request)
            webpage = str(webpage.read()) # read it into a string
            newParser = customParser() # create parser
            newParser.feed(webpage) # parse it
            rawData = " ".join(pageData) # turning results into a string

            if mode == 0:
                for word in badWords: foundBWords += re.findall(word,rawData)
                for word in goodWords: foundGWords += re.findall(word,rawData)
                numbers = re.findall("[A-Z]?[a-z]+ \$?[0-9]+,?(?:[0-9]|,)*[0-9]*%? [a-z]+",rawData) # find numbers of interest
                returnList += [foundBWords,foundGWords,numbers]
                returnList.append(numbers)
                if len(foundBWords) > len(foundGWords): print("BAD")
                else: print("GOOD")
            elif mode == 1:
                companies = extrainfo.split(",")
                found = []
                for company in companies: found += re.findall("[\.\, ]"+company+"[\.\,\ ]",rawData)
                returnList = len(found)
                
            elif mode == 2:
                for word in imWords: foundIWords += re.findall(word,rawData)
                numbers = re.findall("[A-Z]?[a-z]+ \$?[0-9]+,?(?:[0-9]|,)*[0-9]*%? [a-z]+",rawData) # find numbers of interest
                returnList = foundIWords + numbers

            else: print("Mode",mode,"not defined.")
                        
        except urllib.request.HTTPError as error:
            print("\n\n\nThere was an HTTP error:", error.code,error.reason, "with the url",url)
    return returnList


#input neutral words
# create library
        #words in title
    

