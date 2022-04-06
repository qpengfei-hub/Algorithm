import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def six_hump_camel(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Six_Hump_Camel')

    # 定义x, y
    x = np.linspace(x1_min_bound, x1_max_bound, 80)
    y = np.linspace(x2_min_bound, x2_max_bound, 80)
    # x = np.arange(x1_min_bound, x1_max_bound, 0.1)
    # y = np.arange(x2_min_bound, x2_max_bound, 0.1)

    ax.set_xlim(x1_min_bound, x1_max_bound)
    ax.set_ylim(x2_min_bound, x2_max_bound)

    X, Y = np.meshgrid(x, y)

    Z = (4 - 2.1 * X ** 2 + X ** 4 / 3) * X ** 2 + X * Y + (-4 + 4 * Y ** 2) * Y ** 2

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=-1.0316, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = -1.0316, x* = (0.0898, -0.7126) and (0.0898, 0.07126)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    #  x1 ∈ [-3, 3], x2 ∈ [-2, 2].
    # x1_min_bound = -3
    # x1_max_bound = 3
    # x2_min_bound = -2
    # x2_max_bound = 2
    x1_min_bound = -2
    x1_max_bound = 2
    x2_min_bound = -1
    x2_max_bound = 1
    six_hump_camel(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound)
