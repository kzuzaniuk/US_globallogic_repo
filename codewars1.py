# Someone was hacking the score. Each student's record is given as an array The objects in the array are given again as an array of scores for each name and total score. ex>

# array = [
# ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
# ["name2", 110, ["B", "A", "A", "A"]],
# ["name3", 200, ["B", "A", "A", "C"]],
# ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
# ]

# The scores for each grade is:

#     A: 30 points
#     B: 20 points
#     C: 10 points
#     D: 5 points
#     Everything else: 0 points

# If there are 5 or more courses and all courses has a grade of B or above, additional 20 points are awarded. After all the calculations, the total score should be capped at 200 points.

# Returns the name of the hacked name as an array when scoring with this rule. 

def find_hack(arr):
    hacked = []
    for array in arr:
        # if array[1] > 200:
        #     hacked.append(array[0])
        # print(array[1])
        temp_score = 0
        temp_array = []
        for l in array[2]:
            match l:
                case 'A':
                    temp_score += 30
                    temp_array.append(30)
                case 'B':
                    temp_score += 20
                    temp_array.append(20)
                case 'C':
                    temp_score += 10
                    temp_array.append(10)
                case 'D':
                    temp_score += 5
                    temp_array.append(5)
                case _:
                    temp_score += 0
                    temp_array.append(0)
        print(list(temp_array))
        if all(i >= 20 for i in temp_array) and len(temp_array) >= 5:
            temp_score += 20
        if temp_score > 200:
            temp_score = 200
        print(temp_score)
        if temp_score != array[1]:
            hacked.append(array[0])
    return hacked # hacked entries

#co można poprawić:
    #zamiast ifa sprawdzającego, czy przekracza 200, to może użyć jakiegoś clampa/max
    #zamiast tworzyć nową tabelę dla wartości dla poszczególnych liter, to może zrobić dictionary?
    #dwie pętle to sporo, pewnie można zrobić to łatwiej, może list/dict comprehension
    
#https://www.codewars.com/users/kzuzaniuk/completed 

array = [
["name1", 445, ["B", "A", "A", "C", "A", "A"]], # name1 total point is over 200 => hacked
["name2", 110, ["B", "A", "A", "A"]], #  name2 point is right
["name3", 200, ["B", "A", "A", "C"]], # name3 point is 200 but real point is 90 => hacked
["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]] # name4 point is right
]


print(list(find_hack(array)))