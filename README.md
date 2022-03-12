# Project Work Group 4
## Indice 

- [Introduction](#Introduction)
- [Technologies](#technologies)
- [Response examples](#Response-examples)

### Introduction
#### The aim of our project is to allow at the user to know the minimun, maximun, average and trend value of a specific company by passing the company name or the symbol of the company as a parameter.

### Technologies
#### The project runs on Python 3.9. The information we used to perform the tasks is provided by the following API:
https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=FCAU&apikey=F3FV4ARAKOYQT44K. 
#### The lambda function was based on AWS technologies and we also tried in the first place to run the our code in local, that helped the discover of bugs and optimisations possibilities. We also had more informations that aws didn't give us.
#### The Alexa Skill has been developed using Alexa Developer Console where we created our skill,  that we called "stock market". To show the result from Alexa the only two parameters are the name or the symbol of the company and the type of the period which can be weekly o daily. The frase to invoke the stock market intent is: `Dimmi lo stato in borsa dell'azienda  {name} nel periodo di tipo {periodType}`.
  
### Response examples
#### The lambda function return the follow json:
```
{
    "type": "Weekly",
    "name": "Facebook Inc",
    "symbol": "FBOK34.SAO",
    "period": "2022-01-13 - 2022-01-24",
    "avg": 62.6407,
    "min": 57.01,
    "max": 65.99,
    "trend": "6.08 degrees"
}
```


