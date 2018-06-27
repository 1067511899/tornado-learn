# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1.读入数据
import pandas as pd
data1 = pd.read_csv('train.csv',
                  sep=',', index_col='PassengerId', engine='python')
# 看下前几行的数据
data1.head()
# 描述性统计
data1.describe()
# 相关系数
data1.corr()
# 2.数据清洗
# help(pd.DataFrame.fillna) fillna的帮助命令
# 用均值填补空值
data1['Age'] = data1['Age'].fillna(data1['Age'].mean())
# 用后一个值填补空值
data1['Embarked'] = data1['Embarked'].fillna(method='bfill')
# 测试集Fare有个空值
# data11['Fare']=data11['Fare'].fillna(method='bfill')
# 删除指标（主观认为：Name，Ticket、Cabin)
data2 = data1.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# 离散数据的转换
# train_as_dicts=[dict(r.iteritems()) for _, r in data2[['Sex','Embarked']].iterrows()]
# 先把DataFrame格式的数据转成字典格式的，目的为了用DictVectorizer函数
train_as_dicts = [dict(r.iteritems()) for _, r in data2.iterrows()]
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False)
data3 = vec.fit_transform(train_as_dicts)
data4 = pd.DataFrame(data3, columns=vec.get_feature_names())
'''#把处理好的数据导出用于分布式
data4.to_csv('train_preprocess.csv')'''
# 3.训练集和测试集
y = data4['Survived']
x = data4.drop(['Survived'], axis=1)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# 4.logistics回归模型
from sklearn import linear_model
logreg = linear_model.LogisticRegression()  # max_iter=200,solver='lbfgs'
logreg.fit(x_train, y_train)
coef = logreg.coef_
intercept = logreg.intercept_
print(coef)
print(logreg.intercept_)
y_pred = logreg.predict(x_test)
# 模型评估
from sklearn.metrics import accuracy_score
# 准确率
accuracy_score(y_test, y_pred)  # 0.79372197309417036
'''#随机森林
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(x_train,y_train)
print(clf.feature_importances_)
y_pred1=clf.predict(x_test)
accuracy_score(y_test,y_pred1)  #0.82959641255605376'''

'''
#输出预测值
y_pred=logreg.predict(data4)
pd.DataFrame(y_pred).to_csv('E:/工作/分类算法/kaggle_competitions/test_sample.csv')'''
