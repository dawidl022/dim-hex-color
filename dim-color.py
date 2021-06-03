from sys import argv

if len(argv) != 2 or len(argv[1]) not in (3, 4, 6, 7):
    print("usage: python3 dim-color.py <hex-color>")
else:
    color = argv[1]
    dimmed_color = []
    for digit in color:
        if digit.lower() not in ("0", "#", "a"):
            digit = chr(ord(digit) - 1)
        elif digit.lower() == "a":
            digit = "9"
        dimmed_color.append(digit)
    print("".join(dimmed_color))
