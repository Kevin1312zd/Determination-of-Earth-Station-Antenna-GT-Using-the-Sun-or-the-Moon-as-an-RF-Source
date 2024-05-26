import math


def calculate_d(r0, a, el):
    """
    根据提供的参数计算月球的角直径 d。

    参数:
    r0 (float): 地月距离，单位为公里。
    a (float): 地球赤道半径，单位为公里。
    el (float): 月亮的仰角，单位为度。

    返回:
    float: 计算的月球的角直径 d，单位为度。
    """
    # 计算 d
    d = 0.5182 / ((r0 / a) / 60.268 - 0.0166 * math.sin(math.radians(el)))

    return d


# 示例用法:
r0 = 384400.0  # 示例地月距离，单位为公里
a = 6378.1366  # 示例地球赤道半径，单位为公里
el = 45.0  # 示例月亮的仰角，单位为度

d = calculate_d(r0, a, el)
print(f"计算的月球的角直径 d: {d} 度")
