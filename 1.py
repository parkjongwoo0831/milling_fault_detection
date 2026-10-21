#데이터 탐색

import pandas as pd
df = pd.read_csv('C:\\pythoncode\\milling_fault_detection\\mill.csv', sep=',')
print(df.describe())
print(df.head())
print(df.tail())
print(df.info(  ))

#가시화
import seaborn as sns 
import matplotlib.pyplot as plt
sns.pairplot(df)
plt.show()