import math
from scipy.constants import Boltzmann


def calculate_gt_moon(y, L0, wavelength, beam_correction_factor,alpha):
    # 常数
    factor = 8 * math.pi * Boltzmann

    # 计算G/T
    gt = 10 * math.log10((factor * (y - 1)) / (L0 * (wavelength ** 2) * beam_correction_factor * alpha))

    return gt


# 示例参数
y = 2.0  # 源噪声功率密度与冷空功率密度之差的线性值
L0 = 0.2  # 月亮通量密度，SFU单位
wavelength = 0.1  # 波长，单位为米
beam_correction_factor = 1.0  # 波束修正因子，线性无单位
alpha = 1.31   #大气衰减在仰角处通常表示为线性无单位

# 计算G/T
gt_value = calculate_gt_moon(y, L0, wavelength, beam_correction_factor,alpha)
print("Calculated G/T value:", gt_value, "dB/K")
