import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bukin_N_6(x_min_bound, x_max_bound, y_min_bound, y_max_bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Bukin N_6')

    # 定义x, y
    x = np.linspace(x_min_bound, x_max_bound, 80)
    y = np.linspace(y_min_bound, y_max_bound, 80)
    # x = np.arange(x_min_bound, x_max_bound, 0.1)
    # y = np.arange(y_min_bound, y_max_bound, 0.1)

    ax.set_xlim(x_min_bound, x_max_bound)
    ax.set_ylim(y_min_bound, y_max_bound)

    X, Y = np.meshgrid(x, y)

    Z = 100 * np.sqrt(np.abs(Y - 0.01 * (X ** 2)) )+ 0.01 * np.abs(X + 10)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=0, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = 0, at x* = (-10, 1)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()

if __name__ == '__main__':
    # x1 ∈ [-15, -5], x2 ∈ [-3, 3]
    x_min_bound = -15
    x_max_bound = -5
    y_min_bound = -3
    y_max_bound = 3
    bukin_N_6(x_min_bound, x_max_bound, y_min_bound, y_max_bound)