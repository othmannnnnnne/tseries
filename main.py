from Scrapers import LeMatin, Bladi, LaVieEco, LeSiteInfo, BourseNews, Medias24, h24info, LaQuotidienne, libelles, BO
import pandas as pd
from enum import Enum
from Weather import weather
from Trends import StockTrends
import itertools
from pymongo import MongoClient

class Mois(Enum):
    janvier = 1
    février = 2
    mars = 3
    avril = 4
    mai = 5
    juin = 6
    juillet = 7
    août = 8
    septembre = 9
    octobre = 10
    novembre = 11
    décembre = 12
dates1=[]
body1=[]
def ArrangeLeMatin(i,n):
    LeMatin.scroll(i,n)
    k=0
    for u in LeMatin.dates:
        for i in range(1, 13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name, str(Mois(i).value))
                LeMatin.dates[k]=date
                k=k+1
    for i in range(0, len(LeMatin.dates)):
        if (len(LeMatin.dates[i]) == 17):
            dates1.append(LeMatin.dates[i][:3] + '0' + LeMatin.dates[i][3:])
        else:
            dates1.append(LeMatin.dates[i])

    for j in range(0,i):
        body1.append("".join(LeMatin.eval('test'+str(j))))

#ArrangeLeMatin(1,50)
#ArrangeLeMatin(2,50)
#ArrangeLeMatin(3,50)

df1 = pd.DataFrame(list(zip(LeMatin.titles, LeMatin.urls, LeMatin.authors, body1, dates1)))

dates2=[]
body2=[]
def ArrangeBladi(i,n):
    Bladi.scroll(i,n)
    k=0
    for u in Bladi.dates:
        for i in range(1,13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name,str(Mois(i).value))
                Bladi.dates[k]=date
                k=k+1
    for i in range(0,len(Bladi.dates)):
        if(len(Bladi.dates[i]==9)):
            dates2.append(Bladi.dates[:3]+'0'+Bladi.dates[3:])
        else:
            dates2.append(Bladi.dates[i])

    for j in range(0,i):
        body2.append("".join(Bladi.eval('test' + str(j))))


#ArrangeBladi(1,50)
#ArrangeBladi(2,50)

df2 = pd.DataFrame(list(zip(Bladi.titles, Bladi.urls, body2, dates2)))

dates3=[]
body3=[]
def ArrangelaVieEco(n):
    LaVieEco.scroll(n)

    for j in range(0,len(LaVieEco.titles)):
        body3.append("".join(LaVieEco.eval('test'+str(j))))

    df3 = pd.DataFrame(list(zip(Bladi.titles, Bladi.urls, Bladi.summaries, Bladi.dates, body3)))

#ArrangelaVieEco(50)

dates4=[]
body4=[]
def ArrangeLeSiteInfo(i,n):
    LeSiteInfo.scroll(i,n)
    k=0
    for u in LeSiteInfo.dates:
        for i in range(1,13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name,str(Mois(i).value))
                LeSiteInfo.dates[k]=date
                k=k+1
    for i in range(0,len(Bladi.dates)):
        if(len(LeSiteInfo.dates[i]==9)):
            dates4.append(LeSiteInfo.dates[:3]+'0'+Bladi.dates[3:])
        else:
            dates4.append(LeSiteInfo.dates[i])

    for j in range(0,i):
        body4.append("".join(LeSiteInfo.eval('text'+str(j))))

#ArrangeLeSiteInfo(1,50)
#ArrangeLeSiteInfo(2,50)

df4=pd.DataFrame(list(zip(LeSiteInfo.titles, LeSiteInfo.urls, dates4 , body4)))

dates5=[]
body5=[]
def ArrangeLaQuotidienne(i,n):
    LaQuotidienne.scroll(i,n)
    k=0
    for u in LaQuotidienne.dates:
        for i in range(1,13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name,str(Mois(i).value))
                Bladi.dates[k]=date
                k=k+1
    for i in range(0,len(Bladi.dates)):
        if(len(LaQuotidienne.dates[i]==9)):
            dates5.append(LaQuotidienne.dates[:3]+'0'+Bladi.dates[3:])
        else:
            dates5.append(LaQuotidienne.dates[i])
    for j in range(0,i):
        body5.append("".join(LaQuotidienne.eval('text'+str(j))))
#ArrangeLaQuotidienne(1,50)
#ArrangeLaQuotidienne(2,50)

df5 = pd.DataFrame(list(zip(LaQuotidienne.titles, LaQuotidienne.urls, dates5, body5)))

dates6=[]
body6=[]
def ArrangeBourseNews(i,n):
    BourseNews.scroll(i,n)
    k = 0
    for u in BourseNews.dates:
        for i in range(1, 13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name, str(Mois(i).value))
                BourseNews.dates[k] = date
                k = k + 1
    for i in range(0, len(Bladi.dates)):
        if (len(BourseNews.dates[i] == 9)):
            dates6.append(BourseNews.dates[:3] + '0' + Bladi.dates[3:])
        else:
            dates6.append(BourseNews.dates[i])
    for j in range(0, i):
        body6.append("".join(LaQuotidienne.eval('text'+str(j))))

#ArrangeBourseNews(1,50)
#ArrangeBourseNews(2,50)
#ArrangeBourseNews(3,50)
#ArrangeBourseNews(4,50)

df6=pd.DataFrame(list(zip(BourseNews.titles,BourseNews.urls, dates6, body6)))

dates7=[]
body7=[]
def Arrangemedias24(i,n):
    Medias24.scroll(i,n)
    k = 0
    for u in Medias24.dates:
        for i in range(1, 13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name, str(Mois(i).value))
                Medias24.dates[k] = date
                k = k + 1
    for i in range(0, len(Bladi.dates)):
        if (len(Medias24.dates[i] == 9)):
            dates7.append(Medias24.dates[:3] + '0' + Bladi.dates[3:])
        else:
            dates7.append(Medias24.dates[i])
    for j in range(0, i):

        body7.append("".join(Medias24.eval('text'+str(j))))

#Arrangemedias24(1,50)
#Arrangemedias24(2,50)

df7 = pd.DataFrame(list(zip(Medias24.titles, Medias24.urls, dates7, body7)))


dates8=[]
body8=[]
def Arrangeh24info(n):
    h24info.scroll(n)
    for j in range(0, len(h24info.titles)):
        body8.append("".join(h24info.titles,h24info.urls, dates8, body8))

#Arrangeh24info(50)

def MatrixLibelles():

    libelles.fetch()
    act = ['buy ', 'sell ', 'hold ', 'order sell ', 'order buy ']
    actions = [ "".join(items) for items in list(itertools.product(act,libelles.instruments))]

#MatrixLibelles()

def StockTrend(start,end):
    StockTrends.trends(start,end)

#StockTrend("2008-01-01","2021-04-16")

def Meteo(freq):

    weather.HistWeather(freq)


# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["poc_database"]
#News
news= db["News"]
for i in range(1,9):
    globals()['news{0}'.format(i)]=eval('df'+str(i)).to_dict()
    news.insert_one(eval('news'+str(i)))

#Trends
trends=db["Trends"]
trends_dict=StockTrends.df.to_dict()
trends.insert_one(trends_dict)

#Weather
histWeather=db["Weather"]
weather_dict=weather.hist_weather_data.to_dict()
histWeather.insert_one(weather_dict)