def rectangle(*args, **kwargs):
    validation_condition = True
    for i in args:
        if not i == int(i):
            return 'Enter valid values!'

    def area():
        a = args[0]
        b = args[1]

        return a * b

    def perimeter():
        a = args[0]
        b = args[1]

        return 2 * (a + b)


    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle('2', 10))
