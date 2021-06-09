import re


def arithmetic_arranger(problems, solution=False):
    arranged_problems_list = [str(), str(), str(), str()]
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in range(len(problems)):
        if len(re.findall("[+-]", problems[i])) != 1:
            return "Error: Operator must be '+' or '-'."
        if re.search("[^-+\d\s]", problems[0]) is not None:
            return "Error: Numbers must only contain digits."

        elements_list = re.findall("([0-9]+)\s*([+-])+\s*([0-9]+)", problems[i])
        first, operator, second = elements_list[0]
        result = str(int(first) + int(second)) if operator == '+' else str(int(first) - int(second))

        length_first = len(first)
        length_second = len(second)
        if length_first > 4 or length_second > 4:
            return "Error: Numbers cannot be more than four digits."

        if length_first > length_second:
            top = first.rjust(length_first + 2)
            bottom = operator + ' ' + second.rjust(length_first)
        elif length_first < length_second:
            top = first.rjust(length_second + 2)
            bottom = operator + ' ' + second
        else:
            top = '  ' + first
            bottom = operator + ' ' + second
        dashes = len(top) * '-'
        result_ = result.rjust(len(top))

        if i > 0:
            arranged_problems_list = [row + 4*' ' for row in arranged_problems_list]

        arranged_problems_list[0] += top
        arranged_problems_list[1] += bottom
        arranged_problems_list[2] += dashes
        arranged_problems_list[3] += result_

    if solution:
        arranged_problems = '\n'.join(arranged_problems_list)
        return arranged_problems
    arranged_problems = '\n'.join(arranged_problems_list[:-1])

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))