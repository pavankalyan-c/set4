def main():
    full_name = input("Please enter a  name: ").split()
    total = 0
    for z in full_name:
        total += len(z)
    print(total)
