# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
boston = sd.load_boston()
fn = boston.feature_names
print(fn)
# 摇一摇
x, y = su.shuffle(boston.data, boston.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]
# 由四百棵四层决策树组成的正向激励集成回归器
model = se.AdaBoostRegressor(st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
# 从回归器中获取特征重要性
fi = model.feature_importances_
print(fi)
print(max(fi))
print(boston.feature_names[list(fi).index(max(fi))])
# 可视化不同特征的重要性排序
mp.figure('Feature Importance', facecolor='lightgray')
mp.title('Feature Importance', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Importance', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi.argsort()[::-1]  # 从高到低排序
pos = np.arange(sorted_indices.size)  # 矩形条对应的位置
# 数组的索引可以是列表，返回列表中索引对应的元素
mp.bar(pos, fi[sorted_indices], facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, fn[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()