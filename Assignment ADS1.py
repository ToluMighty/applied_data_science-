import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 



df = pd.read_excel('Africa Covid 19 cases.xlsx')

data = df[['Sub-Region', 'Country', 'Confirmed', 'Recovered', 'Deaths']]

Total = [df['Confirmed'].sum(), df['Recovered'].sum(), df['Deaths'].sum()]
Total_tab = pd.DataFrame(Total,['Confirmed', 'Recovered', 'Deaths'], columns=['Sum'])

print(Total_tab)

#plotting of bar chart 


def bar_chart(x_value, list, title):
    plt.figure()
    plt.bar(x_value, list)
    plt.title(title, fontsize= 9)
    plt.show()

x_value = Total_tab.index
my_total = Total_tab['Sum']
title = 'A Bar Chart showing total number of confirmed, Recovered and Deaths'

plt.show(bar_chart(x_value, my_total, title))

#plotting line graph 

Subregion_grp = data.groupby('Sub-Region')[['Confirmed', 'Recovered', 'Deaths']].sum()
print(Subregion_grp)


def line_plot(x_value, V_list, xticks, label, title):
    plt.figure(figsize=(8,5))
    for i in range(len(V_list)):
        plt.plot(x_value, V_list[i], label=label[i])
    plt.legend()
    plt.xticks(x_value,xticks)
    plt.title(title, fontsize=9)
    plt.show()
    
    
x_value = Subregion_grp.index
V_list = [Subregion_grp['Confirmed'], Subregion_grp['Recovered'], Subregion_grp['Deaths']]
xticks = ['Eastern Africa ', 'Middle Africa', 'Northern Africa', 'Southern Africa', 'Western Africa']
label = ['Confirmed', 'Recovered', 'Deaths']
title = 'A line plot of confirmed, Recovered and Deaths for the region in Africa'

plt.show(line_plot(x_value, V_list, xticks, label, title))


#plot pie chat

def subplot_piechart(x_value, label, title):
    plt.figure(figsize=(15,10))
    for i in range(len(x_value)):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.pie(x_value[i], labels=label)
    plt.show()    
    
x_value = [Subregion_grp['Confirmed'], Subregion_grp['Recovered'], Subregion_grp['Deaths']]
label = Subregion_grp.index
title = ['Confirmed', 'Recovered', 'Deaths']

plt.show(subplot_piechart(x_value, label, title))
    
