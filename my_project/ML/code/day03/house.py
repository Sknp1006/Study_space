# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm
boston = sd.load_boston()
# 特征名
print(boston.feature_names)
# 506个数据
print(boston.data.shape)
# 506个输出
print(boston.target.shape)
# 对于机器学习来说，数据越有规律越不好，所以要打乱顺序，输入和输出对应，所以要一起洗
x, y = su.shuffle(boston.data, boston.target, random_state=7)  # 指定随机种子，按照随机种子创建随机序列
train_size = int(len(x) * 0.8)
# train_size 划分训练集和测试集的数字
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]
# 单颗四层决策树
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# r2 拟合精度
print(sm.r2_score(test_y, pred_test_y))
# 正向激励adaboost，400颗四层决策树的正向激励集成回归器
model = se.AdaBoostRegressor(st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
