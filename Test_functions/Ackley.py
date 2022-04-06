import numpy as np
import matplotlib.pyplot as plt


def ackley(bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel('x2')
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Ackley')

    # 定义x, y
    x = np.linspace(-bound, bound, 80)
    y = np.linspace(-bound, bound, 80)
    # x = np.arange(-bound, bound, 0.1)
    # y = np.arange(-bound, bound, 0.1)

    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)

    X, Y = np.meshgrid(x, y)

    # a = 20, b = 0.2 and c = 2π
    a = 20
    b = 0.2
    c = 2 * np.pi

    Z = -a * np.exp(-b * np.sqrt((X ** 2 + Y ** 2) / 2)) - np.exp(
        (np.cos(c * X) + np.cos(c * Y)) / 2) + np.e + a

    # Z = -20 * np.exp(-0.2 * np.sqrt((X ** 2 + Y ** 2 )/ 2)) - np.exp(
    #     (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y)) / 2) + np.e + 20

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.grid()
    # 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
    # zdir = 'z', offset = -2 表示投影到z = -2上
    ax.contour(X, Y, Z, zdir='z', offset=0, cmap=plt.get_cmap('viridis'))
    # f(x*) 的minimum = 0, at x* = (0, ..., 0)

    # 调整视角
    ax.view_init(elev=20,  # 仰角
                 azim=-135  # 方位角
                 )

    plt.show()

if __name__ == '__main__':
    # xi ∈ [-32.768, 32.768], for all i = 1, …, d
    # bound = 30
    bound = 5.12
    ackley(bound)