from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import main
import pandas as pd

stocks = ['AFMA', 'AFRIC INDUSTRIES', 'AFRIQUIA', 'AGMA', 'ALLIANCES', 'ALUMINIUM DU MAROC',
          'ARADEI', 'ATLANTASANAD', 'ATTIJARI', 'AUTO HALL', 'AUTO NEJMA', 'BALIMA',
          'BANK OF AFRICA', 'BCP', 'BMCI', 'CARTIER SAADA', 'CDM', 'CENTRALE DANONE', 'CIH', 'CIMENTS DU MAROC',
          'COLORADO', 'COSUMAR', 'CTM', 'DARI COUSPATE', 'DELATTRE LEVIVIER', 'DELTA HOLDING', 'DIAC SALAF',
          'DISWAY', 'ADDOHA', 'ENNAKL', 'EQDOM', 'FENIE BROSSETTE', 'HPS', 'IB MAROC.COM',
          'IMMORENTE', 'INVOLYS', 'ITISSALAT AL-MAGHRIB', 'JET CONTRACTORS', 'LABEL VIE',
          'LAFARGEHOLCIM', 'LESIEUR', 'LYDEC', 'M2M Group', 'MAGHREB OXYGENE', 'MAGHREBAIL',
          'MANAGEM', 'MAROC LEASING', 'MED PAPER', 'MICRODATA', 'MINIERE TOUISSIT', 'MUTANDIS SCA',
          'NEXANS MAROC', 'OULMES', 'PROMOPHARM', 'REALISATIONS MECANIQUES', 'REBAB COMPANY',
          'DAR SAADA', 'RISMA', 'S.M MONETIQUE', 'SAHAM', 'SALAFIN', 'SAMIR', 'SMI', 'SNEP',
          'BOISSONS DU MAROC', 'SODEP-Marsa Maroc', 'SONASID', 'SOTHEMA', 'STOKVIS',
          'STROC', 'TAQA MOROCCO', 'TIMAR', 'TOTAL MAROC', 'UNIMER', 'WAFA', 'ZELLIDJA']
frames = [main.df1,main.df2,main.df3,main.df4,main.df5,main.df6,main.df7]

Media = pd.concat(frames)

for stock in stocks:
    i = 0
    tf=0
    idf=0
    while (i < 174):
        if stock.lower() in Media[3][i].lower():
            tf = Media[3][i].lower().count(stock.lower()) / (Media[3][i].count(' ')+1)
            j = 0
            for k in (0, 173):
                if stock.lower() in Media[3][k].lower():
                    j = j+1
            idf = math.log2(174/ (j+1))
            dates.append(Media[4][i])
            foundStocks.append(stock)
            tfidf.append(tf * idf)
        dates.append(Media[4][i])
        foundStocks.append(stock)
        tfidf.append(tf*idf)
        i = i + 1
tfidf_df = pd.DataFrame(list(zip(dates,foundStocks,tfidf)))
