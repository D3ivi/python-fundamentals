number = int(input())
total_sum = 0

for i in range(number):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")