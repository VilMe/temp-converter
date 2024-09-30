

TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}


def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value