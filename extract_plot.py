import collections
import cleaner as cl
import matplotlib.pyplot as plt


''' extract 'Age-cat' data from dataframe '''
''' get counts per 'Age-cat' '''
cnt = []
#print(df.groupby('Age-cat').size())
cnt = cl.df['Age-cat'].value_counts()
#print(cnt)

''' sort the extracted data according to the item-names and
                    turn into dictionary '''
odcnt = collections.OrderedDict(sorted(cnt.items()))
#print(odcnt)

''' Plot data and Change title and axis labels here :   '''
fig = plt.figure('figure 1', figsize=(14,8))
plt.bar(range(len(odcnt)), odcnt.values(), align='center')  #plot the categories vs. counts 
plt.xticks(range(len(odcnt)), odcnt.keys(), rotation=45) #('JM10', 'JM11-14', 'JM15-17', 'JW10', 'JW11-14', 'JW15-17', 'SM18-19', 'SM20-24', 'SM25-29', 'SM30-34', 'SW18-19', 'SW20-24', 'SW25-29', 'SW30-34', 'VM35-39', 'VM40-44', 'VM45-49', 'VM50-54', 'VM55-59', 'VM60-64', 'VM65-69', 'VM70-74', 'VM75-79', 'VW35-39', 'VW40-44', 'VW45-49', 'VW50-54', 'VW55-59', 'VW60-64', 'VW65-69', 'VW70-74'))
plt.title('Bellville 10-Nov Parkrun (Unknown entries = '+str(cl.un_count)+')')
plt.xlabel('Age-category')
plt.ylabel('count')

plt.show()
