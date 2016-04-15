from yahoo_finance import Share
import csv
import numpy as np
import pandas as pd


yahoo=Share('GE')
YAHOO_t = yahoo.get_historical('2011-01-01', '2016-01-01')

microsoft=Share('GS')
MS_t = microsoft.get_historical('2011-01-01', '2016-01-01')

google=Share('HAL')
GOOGLE_t=google.get_historical('2011-01-01', '2016-01-01')

facebook=Share('JPM')
FACEBOOK_t = facebook.get_historical('2011-01-01', '2016-01-01')

apple=Share('K')
APPLE_t = apple.get_historical('2011-01-01', '2016-01-01')


A1= pd.DataFrame(YAHOO_t)
A1_close=A1.set_index('Date').Close

A2= pd.DataFrame(MS_t)
A2_close=A2.set_index('Date').Close

A3= pd.DataFrame(GOOGLE_t)
A3_close=A3.set_index('Date').Close

A4= pd.DataFrame(FACEBOOK_t)
A4_close=A4.set_index('Date').Close

A5= pd.DataFrame(APPLE_t)
A5_close=A5.set_index('Date').Close


Out= pd.DataFrame()
Out['Date']=A1.Date
Out['General Electric']=A1.Close
Out['GS']=A2.Close
Out['Halliburton']=A3.Close
Out['JP Morgan']=A4.Close
Out['Kellogg']=A5.Close

Out=Out.sort('Date')
Out.to_csv('data.csv')



