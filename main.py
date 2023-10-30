import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
# save numpy array as csv file
from numpy import asarray
from numpy import savetxt

df = pd.read_csv("Time Americans Spend Sleeping.csv")

df2 = df.groupby(['Year', 'Sex'], as_index=False)['Avg hrs per day sleeping'].mean()
df2.to_csv("Avg_hrs_Sex_Year.csv")

df3 = df.groupby(['Age Group', 'Sex', 'Year'], as_index=False)['Avg hrs per day sleeping'].agg(['mean', 'min', 'max'])
df3.to_csv("AgeGroup_Sex_Year_functii.csv")

df4 = df.groupby('Type of Days')['index'].count()
df4.to_csv("Count_TypeOfDays.csv")

df7 = df.groupby('Year')['index'].count()
df7.to_csv("Count_Year.csv")

df8 = df.groupby(['Activity', 'Type of Days', 'Sex'])['Avg hrs per day sleeping'].agg(['min', 'max', 'mean'])
df8.to_csv("TypeOfDay_Sex_functii.csv")

df5 = df.groupby(['Sex', 'Age Group']).first(5)
df5.to_csv("Sex_AgeGroup_first.csv")

df6 = df.groupby(['Type of Days', 'Sex'])['Avg hrs per day sleeping'].mean()
df6.to_csv("TypeofDays_Sex_hours.csv")

# Impart setul de date in grupe diferite dupa Sex
f_filter = df['Sex'] == 'Women'
dff = df[f_filter]
dff.to_csv("Women.csv")

# print(dff) #dff contine obervatii doar pt sex=women
dfff = dff.groupby('Year')['Avg hrs per day sleeping'].mean()
# print(dfff)


m_filter = df['Sex'] == 'Men'
# print(df[m_filter])
df[m_filter].to_csv("Men.csv")

b_filter = df['Sex'] == 'Both'
# print(df[b_filter])
df[b_filter].to_csv("Both.csv")

# asta face acelasi lucru ca cea de mai jos
f_avg = df[f_filter]['Avg hrs per day sleeping'].agg([np.min, np.max])
# print(f_avg)

f_avg = df[f_filter].agg(f_MINavgHours=('Avg hrs per day sleeping', np.min),
                         f_MAXavgHours=('Avg hrs per day sleeping', np.max))
# print(f_avg)
f_avg.to_csv("MinMax.csv")

# numPy array for Avg hours per day sleeping
avg_hours = df[['Avg hrs per day sleeping']].values
# print(avg_hours)
savetxt('Hours.csv', avg_hours, delimiter=',')

# NumPy array for Years
year = df[['Year']].values
# print(year)

# group all sex-> numpy array
sex = df['Sex'].unique()
# print(sex)
savetxt('Grupare_dupa_sex.csv', sex, delimiter=',', fmt='%s')

# group all types of days ->numpy array
day = df['Type of Days'].unique()
# print(day)
savetxt('Grupare_dupa_Zi.csv', day, delimiter=',', fmt='%s')

# matrice cu tot setul de date
variabile_observate = list(df.columns)[:]
x = df[variabile_observate].values
xx = x[:315:15]
# print(xx) #toate linile in anul2003
savetxt('Grupare_dupa_2003.csv', xx, delimiter=',', fmt='%s')

# matrice cu nr de ore pe anul 2003 pt ambele sexe-> 21 de observatii
xxx = df["Avg hrs per day sleeping"].values
hours_list_2003_Both = xxx[:315:15]
savetxt('Grupare_dupa_2003_BOTH.csv', hours_list_2003_Both, delimiter=',', fmt='%s')
# print("Both: 2003: avg hrs per day sleeping: regardless of the age")
# print("Media nr de ore pe care o pers il doarme,in medie, intr-o zi in anul 2003, indiferent de varsta sau zi",np.mean(hours_list_2003_Both))
# print(hours_list_2003_Both) #tabel cu datele pe care se aplica media

y = df["Avg hrs per day sleeping"].values
hours_list_2017_Both = y[14:315:15]
# print("Both: 2017: avg hrs per day sleeping: regardless of the age")
# print("Media nr de ore pe care o pers il doarme,in medie, intr-o zi in anul 2017, indiferent de varsta sau zi",np.mean(hours_list_2017_Both))
# print(hours_list_2017_Both) #tabel cu datele pe care se aplica media

variabile_observate = list(df2.columns)[:]
z = df2[variabile_observate].values
zz = z[::3]  # doar Both -> toti anii -> avg hours per day
# print(zz.size)
# print(zz)

# sortez crescator
zzz = zz[zz[:, 2].argsort()]
savetxt('Sortare_cresc_Both.csv', zzz, delimiter=',', fmt='%s')

# Grafic1
plot.figure(figsize=(12,6))
sns.countplot(x='Age Group',data=df)

# Grafic2
plot.figure(figsize=(12,6))
sns.countplot(x='Avg hrs per day sleeping',data=df)

# Grafic3
plot.figure(figsize=(12,6),dpi=68)
sns.scatterplot(x='Year',y='Type of Days',
             data=df,hue="Type of Days",
                linewidth=100, style="Year",
             )
plot.legend(bbox_to_anchor=(1, 1.02), loc='upper left', borderaxespad=0)


#Grafic4
plot.figure(figsize=(12, 10))
sns.barplot(x='Avg hrs per day sleeping', y='Year',
            data=df2,
            # linewidth=1,
            # size=6,
            # aspect=2,
            dodge=False
            # width=.5,
            # height=8
            )
plot.xlabel("Avg hrs per day sleeping")
plot.title("Ore vs Ani")
plot.ylim(2003, 2017)
plot.show()


