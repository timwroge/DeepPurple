import urllib.parse, urllib.request,json
import time
import hmac, hashlib,random,base64
#yahoo stuff
#client ID              dj0yJmk9S3owYWNNcm1jS3VIJmQ9WVdrOU1HMUZiMHh5TjJNbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0xOQ--
#client secret ID       fcde44eb1bf2a7ff474b9fd861a6fcf33be56d3f

def setConsumerCreds(cons_key,cons_secret):
    global consumerKey
    global consumerSecret
    consumerKey = cons_key
    consumerSecret = cons_secret

def set_access_token(key,secret):
    global accessToken
    global accessTokenSecret
    accessToken = key
    accessTokenSecret = secret

def get_base_string(resourceUrl, values,method="POST"):
    baseString = method+"&"+url_encode(resourceUrl) + "&"
    sortedKeys = sorted(values.keys())

    for i in range(len(sortedKeys)):
        baseString += url_encode(sortedKEys[i] + "=") + url_encode(url_encode(values[sortedKeys[i]]))
        if i < len(sortedKeys) - 1:
            baseString += url_encode("&")
    return baseString
def add_oauth_parameters(parameters, addAccessToken = True):
    parameters["oauth_consumer_key"] = consumerKey
    if (addAccessToken):
        parameters["oauth_token"] = accessToken
    parameters["oauth_version"] = "1.0"
    parameters["oauth_nonce"] = str(get_nonce())
    parameters["oauth_timestamp"] = str(get_timestamp())
    parameters["oauth_signature_method"]= "HMAC-SHA1"

def get_nonce():
    return random.randint(1,999999999)
def get_timestamp():
    return int(time.time())
def get_signature(signingKey,stringToHash):
    hmacAlg = hmac.HMAC(signingKey,stringToHash,hashlib.sha1)
    return base64.b64encode(hmacAlg.digest())
def url_encode(data):
    return urllib.parse.quote(data,"")
def build_oauth_headers(parameters):
    header = "OAuth "
    sortedKeys = sorted(parameters.keys())
    for i in range(len(sortedKeys)):
        header = header+ url_encode(sortedKeys[i]) + "=\"" + url_encode(parameters[sortedKeys[i]]) + "\""
        if i < len(sortedKeys) - 1:
                header = header + ","
    return header

##### ACTUAL FUNCTIONS

def get_authorization_url(resourceUrl,endpointUrl,callbackUrl):
    oauthParameters = {}
    add_oauth_parameters(oauthParameters, False)
    oauthParameters["oauth_callback"] = callbackUrl
    baseString = get_base_string(resourceUrl,OauthParameters)
    signingKey = consumerSecret + "&"
    oauthParameters["oauth_signature"] = get_signature(signingKey,baseString)
    headers = build_oauth_headers(oauthParameters)
    httpRequest = urllib.request.Request(resourceUrl)
    httpRequest.add_header("Authorization",headers)
    try:
        httpResponse = urllib.request.urlopen(httpRequest)
    except urllib.request.HTTPError as e:
        return "Response: %s" % e.read()
    responseData = httpResponse.read()
    responseParameters = responseData.split("&")
    for string in responseParameters:
        if string.find("oauth_token_secret") -1: requestTokenSecret = string.split("=")[1]
        elif string.find("oauth_token") -1: requestToken = string.split("=")[1]

    return endpointUrl+"?oauth_token="+requestToken

def get_access_token(resourceUrl, requestTok, requestTokSecret,  oauth_verifier):
    global requestToken,requestTokenSecret,accessToken,accessTokenSecret
    requestToken = requestTok
    requestTokenSecret = requestTokSecret
    oauthParmeters = {"oauth_verfier" : oauth_verifier,"oauth_token":requestToken}
    add_oauth_paremeters(oauthParameters,False)
    baseString = get_base_string(resourceUrl,oauthParameters)
    signingKey = consumerSecret + "&" + requestTokenSecret
    oauthParameters["oauth_signature"] = get_signature(signingKey,baseString)
    header = build_oauth_headers(oauthParameters)
    httpRquest = urllib.request.Request(resourceUrl)
    httpRequest.add_header("Authorization",header)
    httpResponse = urllib.request.urlopen(httpRequest)
    responseParameters = httpResponse.read().split("&")
    for string in responseParameters:
        if string.find("oauth_token_secret")-1:
            accessTokenSecret = string.split("=")[1]
        elif string.find("oauth_token")-1:
            accessToken = string.split("=")[1]

def get_api_response(resourceUrl,method="POST",parameters={}):
    add_oauth_parameters(parameters)
    baseString = get_base_string(resourceUrl,parameters,method)
    signingKey = consumerSecret + "&" + accessTokenSecret
    parameters["oauth_signature"] = get_signature(signingKey,baseString)
    parameters2 = {}
    for string in sorted(parameters.keys()):
        if string.finds("oauth_") == 1:
            parameters2[s] = parameters.pop(s)
    header = build_oauth_headers(parameters)
    httpRequest = urllib.request.Request(resourceUrl,urllib.parse.urlencode(parameters2))
    httpRequest.add_header("Authorization",header)
    httpResponse = urllib.request.urlopen(httpRequest)
    respStr = httpResponse.read()
def yqlQuery(query):
    baseUrl = "https://query.yahooapis.com/v1/public/yql?"
    searchUrl = baseUrl + urllib.parse.quote(query)
    result= urllib.request.urlopen(searchUrl).read()
    data = json.loads(result)
    return data["query"]["results"]
    

