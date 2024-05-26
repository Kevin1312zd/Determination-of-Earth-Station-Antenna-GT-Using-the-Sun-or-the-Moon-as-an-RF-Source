def calculate_wavelength(frequency_hz):
    """
    计算波长

    参数:
    frequency_hz (float): 测量频率 (Hz)

    返回:
    float: 波长 (米)
    """
    speed_of_light = 299792458  # 光速 (米/秒)
    wavelength = speed_of_light / frequency_hz
    return wavelength

# 示例值（应根据实际情况替换）
frequency_hz = 10e9  # 10 GHz 示例频率

# 计算波长
wavelength = calculate_wavelength(frequency_hz)
print(f"Wavelength: {wavelength} meters")