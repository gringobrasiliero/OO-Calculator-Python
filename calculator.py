import operator

ops = {"+": operator.add, "-": operator.sub, "/": operator.div, "*": operator.mul}
again = ""


def calc():
    calculation = input("What math equation are you trying to solve?")
    first_index = 0
    while calculation[first_index] not in "+-/*":
        first_index = first_index + 1

    first_num = int(calculation[:first_index])
    second_index = first_index + 1
    second_num = int(calculation[second_index:])
    operator = calculation[first_index:second_index]
    global answer
    answer = ops[operator](first_num, second_num)

    print(answer)


def again_again(answer):
    again = input("Do you have any other problems?")

    if again == "":
        return
    elif again[0] == "+" or again[0] == "-" or again[0] == "/" or again[0] == "*":
        num_three = int(again[1:])
        answer = ops[again[0]](answer, num_three)
        print(answer)
        again_again(answer)


def run_calc():
    while again == "":
        calc()
        again_again(answer)


run_calc()
