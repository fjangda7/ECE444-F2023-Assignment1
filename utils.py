class Utils:
    @staticmethod
    def reversed(number):
        if isinstance(number, int):
            sign = 1
            if number < 0:
                number = abs(number)
                sign = -1

            reversedNum = 0
            while number > 0:
                reversedNum = reversedNum * 10 + number % 10
                number //= 10

            return sign * reversedNum
        else: 
            raise ValueError("Incorrect input: expected integer.")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            binary = bin(number)
            octal = oct(number)
            return binary, octal
        else: 
            raise ValueError("Incorrect input: expected integer.")
