import math

def calculate_solar_flux_density(T_d, wavelength):
    """
    计算太阳辐射通量密度 (F_s)

    参数:
    T_d (float): 太阳亮度温度 (开尔文)
    wavelength (float): 波长 (米)

    返回:
    float: 太阳辐射通量密度 (F_s)，单位是Jansky (10^-26 W/m²/Hz)
    """
    k_B = 1.38e-23  # 玻尔兹曼常数 (W/K/Hz)
    alpha = 0.25  # 太阳的角半径 (度)

    # 使用给定公式计算 F_s
    F_s = 2 * k_B * T_d * math.pi * (alpha * math.pi / 180)**2 * (wavelength**-2)

    return F_s

# 示例使用:
T_d = 6000  # 示例值：太阳亮度温度 (开尔文)
wavelength = 0.01  # 示例值：波长 (米) (10 厘米)
F_s = calculate_solar_flux_density(T_d, wavelength)
print(f"太阳辐射通量密度 (F_s): {F_s} Jansky")
