def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""


# Test code 1
print(rectangle(2, 10))
# Test code 2
print(rectangle('2', 10))
