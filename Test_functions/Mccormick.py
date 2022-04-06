import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def mccormick(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Mccormick')

    # 定义x, y
    x = np.linspace(x1_min_bound, x1_max_bound, 80)
    y = np.linspace(x2_min_bound, x2_max_bound, 80)
    # x = np.arange(x1_min_bound, x1_max_bound, 0.1)
    # y = np.arange(x2_min_bound, x2_max_bound, 0.1)

    ax.set_xlim(x1_min_bound, x1_max_bound)
    ax.set_ylim(x2_min_bound, x2_max_bound)

    X, Y = np.meshgrid(x, y)

    Z = np.sin(X + Y) + (X - Y) ** 2 - 1.5 * X + 2.5 * Y + 1

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=-1.9133, cmap=plt.get_cmap('viridis'))
    # f(x1, x2) 的minimum = -1.9133, x* = (-0.54719, -1.54719)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    #  x1 ∈ [-1.5, 4], x2 ∈ [-3, 4].
    x1_min_bound = -1.5
    x1_max_bound = 4
    x2_min_bound = -3
    x2_max_bound = 4
    mccormick(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound)
