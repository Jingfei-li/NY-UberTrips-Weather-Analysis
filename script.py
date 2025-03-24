import pandas as pd
# 读取文件
df = pd.read_excel('NY Weather Data - Apr 14 - Jul 14 (1).xlsx')

# 获取每个月份的行索引（用是否是字符串类型来判断获取）
data_index = [i for i in range(len(df)) if str(df[2014][i]).isalpha()]

# 根据每个月进行划分，存入到data列表当中
data = []
for i in range(len(data_index)):
    if i!=len(data_index)-1:
        data.append(df.iloc(axis=0)[data_index[i]:data_index[i+1]-1].reset_index(drop = True))
    else:data.append(df.iloc(axis=0)[data_index[i]:].reset_index(drop = True))

# 获取全部的columns
column_names = [i for i in df.columns.tolist() if 'Unnamed' not in str(i)]

# 将columns变成三个三个
columns = []
# column_names[1:-2]是去除开头和末尾两个
for i in column_names[1:-2]:
    columns =columns+((i+',')*3).split(',')[:-1]

# 解释英文含义
mouth_dict = {'Apr':'4','May':'5','Jun':'6',"Jul":'7'}

# 循环改变年份
for frame in data:
    # frame是不同月份的数据
    frame[2014][1:] = frame[2014][1:].apply(lambda x:'2014/'+mouth_dict[frame[2014][0]]+'/'+str(x))
    frame.columns = [str(df.columns[0])]+columns+df.columns[-2:].tolist()
    
# 这时候需要改变每个月份的表头
new_cols = []
for i,j in zip(data[0].columns[1:-2],data[0].iloc(axis =0)[0][1:-2]):
    new_cols.append(i+'-'+j)
# 组合表头
new_cols = ['Date'] + new_cols + data[0].columns[-2:].tolist()
# 循环改变各个月份的表头
for frame in data:
    frame.drop(0,axis=0,inplace=True)
    frame.columns = new_cols

# 对各个月份进行拼接
final = pd.concat(data,axis=0,ignore_index=True)
# 保存成csv文件
final.to_csv('final.csv',index=None)