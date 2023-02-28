


# FREEZE CODE BEGIN
import random
random.seed() # This makes random not random so that it can be tested.
# FREEZE CODE END

def isLucky(num):
    grad = False

    print("The student should be lucky: ")
    for i in range(num):
        a = random.randint(1, 6)
        print("Rolling the dice...", a)
        if a in [1, 2, 3, 4, 5]:
            continue
        elif a == 6:
            grad = True
            break
    return grad# Use random.randint(1, 6) as your dice


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
        highest = biology

    return highest


def averageGrade(math, english, physics, history, biology):
    average = (math + english + physics + history + biology) / 5

    return average


def evaluate(lowest, average, highest):

    new_lowest = lowest + 20
    if lowest >= 75:
        if average >= 85:
            if highest <= new_lowest:
                return True
            else:
                return isLucky(5)
        else:
            return False
    else:
        return False





def main():
    is_student_valid: bool = True
    while is_student_valid:
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

        graduation = evaluate(lowest, average, highest)

        if graduation == True:
            print("The student can graduate! ")
        elif graduation == False:
            print("The student cannot graduate! ")

        student_match = input("Do you want to continue? ")
        student_match = student_match[0]
        student_match = student_match.upper()

        if student_match in 'Y':
            is_student_valid = True
        else:
            is_student_valid = False


if __name__ == "__main__":  # This is important, do not delete it
    main()

# Print statement for the general grades expression