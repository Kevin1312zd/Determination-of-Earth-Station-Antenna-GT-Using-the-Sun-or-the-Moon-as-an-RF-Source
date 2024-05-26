def calculate_L0(f, T, d):
    """
    根据提供的参数计算 L_0。

    参数:
    f (float): G/T 测量频率，单位为 GHz。
    T (float): 月球平均亮度温度，单位为开尔文。
    d (float): 月球的角直径，单位为度。

    返回:
    float: 计算的 L_0 值，单位为 SFU。
    """
    # 计算 L_0
    L_0 = 7.349 * (f ** 2) * T * (d ** 2)

    # 将 L_0 转换为 SFU
    L_0_SFU = L_0 * 1e4

    return L_0_SFU


# 示例用法:
f = 10.0  # 示例 G/T 测量频率，单位为 GHz
T = 250.0  # 示例月球平均亮度温度，单位为开尔文
d = 0.5  # 示例月球的角直径，单位为度

L_0_SFU = calculate_L0(f, T, d)
print(f"计算的 L_0 值（单位：SFU）: {L_0_SFU}")
