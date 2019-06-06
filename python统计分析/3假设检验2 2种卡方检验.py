#coding:utf8
#https://www.jianshu.com/p/c307d04eee56
#1。适合度分析（拟合性分析）
# 某科学家预言抛一个色子，各面向上的几率都相同。为了验证自己理论的正确性，该科学家抛了600次硬币，
# 结果为一点102次，二点102次，三点96次，四点105次，五点95次，六点100次。
# 显然这个结果和理论预期并不完全一样，那么，科学家的理论有错吗？我们就用Python来验证一下。

from scipy import stats
import numpy as np

from scipy import stats
obs = [102, 102, 96, 105, 95, 100]
exp = [100, 100, 100, 100, 100, 100]
stats.chisquare(obs, f_exp = exp)

#p>0.95很合适 没错






#2 独立性分析
#“独立性检验”验证从两个变量抽出的配对观察值组是否互相独立（例如：每次都从A国和B国各抽一个人，看他们的反应是否与国籍无关）。
#https://www.cnblogs.com/Yuanjing-Liu/p/9252844.html#_label1_1
#https://blog.csdn.net/QimaoRyan/article/details/72824766

#e.g. 三种农药的杀虫数据

# 杀虫效果	甲	乙	丙
# 死亡数	37	49	23
# 未死亡数	150	100	57
# 分析杀虫效果与农药类型是否有关

import numpy as np
from scipy.stats import chi2_contingency

d = np.array([[37, 49, 23], [150, 100, 57]])
print chi2_contingency(d)

#p=0.02 0。05 拒绝，杀虫效果与农药类型有关系，不独立
#第一个值为卡方值，第二个值为P值，第三个值为自由度，第四个为与原数据数组同维度的对应理论值