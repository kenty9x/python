def exception_handling(number1, number2, operator):
    try:
        int(number1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(number2)
    except:
        return "Error: Numbers must only contain digits."
    try:
        if len(number1) > 4 or len(number2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    try:
        if operator != '+' and operator != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""


def arithmetic_arranger(problems, show_result=False):
    first_item = True
    first_num = []
    sign = []
    second_num = []
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in problems:
        temp = i.split()
        first_num.append(temp[0])
        sign.append(temp[1])
        second_num.append(temp[2])
        exp = exception_handling(temp[0], temp[2], temp[1])
        if exp != "":
            return exp
        no1=int(temp[0])
        no2=int(temp[2])
        space=max(len(temp[0]), len(temp[2]))
        if first_item == True:
            line1 += temp[0].rjust(space+2)
            line2 += temp[1] + ' ' + temp[2].rjust(space)
            line3 += '-'*(space+2)
            if show_result == True:
                if temp[1] == '+':
                    line4 += str(no1+no2).rjust(space+2)
                else:
                    line4 += str(no1-no2).rjust(space+2)
            first_item = False
        else:
            line1 += temp[0].rjust(space+6)
            line2 += temp[1].rjust(5) + ' ' + temp[2].rjust(space)
            line3 += side_space+ '-'*(space+2)
            if show_result == True:
                if temp[1] == '+':
                    line4 += side_space+str(no1+no2).rjust(space+2)
                else:
                    line4 += side_space+str(no1-no2).rjust(space+2)
    if show_result == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3