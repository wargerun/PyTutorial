import re


class Operation(object):
    @staticmethod
    def Sum(numbers):
        sum = 0
        for number in numbers:
            sum += float(number)
        return sum

    def getting(msg):
        return "Hello: " + msg.capitalize()


msg = Operation.getting("world")
print(msg)

numbers = re.split(', | ', "1 0, 2 3 4 5 6 7 8")
msg = Operation.Sum(numbers)

print(msg)
