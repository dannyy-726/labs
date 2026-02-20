def greet(name):
    print(f"Hello {name}!")

def farewell(name):
    print(f"Goodbye {name}!")

if __name__ == "__main__":
    print(f"Running {__file__}, name = {__name__}")
else:
    print(f"{__file__} is being imported, name = {__name__}")