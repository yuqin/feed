# coding: utf-8
# __author__: u"Yuqin"
"""
这里研究预处理之后的数据、在不同的模型下效果如何, 一个模型为一个class

这里的x y要自己构造

"""

from sklearn import tree
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)

clf.predict([[1, 1]])