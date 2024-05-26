import math

def calculate_Ie(f_GT, f1, f2):
    """
    根据提供的频率计算 I_e。

    参数:
    f_GT (float): G/T 测量频率。
    f1 (float): 流量测量频率 1。
    f2 (float): 流量测量频率 2。

    返回:
    float: 计算的 I_e 值。
    """
    # 计算对数
    numerator = math.log10(f_GT / f2)
    denominator = math.log10(f1 / f2)

    # 计算 I_e
    Ie = numerator / denominator

    return Ie


def calculate_S0(f_m1, f_m2, Ie):
    """
    根据提供的参数计算 S_0。

    参数:
    f_m1 (float): 频率 f1 的通量测量值。
    f_m2 (float): 频率 f2 的通量测量值。
    I_e (float): 插值指数。

    返回:
    float: 计算的 S_0 值。
    """
    # 计算 S_0
    S_0 = f_m2 * (f_m1 / f_m2) ** Ie

    return S_0

# 示例用法:
f_GT = 3.0e9  # 示例 G/T 测量频率，单位为赫兹
f1 = 1.0e9  # 示例流量测量频率 1，单位为赫兹
f2 = 2.0e9  # 示例流量测量频率 2，单位为赫兹
f_m1 = 200.0  # 示例频率 f1 的流量测量值
f_m2 = 150.0  # 示例频率 f2 的流量测量值


Ie = calculate_Ie(f_GT, f1, f2)
S_0 = calculate_S0(f_m1, f_m2, Ie)
print(f"计算的 I_e 值: {Ie}")
print(f"计算的 S_0 值: {S_0}")