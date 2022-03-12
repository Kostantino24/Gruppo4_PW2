import json
import sys
import stock_market
import numpy as np

def get_data(function, apikey,year,month,day,symbol = "", name = ""):
    """FUNZIONE PRINCIPALE PER L'OTTENIMENTO E CALCOLO DEI DATI"""
    # url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=FCAU&apikey=EPH9JSNA7C3KJYZU"
    # url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={apikey}"
    if function == "month":
        function = "TIME_SERIES_WEEKLY"
    elif function == "week":
        function = "TIME_SERIES_DAILY"
        
    """return {
            "funzione":function,
            "api":apikey,
            "year":year,
            "month":month,
            "day":day,
            "symbol":symbol,
            "name":name
        }"""


    if symbol == "":
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={name}&apikey={apikey}"
        loaded = stock_market.get_data(url)  # Ottenimento delle coordinate basate sul nome della città
        if len(loaded['bestMatches']) == 0:
            return {
                "error": "Company not found"
            }
        symbol = loaded['bestMatches'][0]['1. symbol']
        name = loaded['bestMatches'][0]["2. name"]
    else:
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={apikey}"
        loaded = stock_market.get_data(url)
        if len(loaded['bestMatches']) == 0:
            return {
                "error": "Company not found"
            }
        name = loaded['bestMatches'][0]["2. name"]
    
    
    print (symbol)
    print (name)
    print (function)
    print (apikey)
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={apikey}"
    
    loaded = stock_market.get_data(url)  # Ottenimento delle coordinate basate sul nome della città
    
    print (loaded)
    
    # Tentativo di connessione al sito, se fallice per 3 volte il programma termina
    for _ in range(0, 3):
        loaded = stock_market.get_data(url)  # Connessione al sito del meteo
        if not isinstance(loaded, int):
            break
        print(f"Il il sito non è raggiungibile. Status code {loaded}")

    if isinstance(loaded, int):
        print(f"Il il sito non è raggiungibile. Status code {loaded}")
        return f"Error :{loaded}"

    if function == "TIME_SERIES_DAILY":
        type = "Weekly"
    elif function == "TIME_SERIES_WEEKLY":
        type = "Montly"

    keys = stock_market.getList(loaded)
    
    
    if keys[0] == "Note":
        return {
            "type": type,
            "name": name,
            "error": loaded[keys[0]]
        }

    date = ""
    for i in loaded[keys[1]]:
        if int(i[:4]) <= int(year):
            if int(i[5:7]) <= int(month):
                if int(i[8:10]) <= int(day):
                    date = i
                    break

    if date == "":
        return {
            "type": type,
            "name": name,
            "error": "day not found"
        }

    data = stock_market.trim(loaded[keys[1]],date,type)

    chiavex = stock_market.getList(loaded[keys[1]])[stock_market.getList(loaded[keys[1]]).index(stock_market.getList(data)[-1]) + 1]
    keys = stock_market.getList(data)
    
    g = []
    for x in keys:
        g.append(stock_market.media({x:data[x]}))
    #

    a, b = stock_market.linreg(range(len(g)), g)
    extrapolatedtrendline = [a * index + b for index in range(len(g))]

    vector_1 = [0, extrapolatedtrendline[0]]
    vector_2 = [len(g), extrapolatedtrendline[-1]]

    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)

    print(json.dumps({
           "type": type,
           "name": name,
           "symbol": symbol,
           "period": chiavex + " - "+keys[0],
            "avg": stock_market.media(data),
            "min": stock_market.minimo(data),
            "max": stock_market.massimo(data),
            "trend":f"{round(np.degrees(angle),2)} degrees",
            #"data": data
    } ))
    return {
           "type": type,
           "name": name,
           "symbol": symbol,
           "period": chiavex + " - "+keys[0],
            "avg": stock_market.media(data),
            "min": stock_market.minimo(data),
            "max": stock_market.massimo(data),
            "trend":f"{round(np.degrees(angle),2)} degrees",
            #"data": data
    } 

        
def lambda_handler(event, context):
    #y = json.loads(event['body'])
    y = event["body"].replace("=",":").replace("&",",")
   
    y = "{"+y[0:len(y)]+"}"
    y = y.replace(":",'":"').replace(",",'","').replace("{",'{"').replace("}",'"}')
   
    
    
    y = json.loads(y)
    print(y)
    return {
        'statusCode': 200,#json.dumps(body)
        'body': json.dumps(get_data(y["function"],y["apikey"],y["year"],y["month"],y["day"],y["symbol"],y["name"]))
    }
