# Project Work Group 4
## Indice 

- [Introduction](#Introduction)
- [Technologies](#technologies)
- [Response examples](#Response-examples)

### Introduction
#### The aim of our project is to allow at the user to know the minimun, maximun, average and trend value of a specific company by passing the company name or the symbol of the company as a parameter.

### Technologies
#### To realise this project we use only Python 3.9 to write the code.The information we used to perform the tasks was taken from the following API:
https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=FCAU&apikey=F3FV4ARAKOYQT44K. 
#### The lambda function has been developed in AWS and we also try our code in local to find some errors that AWS not given us.
#### The Alexa Skill has been developed in Alexa Developer Console where we created our skill and then we write the function to solve the task that we call "stock market". To show the result from Alexa the only two parameters are the name or the symbol of the company and the type of the period which can be weekly o daily. The frase to invoke the stock market intent is: `Dimmi lo stato in borsa dell'azienda  {name} nel periodo di tipo {periodType}`.
  
### Response examples
#### The lambda function return the follow json: 


