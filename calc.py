def main():
    print("Let's implement division.")
    x = int(input("x > "))
    y = int(input("y > "))
    print(f"{x} / {y} = {divide(x, y)}")

def divide(x, y):
    if y == 0:
        print("Error: cannot divide by zero.")
    else:
        return x/y
    
def add(x, y):
    return x+y