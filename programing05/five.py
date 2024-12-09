import sys

def arg(argv):
    temperatures = [float(x) for x in argv]
    maximum = max(temperatures)
    minimum = min(temperatures)
    mean = sum(temperatures) / len(temperatures)
    print(f"Maximum temperature: {maximum}, Minimum temperature: {minimum}, Mean temperature: {mean}")

argv = sys.argv[1:]
if len(argv) < 1:
    print("Enter some numbers.")
else:
    arg(argv)
