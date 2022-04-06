import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def goldstein_price(bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Goldstein-Price')

    # 定义x, y
    x = np.linspace(-bound, bound, 80)
    y = np.linspace(-bound, bound, 80)
    # x = np.arange(-bound, bound, 0.1)
    # y = np.arange(-bound, bound, 0.1)

    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)

    X, Y = np.meshgrid(x, y)

    Z = (1 + (X + Y + 1) ** 2 * (19 - 14 * X + 3 * X ** 2 - 14 * Y + 6 * X * Y + 3 * Y ** 2)) * (
                30 + (2 * X - 3 * Y) ** 2 * (18 - 32 * X + 12 * X ** 2 + 48 * Y - 36 * X * Y + 27 * Y ** 2))

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=3, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = 3, at x* = (0, -1)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    # xi ∈ [-2, 2], for all i = 1, 2.
    bound = 2
    goldstein_price(bound)