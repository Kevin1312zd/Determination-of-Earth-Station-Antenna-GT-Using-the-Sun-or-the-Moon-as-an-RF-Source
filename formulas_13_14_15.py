import math


def calculate_beamwidth(wavelength, antenna_diameter):
    """
    计算天线波束宽度 (B_w).

    参数:
    wavelength (float): 波长，单位为米
    antenna_diameter (float): 天线直径，单位为米

    返回:
    float: 波束宽度，单位为度
    """
    B_w = 68 * (wavelength / antenna_diameter)
    return B_w


def calculate_effective_rf_diameter(B_HPBW, f_GT):
    """
    计算有效RF直径 (r).

    参数:
    B_HPBW (float): 视在角直径，单位为度
    f_GT (float): G/T 测量频率，单位为GHz

    返回:
    float: 有效RF直径，单位为度
    """
    r = B_HPBW * (1.24 - 0.162 * math.log10(f_GT))
    return r


def calculate_beam_correction_factor(r, B_w):
    """
    计算波束修正因子 (C).

    参数:
    r (float): 有效RF直径，单位为度
    B_w (float): 天线波束宽度，单位为度

    返回:
    float: 波束修正因子
    """
    numerator = - (r / B_w) ** 2 * math.log10(2)
    denominator = (r / B_w) ** 2 * math.log10(2)
    C = 1 - math.exp(numerator) / denominator
    return C


# 示例使用
wavelength = 0.03  # 举例的值，单位为米 (例如10 GHz对应的波长)
antenna_diameter = 3.0  # 举例的值，单位为米
B_HPBW = 0.525  # 视在角直径，单位为度 (例如太阳)
f_GT = 10.0  # 举例的值，单位为GHz

B_w = calculate_beamwidth(wavelength, antenna_diameter)
r = calculate_effective_rf_diameter(B_HPBW, f_GT)
C = calculate_beam_correction_factor(r, B_w)

print(f"Antenna Beamwidth (B_w): {B_w} degrees")
print(f"Effective RF Diameter (r): {r} degrees")
print(f"Beam Correction Factor (C): {C}")

#Beam Correction Factor (C)的最终结果可以应用到公式2