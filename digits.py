class NumberFilter:
    def __init__(self, number):
        self.number = number

    def is_multiple_of_three(self):
        return self.number % 3 == 0

    def is_not_multiple_of_five(self):
        return self.number % 5 != 0

    def sum_of_digits_less_than_ten(self):
        return sum(int(digit) for digit in str(self.number)) < 10

    def meets_criteria(self):
        return (self.is_multiple_of_three() and
                self.is_not_multiple_of_five() and
                self.sum_of_digits_less_than_ten())


class NumberPrinter:
    def __init__(self, max_number):
        self.max_number = max_number

    def print_numbers(self):
        for number in range(self.max_number + 1):
            filter_instance = NumberFilter(number)
            if filter_instance.meets_criteria():
                print(number)


if __name__ == "__main__":
    printer = NumberPrinter(1000)
    printer.print_numbers()
