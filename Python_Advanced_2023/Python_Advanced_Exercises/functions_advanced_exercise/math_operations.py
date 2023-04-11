def math_operations(*args, **kwargs):
    result, pos = "", 1

    for num in args:

        if pos == 1:
            kwargs["a"] += num

        elif pos == 4:
            kwargs["m"] *= num

        elif pos == 2:
            kwargs["s"] -= num

        elif pos == 3:

            if num != 0:
                kwargs["d"] /= num

        pos += 1

        if pos > 4:
            pos = 1

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f"{key}: {value:.1f}\n"

    return result
