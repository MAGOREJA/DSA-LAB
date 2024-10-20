import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dailyActivity_Merged.csv')

# print(df.dtypes)
list1 = df['ActivityDate'].values.tolist()
list2 = df['TotalSteps'].values.tolist()

# plt.plot(list1,list2)
# plt.show()

#prob 2
list3 = df['ActivityDate'].values.tolist()
list4 = df['TotalDistance'].values.tolist()
# plt.bar(list3,list4,color=['red','blue','green','yellow','orange'])
# plt.show()

#prob 3
df = pd.read_csv('sleepDay_merged.csv')
x = df['SleepDay'].values.tolist()
y = df['TotalTimeInBed'].values.tolist()
plt.scatter(x,y,color='Green')
plt.show()

#prob 4
df = pd.read_csv('hourlySteps_merged.csv')

test_df = df[df['ActivityHour'].str.contains('4/12/2016')]

x = test_df['ActivityHour'].values.tolist()
y = test_df['StepTotal'].values.tolist()

# plt.pie(y, labels=x, autopct='%1.1f%%', startangle=140)
# plt.title('Hourly Steps on 12th April 2016')
# plt.axis('equal')
# plt.show()