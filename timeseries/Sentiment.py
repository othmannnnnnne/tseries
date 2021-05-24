import main
import pandas as pd
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

stocks = ['AFMA', 'INDUSTRIES', 'AFRIQUIA', 'AGMA', 'ALLIANCES', 'ALUMINIUM',
          'ARADEI', 'SANAD', 'ATTIJARI', 'AUTO HALL', 'AUTO NEJMA', 'BALIMA',
          'BANK', 'BCP', 'BMCI', 'CARTIER SAADA', 'CDM', 'CENTRALE', 'CIH', 'CIMENTS',
          'COLORADO', 'COSUMAR', 'CTM', 'DARI COUSPATE', 'DELATTRE LEVIVIER', 'DELTA HOLDING', 'DIAC SALAF',
          'DISWAY', 'ADDOHA', 'ENNAKL', 'EQDOM', 'FENIE BROSSETTE', 'HPS', 'IB MAROC.COM',
          'IMMORENTE', 'INVOLYS', 'ITISSALAT AL-MAGHRIB', 'JET CONTRACTORS', 'LABEL VIE',
          'LAFARGEHOLCIM', 'LESIEUR', 'LYDEC', 'M2M Group', 'MAGHREB OXYGENE', 'MAGHREBAIL',
          'MANAGEM', 'LEASING', 'MED PAPER', 'MICRODATA', 'MINIERE', 'MUTANDIS',
          'MAROC', 'OULMES', 'PROMOPHARM', 'REALISATIONS MECANIQUES', 'REBAB',
          'SAADA', 'RISMA', 'MONETIQUE', 'SAHAM', 'SALAFIN', 'SAMIR', 'SMI', 'SNEP',
          'BOISSONS DU MAROC', 'SODEP-Marsa', 'SONASID', 'SOTHEMA', 'STOKVIS',
          'STROC', 'TAQA MOROCCO', 'TIMAR', 'TOTAL', 'UNIMER', 'WAFA', 'ZELLIDJA']
frames = [main.df1,main.df2,main.df3,main.df4,main.df5,main.df6,main.df7]
Media = pd.concat(frames)

sentiment=[]
foundStocks=[]
dates=[]

for article in Media:
    for stock in stocks:
        i=0
        if stock.lower() in article(3):
            blob=tb(article(3))
            senti=blob.sentiment[0]
            foundStocks.append(stock)
            sentiment.append(senti)
            dates.append(article(4))

for i in (0,len(foundStocks)):
    for j in (i+1,len(foundStocks)):
        if foundStocks[i]==foundStocks[j]:
            p=0
            if dates[i]==dates[j]:
                p=p+1
                sentiment[i]=(p*sentiment[i]+sentiment[j])/(p+1)
                sentiment.pop(j)
                dates.pop(j)
                foundStocks.pop(j)

sentiment_df = pd.DataFrame(list(zip(dates1,foundStocks,sentiment)))


