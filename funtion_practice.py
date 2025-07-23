def welcome_messege():
    print("="*30)
    print("welcome to the grade calculator")
    print("="*30)



def get_test_scores():
    score1 = float(input("what is your first score "))
    score2 = float(input("what is your second score "))
    score3 = float(input("what is your third score "))
    print(f"your scores are {score1}, {score2} and {score3}")
    return score1, score2, score3




def calculator_averege(score1, score2, score3):
    
    averege = (score1 + score2 + score3)/3
    print (f"Your averge is {averege : .2f} ")

    return averege



def get_letter_grade(averege):
    if averege >= 90:
        letter_grade = "A"
        print("you got an A")
        return letter_grade
    elif averege >= 80:
        letter_grade = "B"
        print("you got an B")
        return letter_grade
    elif averege >= 70:
        letter_grade = "C"
        print("you got an C")
        return letter_grade
    else:
        letter_grade = "F"
        print("you got an F")

    
def display_reslult(score1, score2, score3, averege, letter_grade):
    print("\n Your results")
    print(f"Test 1: {score1}")
    print(f"Test 2: {score2}")
    print(f"Test 3: {score3}")
    print(f"Averge: {averege: .1f}")
    print(f"Grade: {letter_grade}")
    
def main():
    welcome_messege()
    score1, score2, score3 = get_test_scores()
    averege = calculator_averege(score1, score2, score3)
    letter_grade = get_letter_grade(averege)
    display_reslult(score1, score2, score3, averege, letter_grade)

if __name__ == "__main__":
    main()


