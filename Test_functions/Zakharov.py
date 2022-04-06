import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def zakharov(min_bound, max_bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Zakharov')

    # 定义x, y
    x = np.linspace(min_bound, max_bound, 80)
    y = np.linspace(min_bound, max_bound, 80)
    # x = np.arange(min_bound, max_bound, 0.1)
    # y = np.arange(min_bound, max_bound, 0.1)

    ax.set_xlim(min_bound, max_bound)
    ax.set_ylim(min_bound, max_bound)

    X, Y = np.meshgrid(x, y)

    Z = X ** 2 + Y ** 2 + (0.5 * X + 0.5 * 2 * Y) ** 2 + (0.5 * X + 0.5 * 2 * Y) ** 4

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=0, cmap=plt.get_cmap('viridis'))
    # f(x1, x2) 的minimum = 0, x* = (0, ..., 0)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    #  xi ∈ [-5, 10], for all i = 1, …, d
    min_bound = -10
    max_bound = 10
    zakharov(min_bound, max_bound)
