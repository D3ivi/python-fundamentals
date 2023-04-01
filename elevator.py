import math

num_people = int(input())
capacity = int(input())

course = math.ceil(num_people/capacity)

print(course)
