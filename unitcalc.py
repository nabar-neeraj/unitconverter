conversion_dict = {
    "length": {
        "meters": {
            "meters": lambda x: x,
            "yards": lambda x: 1.0936 * x,
            "feet": lambda x: 3.28084 * x,
            "centimeters": lambda x: 100 * x,
            "kilometers": lambda x: x / 1000.0,
            "miles": lambda x: x / 1000.0 / 1.60934
        },
        "yards": {
            "yards": lambda x: x,
            "meters": lambda x: x / 1.0936,
            "centimeters": lambda x: x / 1.0936 * 100,
            "feet": lambda x: 3 * x,
            "kilometers": lambda x: 0.0009144 * x,
            "miles": lambda x: 0.0009144 * x / 1.60934
        },
        "centimeters": {
            "centimeters": lambda x: x,
            "meters": lambda x: x / 100.0,
            "yards": lambda x: x * 1.0936 / 100,
            "feet": lambda x: x * 3.28084 / 100,
            "miles": lambda x: x * 100 * 1000 / 1.60934
        },
        "feet": {
            "feet": lambda x: x,
            "meters": lambda x: x / 3.28084,
            "yards": lambda x: x / 3.0,
            "centimeters": lambda x: x * 100 / 3.28084,
            "kilometers": lambda x: x * 3.28084 / 1000,
            "miles": lambda x: x * 3.28084 / 1000 / 1.60934
        },
        "miles": {
            "miles": lambda x: x,
            "kilometers": lambda x: 1.60934 * x,
            "meters": lambda x: 1.60934 * x * 1000,
            "centimeters": lambda x: 1.60934 * x * 1000 * 100,
            "feet": lambda x: 5280 * x,
            "yards": lambda x: 5280 * x / 3.0
        },
        "kilometers": {
            "kilometers": lambda x: x,
            "meters": lambda x: x * 1000,
            "centimeters": lambda x: x * 1000 * 100,
            "miles": lambda x: x / 1.60934,
            "yards": lambda x: x * 1093.61,
            "feet": lambda x: x * 1093.61 * 3
        }
    },
    "temperature": {
        "celsius": {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: 1.8 * x + 32,
            "kelvin": lambda x: x + 273,
        },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celsius": lambda x: (x - 32) * 5.0 / 9.0,
            "kelvin": lambda x: (x - 32) * 5.0 / 9.0 + 273,
        },
        "kelvin": {
            "kelvin": lambda x: x,
            "celsius": lambda x: x - 273,
            "fahrenheit": lambda x: 1.8 * (x - 273) + 32,
        }
    }
}

if __name__ == "__main__":
    try:
        print("{0:.4f}".format(conversion_dict["length"]["meters"]["miles"](2)))
    except KeyError:
        pass
    for k in conversion_dict.keys():
        print(k.capitalize())
        print(tuple(conversion_dict[k].keys()))
