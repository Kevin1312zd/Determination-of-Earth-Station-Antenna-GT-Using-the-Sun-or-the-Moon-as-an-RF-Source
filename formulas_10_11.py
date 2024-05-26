import math


def calculate_T(f, phi, psi):
    """
    根据提供的参数计算月球平均亮度温度 T。

    参数:
    f (float): 测量频率，单位为 GHz。
    phi (float): 月相角度，单位为度。
    psi (float): 月相滞后角度，单位为度。

    返回:
    float: 计算的月球平均亮度温度 T，单位为开尔文。
    """
    # 计算 T0
    T0 = 207.7 + 24.43 / f

    # 计算 T1 / T0
    T1_T0 = 0.004212 * f ** 1.224

    # 计算 T
    T = T0 * (1 - T1_T0 * math.cos(math.radians(phi - psi)))

    return T


def calculate_phi(R, Delta, psi):
    """
    根据提供的参数计算月相角度 phi。

    参数:
    R (float): 地心距离（从地球到太阳的距离），单位为公里。
    Delta (float): 地心距离（从地球到月球的距离），单位为公里。
    psi (float): 月球的地心延伸角度，单位为度。

    返回:
    float: 计算的月相角度 phi，单位为度。
    """
    # 计算 phi
    phi = math.degrees(math.atan2(R * math.sin(math.radians(psi)), Delta - R * math.cos(math.radians(psi))))

    return phi


# 示例用法:
f = 10.0  # 示例测量频率，单位为 GHz
R = 149597870.7  # 示例地心距离（从地球到太阳的距离），单位为公里
Delta = 384400  # 示例地心距离（从地球到月球的距离），单位为公里
psi = 5.0  # 示例月球的地心延伸角度，单位为度

phi = calculate_phi(R, Delta, psi)
T = calculate_T(f, phi, psi)

print(f"计算的月相角度 phi: {phi} 度")
print(f"计算的月球平均亮度温度 T: {T} 开尔文")
