from string import digits


class Phone(object):
    def __init__(self, phone_number):
        numbers = "".join(ch for ch in phone_number if ch in digits)
        if numbers.startswith("1"):
            numbers = numbers[1:]
        if len(numbers) != 10 or numbers[0] == "0" or numbers[3] in ["0", "1"]:
            raise ValueError("Invalid phone number")
        self.number = numbers

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"
