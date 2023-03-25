def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 0
        raise ValueError

        raise IndexError


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
result = []
for key in data:
    res = divider(key, data[key])
    result.append(res)




print(result)