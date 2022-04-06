import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def bohachevsky(bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Bohachevsky')

    # 定义x, y
    x = np.linspace(-bound, bound, 80)
    y = np.linspace(-bound, bound, 80)
    # x = np.arange(-bound, bound, 0.1)
    # y = np.arange(-bound, bound, 0.1)

    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)

    X, Y = np.meshgrid(x, y)

    Z1 = X ** 2 + 2 * Y ** 2 - 0.3 * np.cos(3 * np.pi * X) - 0.4 * np.cos(4 * np.pi * Y) + 0.7
    Z2 = X ** 2 + 2 * Y ** 2 - 0.3 * np.cos(3 * np.pi * X) * np.cos(4 * np.pi * Y) + 0.3
    Z3 = X ** 2 + 2 * Y ** 2 - 0.3 * np.cos(3 * np.pi * X + 4 * np.pi * Y) + 0.3

    # 一共有3个形式，这里只显示f1(x1, x2) = Z1
    # The Bohachevsky functions all have the same similar bowl shape. The one shown above is the first function.
    ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z1, zdir='z', offset=0, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = 0 ，at x* = (0, 0), for all j = 1,2,3

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    # xi ∈ [-100, 100], for all i = 1, 2.
    # bound = 10
    bound = 5.12
    bohachevsky(bound)
