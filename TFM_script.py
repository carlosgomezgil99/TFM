import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,MinMaxScaler

df=pd.read_excel('data/CMBD_6_20181217-135856.xlsx')
df_calidad_aire_08=pd.read_csv('data/datos08.csv',sep=';')
df_calidad_aire_09=pd.read_csv('data/datos09.csv',sep=';')
df_calidad_aire_10=pd.read_csv('data/datos10.csv',sep=';')
df_calidad_aire_11=pd.read_csv('data/datos11.csv',sep=';')
df_calidad_aire_12=pd.read_csv('data/datos12.csv',sep=';')
df_calidad_aire_13=pd.read_csv('data/datos13.csv',sep=';')
df_calidad_aire_14=pd.read_csv('data/datos14.csv',sep=';')
df_calidad_aire_15=pd.read_csv('data/datos15.csv',sep=';')

df.head()

df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')

df.describe(include='all').T

comunidad_autonoma=13
provincia=28

df.drop(['comunidad_autónoma','provincia'],axis=1,inplace=True)

df.dtypes
df_calidad_aire_08.dtypes

df.shape
df_calidad_aire_08.shape

df.isnull().mean().sort_values(ascending=False)*100

df.duplicated().sum()

df.select_dtypes('object').apply(pd.Series.nunique, axis = 0).sort_values()

def vuelta_fecha(x):
    x=str(x)
    if len(x)==8:
        año=x[4:]
        mes=x[2:4]
        dia=x[:2]
        fecha=año+'-'+mes+'-'+dia
    else:
        año=x[3:]
        mes=x[1:3]
        dia=x[:1]
        fecha=año+'-'+mes+'-'+'0'+dia
    return fecha


df[['fecha_de_alta','fecha_de_nacimiento','fecha_de_ingreso']]=df[['fecha_de_alta','fecha_de_nacimiento','fecha_de_ingreso']].applymap(lambda x:vuelta_fecha(x))

df.fecha_de_alta=pd.to_datetime(df.fecha_de_alta,format='%Y-%m-%d')
df.fecha_de_nacimiento=pd.to_datetime(df.fecha_de_nacimiento,format='%Y-%m-%d')
df.fecha_de_ingreso=pd.to_datetime(df.fecha_de_ingreso,format='%Y-%m-%d')

df.servicio=LabelEncoder().fit_transform(df.servicio)

df.corr().style.background_gradient('RdYlGn')

df.select_dtypes('number').describe()

df.plot(x='edad',y='estancia',kind='scatter',figsize=(20,10))

df.corr()['edad'].sort_values(ascending=False)