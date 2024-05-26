import math


def calculate_y(Psd, Psc):
    """
    计算天线系统接收源功率密度与冷天空功率密度之差的线性表示值y。

    参数:
    Psd (float): 天线系统指向RF源时接收到的功率 (dB)。
    Psc (float): 天线系统指向冷天空时接收到的功率 (dB)。

    返回:
    float: 功率密度差值的线性表示值y。
    """
    Pd_diff = abs(Psd - Psc)
    y = 10 ** (Pd_diff / 10)
    return y


# 示例使用
Psd_example = 50  # 示例值，单位为dB
Psc_example = 55  # 示例值，单位为dB
y_value = calculate_y(Psd_example, Psc_example)
print(f"y的计算结果为: {y_value}")
