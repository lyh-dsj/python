import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15, 5)


# 构建convert_data_to_timeseries函数,
# 该函数目的是将原始数据中的某地销售数据转换为Series结构，
# 其索引为年月构成的时间，因为Series强大的功能方便我们进行统计
def convert_data_to_timeseries(infile, column):
    """
    infile:文件路径
    column:A地或B地的销售数据， 2:A   3:B
    return Series一维数组（A地或B地的销售数据，时间为索引）
    """
    data = pd.read_table(infile,
                         header=None,
                         encoding='utf-8',
                         sep=',',
                         index_col=False)
    # 把年和月拼接在一起
    data[4] = data[0].map(str) + '-' + data[1].map(str)
    # 设置为行索引
    data = data.set_index(data[4])
    # 构建一维数组Series
    dh = pd.Series(data[column].values, index=data[4])
    return dh


# 构建series对象，A地销售数据
df = convert_data_to_timeseries(r'C:\Users\luyuehua\Desktop\数据挖掘\data.txt', 2)
print(df)
df.plot()
# 构建series对象，B地销售数据
dh = convert_data_to_timeseries(r'C:\Users\luyuehua\Desktop\数据挖掘\data.txt', 3)
# 合并为dataframe对象
data = pd.DataFrame(list(zip(df, dh)), index=df.index)
print(data)
data.plot()
# 分别计算最大值，最小值，平均值。查看相关系数
print('\nMaximum:\n', data.max())
print('\nMinimum:\n', data.min())
print('\nMean:\n', data.mean())
print('\nCorrelation coefficients:\n', data.corr())

data.corr().plot()
plt.show()