import re


class StringOperations:
    @staticmethod
    def convert_str_number_to_float(txt):
        clean_txt = re.sub(r'[^\d,]', '', txt)
        float_value = float(clean_txt.replace(',', '.'))
        return float_value

    @staticmethod
    def add_decimal_point(number):
        number_str = str(number)
        return number_str[0] + '.' + number_str[1:]

    @staticmethod
    def extract_numeric_part(txt):
        match = re.search(r'(\d+)\.(\d+)', txt)
        if match:
            return match.group(1) + match.group(2)
        return None

    @staticmethod
    def extract_screen_size_and_dimension(text):
        pattern = r'экран (\d+(\.\d+)?)"\s+\w+\s+\((\d+)x(\d+)\)'
        match = re.search(pattern, text)

        if match:
            screen_size = match.group(1)
            resolution = f"{match.group(3)}x{match.group(4)}"
            return screen_size, resolution
        else:
            return None, None

    @staticmethod
    def extract_device_specs(text):
        os_match = re.search(r'(Apple iOS|Android|Windows Phone|Nokia Series 30+|HarmonyOS)\s?\w*', text, re.IGNORECASE)
        screen_size_match = re.search(r'экран\s?(\d+(\.\d+)?)', text, re.IGNORECASE)
        screen_dimension_match = re.search(r'(\d+x\d+)', text)
        ram_match = re.search(r'ОЗУ\s?(\d+ ГБ)', text)
        memory_match = re.search(r'память\s?(\d+ ГБ)', text)

        os_value = os_match.group(1) if os_match else None
        screen_size_value = screen_size_match.group(1) if screen_size_match else None
        screen_dimension_value = screen_dimension_match.group(1) if screen_dimension_match else None
        ram_value = ram_match.group(0) if ram_match else None
        memory_value = memory_match.group(0) if memory_match else None

        param = [os_value, screen_size_value, screen_dimension_value, ram_value, memory_value]
        return param
