import pandas as pd

bromma_stadsdelar = [
    'Södra Ängby', 'Nockeby', 'Alvik', 'Bromma', 'Traneberg', 'Åkeslund',
    'Ålsten', 'Smedslätten', 'Beckomberga', 'Ulvsunda', 'Abrahamsberg',
    'Norra Ängby', 'Blackeberg', 'Höglandet', 'Riksby', 'Mariehäll',
    'Bromma kyrka', 'Eneby', 'Åkeshov', 'Olovslund', 'Nockebyhov',
    'Stora mossen', 'Äppelviken', 'Bällsta', 'Ulvsunda industriområde',
    'Bromma stadsdelsområde', 'Råcksta'
]

hagerstensalvsjo_stadsdelar = [
    'Hägersten', 'Älvsjö', 'Västberga', 'Midsommarkransen', 'Aspudden',
    'Fruängen', 'Långbro', 'Liseberg', 'Älvsjö industriområde',
    'Hägerstensåsen', 'Västertorp', 'Solberga', 'Mälarhöjden', 'Örby slott', 'Gröndal', 'Liljeholmen', 'Långsjö'
]


def map_omrade(stadsdel):
    if stadsdel in bromma_stadsdelar:
        return 'Bromma'
    elif stadsdel in hagerstensalvsjo_stadsdelar:
        return 'Hägersten-Älvsjö'
    else:
        return 'N/A'


df = pd.read_csv('data_files/parker.csv')
df['Stadsdel'] = df['Stadsdelsområde'].apply(map_omrade)
df.to_csv('data_files/parker.csv',
          index=False, encoding='utf-8-sig')
print("Klart!")
