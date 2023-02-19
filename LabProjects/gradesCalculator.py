def minGrade(math, english, physics, history, biology):
    # if structure to find min
    lowest = math

    if english < lowest:
        lowest = english

    if physics < lowest:
        lowest = physics

    if history < lowest:
        lowest = history

    if biology < lowest:
        lowest = biology

    return lowest

def maxGrade(math, english, physics, history, biology):
    # if structure to find the maximum
    highest = math

    if english > highest:
        highest = english

    if physics > highest:
        highest = physics

    if history > highest:
        highest = history

    if biology > highest:
        highest = history

    return highest


def averageGrade(math, english, physics, history, biology):
    average = (math + english + physics + history + biology) / 5
    return average


def evaluate(lowest, average, highest):
    if average >= 85 and lowest >= 75 and highest < (lowest + 20):
        return True
    elif average >= 85 and lowest >= 75 and highest > (lowest + 20):
        a = isLucky(5)
        return a
    else:
        return False




def isLucky(num):
    import random

    grad = False

    print("The student should be lucky: ")
    for i in range(num):
        a = random.randint(1, 6)
        print("Rolling the dice...", a)
        if a == [1, 2, 3, 4, 5]:
            continue
        elif a == 6:
            grad = True
            break
    return grad


def main():
    # Print statement for the general grades expression
    print("""Enter Student’s Grades (0-100): """)

    # Input for the grades
    math = int(input("Math: "))
    english = int(input("English: "))
    physics = int(input("Physics: "))
    history = int(input("History: "))
    biology = int(input("Biology: "))

    lowest = minGrade(math, english, physics, history, biology)
    highest = maxGrade(math, english, physics, history, biology)
    average = averageGrade(math, english, physics, history, biology)

    graduation = evaluate(lowest, highest, average)

    if graduation == True:
        print("You will graduate! ")
    elif graduation == False:
        print("You will not graduate! ")


if __name__ == "__main__":  # This is important, do not delete it
    main()







