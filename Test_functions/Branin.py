import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def branin(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Branin')

    # 定义x, y
    x = np.linspace(x1_min_bound, x1_max_bound, 80)
    y = np.linspace(x2_min_bound, x2_max_bound, 80)
    # x = np.arange(x1_min_bound, x1_max_bound, 0.1)
    # y = np.arange(x2_min_bound, x2_max_bound, 0.1)

    ax.set_xlim(x1_min_bound, x1_max_bound)
    ax.set_ylim(x2_min_bound, x2_max_bound)

    X, Y = np.meshgrid(x, y)
    # The Branin, or Branin-Hoo, function has three global minima.
    # The recommended values of a, b, c, r, s and t are:
    # a = 1, b = 5.1 ⁄ (4π2), c = 5 ⁄ π, r = 6, s = 10 and t = 1 ⁄ (8π).
    a = 1
    b = 5.1/(4 * np.pi ** 2)
    c = 5/np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)

    Z = a * (Y - b * X ** 2 + c * X - r) ** 2 + s * (1 - t) * np.cos(X) + s

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=0.397887, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = 0.397887, at x* = (-pi, 12.275),(pi, 2.275) and (9.42478, 2.475)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()

if __name__ == '__main__':
    # x1 ∈ [-5, 10], x2 ∈ [0, 15].
    x1_min_bound = -2
    x1_max_bound = 10
    x2_min_bound = 0
    x2_max_bound = 15
    branin(x1_min_bound, x1_max_bound, x2_min_bound, x2_max_bound)