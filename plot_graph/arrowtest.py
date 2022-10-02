# PYTHON_MATPLOTLIB_ANNOTATE_07

import numpy as np
import matplotlib.pyplot as plt

# file
file=open('plotvector.txt','r')
print('n=')
n=int(input())

# FigureとAxesを描画
fig, ax = plt.subplots(figsize = (7.5, 9))
ax.grid()
ax.set_xlim(75, 825)
ax.set_ylim(-450, 450)

# 矢印のプロパティを設定
arrow_dict = dict(arrowstyle = "->", color = "red")

# plot
for i in range(n):
    x,y,u,v=file.readline(n).split()
    x=float(x)
    y=float(y)
    u=float(u)
    v=float(v)
    #calc
    u=x+u*10
    v=y+v*10
    # 矢印を入れる
    ax.annotate("", size = 5, color = "red",
            xy = (u, v), xytext = (x, y), arrowprops = arrow_dict)
    #plt.plot(x,y,clip_on=False,marker='+', color='red',markersize=3,markeredgecolor="red")

#plt.show()
plt.show()