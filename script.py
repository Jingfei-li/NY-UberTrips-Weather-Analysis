import pandas as pd
# readin data
df = pd.read_excel('NY Weather Data - Apr 14 - Jul 14 (1).xlsx')

# Get the row index of each month (use string type to determine whether it is obtained)
data_index = [i for i in range(len(df)) if str(df[2014][i]).isalpha()]

# Divide by month and store in the data list
data = []
for i in range(len(data_index)):
    if i!=len(data_index)-1:
        data.append(df.iloc(axis=0)[data_index[i]:data_index[i+1]-1].reset_index(drop = True))
    else:data.append(df.iloc(axis=0)[data_index[i]:].reset_index(drop = True))

# get all columns
column_names = [i for i in df.columns.tolist() if 'Unnamed' not in str(i)]

# divide columns into 3
columns = []
# column_names[1:-2]Remove the first and last two
for i in column_names[1:-2]:
    columns =columns+((i+',')*3).split(',')[:-1]

# rename
mouth_dict = {'Apr':'4','May':'5','Jun':'6',"Jul":'7'}

# for loop change the year
for frame in data:
    frame[2014][1:] = frame[2014][1:].apply(lambda x:'2014/'+mouth_dict[frame[2014][0]]+'/'+str(x))
    frame.columns = [str(df.columns[0])]+columns+df.columns[-2:].tolist()
    
new_cols = []
for i,j in zip(data[0].columns[1:-2],data[0].iloc(axis =0)[0][1:-2]):
    new_cols.append(i+'-'+j)

new_cols = ['Date'] + new_cols + data[0].columns[-2:].tolist()

for frame in data:
    frame.drop(0,axis=0,inplace=True)
    frame.columns = new_cols

# combine 
final = pd.concat(data,axis=0,ignore_index=True)
# write csv
final.to_csv('final.csv',index=None)
