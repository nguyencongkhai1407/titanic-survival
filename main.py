import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Finding the path to file
for dirpath, _, file_names in os.walk("data/"):
    for filename in file_names:
        print(os.path.join(dirpath, filename))


training = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
# print(training.head())

training['train_test'] = 1
test['train_test'] = 0
test['Survived'] = np.NaN
all_data = pd.concat([training,test])

print(all_data.columns)

# Take a closer look at the data given (data types and number of null values)
# print(training.info())
# print(training.describe())

# look at numeric and categorical values separately
df_num = training[['Age','SibSp','Parch','Fare']]
df_cat = training[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]

# for i in df_num.columns:
#     plt.hist(df_num[i])
#     plt.title(i)
#     plt.show()

# Find correlation between independent variables
# print(df_num.corr())
# sns.heatmap(df_num.corr(), annot=True)
# plt.show()

# compare survival rate across Age, SibSp, Parch, and Fare
print(pd.pivot_table(training, index = 'Survived', values = ['Age','SibSp','Parch','Fare']))
