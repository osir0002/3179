

intervals = 40000000


for index, row in df.iterrows():
    if  row['Defense_Budget'] > 42000000000:
        MoneyD[row['country']] = row['Defense_Budget']





MoneyD2 = dict()

for key in MoneyD:
    MoneyD2[key] = range(intervals, MoneyD[key], intervals)

