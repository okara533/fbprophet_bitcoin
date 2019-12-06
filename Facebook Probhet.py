#!/usr/bin/env python
# coding: utf-8

# # Fbprophet ile Bitcoin Fiyat Öngörüsü

# Öncelikle gerekli kütüphaneleri indirerek başlıyoruz. Veriler için YahooFinancials modelleme için fbprophet indirmemiz gerekiyor. Bu kütüphaneleri indirmeden önce kütüphaneleri yüklediğinizden emin olun. pip install koduyla kütüphanleri yükleyebilirsiniz    

# In[1]:


from yahoofinancials import YahooFinancials
import pandas as pd
import numpy as np
from fbprophet import Prophet


# YahooFinancials'dan verilen tarih aralığı ile verileri indirebilirsiniz. Burada birden çok kripto para birmini kullanabilirsiniz. Yahoodan sembolleri ekleyerek diğer kripto paralar ile ilgili de analizi yapabilirsiniz.

# In[ ]:


bas_tarih=input("Başlangıç tarihi giriniz,Örn:2019-06-29....  ")
bit_tarih=input("Bitiş tarihi giriniz,Örn:2019-08-29....  ")
cryptocurrencies = ['BTC-USD', 'ETH-USD',"XRP-USD","LTC-USD","XLM-USD","LINK-USD"]
yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
daily_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data(bas_tarih, bit_tarih, 'daily')
df=pd.DataFrame(daily_crypto_prices)
BTCUSD=pd.DataFrame(df["BTC-USD"]["prices"])

ETHUSD=pd.DataFrame(df['ETH-USD']["prices"])
XRPUSD=pd.DataFrame(df['XRP-USD']["prices"])
LTCUSD=pd.DataFrame(df['LTC-USD']["prices"])
XLMUSD=pd.DataFrame(df['XLM-USD']["prices"])
LINKUSD=pd.DataFrame(df['LINK-USD']["prices"])

currency=input("BTC,ETH,XRP,LTC,XLM...:")
if currency=="BTC":
    data_prophet = BTCUSD.copy()
elif currency=="ETH":
    data_prophet = ETHUSD.copy()
elif currency=="XRP":
    data_prophet = XRPUSD.copy()
elif currency=="LTC":
    data_prophet = LTCUSD.copy()
elif currency=="XLM":
    data_prophet = XLMUSD.copy()
elif currency=="LINK":
    data_prophet = LINKUSD.copy()


# Öngörü gün sayısı arttıkça güven aralığı da artacaktır.

# In[2]:




a=input("Kaç Günlük Öngörü:..........")
del data_prophet["date"]
del data_prophet["high"]
del data_prophet["low"]
del data_prophet["open"]
del data_prophet["volume"]
del data_prophet["close"]
data_prophet.columns =['y','ds']
data_prophet=data_prophet.reindex(["ds","y"],axis="columns")
data_prophet.reset_index(drop=False, inplace=True)
pd.to_numeric(data_prophet["y"])
data_prophet.ds=pd.to_datetime(data_prophet.ds, yearfirst=True)
#data_prophet.ds.astype("int")
m = Prophet()
m.fit(data_prophet)
future = m.make_future_dataframe(periods=int(a),freq="d")
forecast = m.predict(future)
pd.plotting.register_matplotlib_converters()
m.plot(forecast)
m.plot_components(forecast)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




