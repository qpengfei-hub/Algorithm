import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def shubert(bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Shubert')

    # 定义x, y
    x = np.linspace(-bound, bound, 80)
    y = np.linspace(-bound, bound, 80)
    # x = np.arange(-bound, bound, 0.1)
    # y = np.arange(-bound, bound, 0.1)

    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)

    X, Y = np.meshgrid(x, y)
    part1 = part2 = 0
    for i in range(1,6): # i = 1-5
        part1 += (i * np.cos((i + 1) * X + i))
        part2 += (i * np.cos((i + 1) * Y + i))
    Z = part1 * part2

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=-186.7309, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = -186.7309

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()


if __name__ == '__main__':
    # xi ∈ [-10, 10], for all i = 1, 2, although this may be restricted to
    # the square xi ∈ [-5.12, 5.12], for all i = 1, 2.
    # bound = 10
    bound = 5.12
    shubert(bound)