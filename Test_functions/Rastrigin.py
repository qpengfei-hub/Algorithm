import numpy as np
import matplotlib.pyplot as plt



def rastrigin(bound):
    # 定义figure
    fig = plt.figure()

    # 将figure变为3d
    ax = plt.axes(projection='3d')
    fig.add_axes(ax)

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.zaxis.set_rotate_label(False)  # 一定要先关掉默认的旋转设置
    ax.set_zlabel('f(x1,x2)', rotation=90)
    ax.set_title('Rastrigin')

    # 定义x, y
    x = np.linspace(-bound, bound, 80)
    y = np.linspace(-bound, bound, 80)
    # x = np.arange(-bound, bound, 0.1)
    # y = np.arange(-bound, bound, 0.1)

    ax.set_xlim(-bound, bound)
    ax.set_ylim(-bound, bound)

    X, Y = np.meshgrid(x, y)

    Z = 20 + X ** 2 + Y ** 2 - 10 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y))
    # (X ** 2 - 10 * np.cos(2 * np.pi * X) + 10) + (Y ** 2 - 10 * np.cos(2 * np.pi * Y))

    # rstride:行之间的跨度  cstride:列之间的跨度
    # rcount:设置间隔个数，默认50个，ccount:列的间隔个数  不能与上面两个参数同时出现
    # rstride：行步长，默认值为 10
    # cstride：列步长，默认值为 10

    # color：表面的颜色
    # cmap：表面的颜色图 "rainbow" / "coolwarm" / viridis  一般的三维曲面是 rainbow
    # facecolors：表面中每个补丁的面部颜色
    # norm：Normalize 的一个实例，用于将值映射到颜色
    # vmin：要映射的最小值
    # vmax：要映射的最大值
    # shade：是否遮罩脸部颜色
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    # edgecolor='none'

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
    # xi ∈ [-5.12, 5.12], for all i = 1, …, d.
    bound = 5.12
    rastrigin(bound)
