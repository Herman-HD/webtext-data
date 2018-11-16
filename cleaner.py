import pandas as pd
import numpy as np


''' declare lists here to use while constructing a dataframe at the end '''
n, N, names, t, c, cat, p, per, rek, rekord, times, pos, count = \
[], [], [], [], [], [], [], [], [], [], [], [], []

url = "bel1011_parkrun.txt"

''' find where record/row begins and extract each row raw-data '''
def getrowdata(file, text_split):
    rawdata = []
    with open(file) as fd :
        for line in fd :
            rawdata += line.split(text_split)
    return rawdata

''' extract row-data beginning at specific text_split-positions '''
rdata = getrowdata(url, '<td class="pos">')

''' make lists of each label/column by splitting the rows at specific '' index-text-position '''
for r in rdata :
    n += r.split('<')[0:1]  # "position"-number is in first index position for this split
    N += r.split('>')[3:4]  # "name" is in index 3:4 for this split
    t += r.split('>')[6:7]  # "time" index
    c += r.split('>')[9:10] # "age category" index
    p += r.split('>')[12:13] # "age grade" index
    rek += r.split('>')[22:23]  # "personal note" index
    
    
''' remove trailing-characters form list items '''
for z in N :
    names += z.split('</a')[0:1]  # clean names_
for z in t :
    times += z.split('</td')[0:1]  # clean times_
for z in c :
    cat += z.split('</a')[0:1]  # clean age-category_
for z in p :
    per += z.split('</td')[0:1]  # clean age-grade_
for z in rek :
    rekord += z.split('</td')[0:1]  # clean personal-note_

''' combine all lists into one '''
'''  make list of lists, every list has 6 items '''
ps = [list(i) for i in zip(n, names, times, cat, per, rekord)]
#print(ps[0:11])

''' remove all unknown entries (with names=<td/ or <td), and make final list = pos '''
un_count = 0
for p in ps :
    if p[1] != '<td/':  
        pos.append(p)
    else :
        un_count += 1
#print(pos[0:11])        

print('Unknown entries = : '+str(un_count))

   
''' add labels to form a dataframe '''
labels = ['pos', 'Name', '5km-Time', 'Age-cat', 'Age-grade', 'rek-Note']

df = pd.DataFrame(pos, columns=labels)  # make dataframe with a header=labels
df = df.drop([0, 0])  # remove first row, not used
print(df.head())


