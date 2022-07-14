last_semester_gradebook = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65],
]

# Your code below:

subjects = ["physics", "calculus", "poetry", "history"]
grades = [80, 96, 97, 65]

gradebook = [["physics", 80], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

print(gradebook)

gradebook[-1][-1] += 5

print(gradebook)

gradebook[2].remove(gradebook[2][1])
gradebook[2].append("Pass")

print(gradebook)
