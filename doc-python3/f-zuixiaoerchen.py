#https://blog.csdn.net/zwq912318834/article/details/78476842
import numpy
from scipy.optimize import leastsq
import pylab


def zuixiaoerchen(arrayY, picTitle):
    print(f"arrayY: {arrayY}")
    print(f"picTitle: {picTitle}")

    if len(arrayY) == 0:
        return [0, 0, 0]

    # 取得最大销量，作为纵坐标的峰值标准
    maxValue = max(arrayY)

    # 设置横坐标和纵坐标的值
    # def arange(start=None, stop=None, step=None, dtype=None)
    x = numpy.arange(1, len(arrayY) + 1, 1)

    # def array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
    y = numpy.array(arrayY)

    # 第1個拟合，设置自由度為1 : (y = ax + b)
    z = numpy.polyfit(x, y, 1)
    # z: [  0.46428571  13.35238095]
    print(f"z: {z}")

    # 生成的多項式對象(y = ax + b)
    p = numpy.poly1d(z)
    # p: -0.1448x + 13.23
    print(f"p: {p}")

    if z[0] > 0:

        # 绘制原曲线及 拟合后的曲线

        # 原曲线 , 设置颜色(蓝色)和标签
        pylab.plot(x, y, 'b^-', label='original sales growth')

        # 自由度为1的趋势曲线, 设置颜色(蓝色)和标签
        pylab.plot(x, p(x), 'gv--', label=f'y = {z[0]}x + {z[1]}')

        # 设置图表的title
        pylab.title(f"picTitle: {picTitle}")

        # 设置横坐标，纵坐标的范围 [xmin=0, xmax=16, ymin=0, ymax=30]
        pylab.axis([0, len(arrayY) + 1, 0, maxValue + 1])
        pylab.legend()

        # 保存成图片，需要提前创建文件夹 Growth，程序不会自动创建
        pylab.savefig(f"Growth/{picTitle}.png", dpi=96)

        # 清除图表设置，以防止曲线多次累计
        # 如果不清除，那么在这个程序运行起见，多次调用这个函数时，会不断将之前的曲线累计到新图片中
        pylab.clf()

    return [z[0], z[1], maxValue]

if __name__ == '__main__':

    # 用最小二乘法，生成销量趋势
    sales = [10, 15, 8, 20, 16, 19, 11, 30, 21, 15, 19, 17, 16, 22, 17]
    a, b, maxSale = zuixiaoerchen(sales, "sales Growth")
    growth = a
    maxSale = maxSale

    print(f"growth = {growth}, maxSale = {maxSale}")

# 输出结果
arrayY: [10, 15, 8, 20, 16, 19, 11, 30, 21, 15, 19, 17, 16, 22, 17]
picTitle: sales Growth
z: [  0.46428571  13.35238095]
p:  
0.4643 x + 13.35
growth = 0.4642857142857137, maxSale = 30
