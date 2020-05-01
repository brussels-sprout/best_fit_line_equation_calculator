# best_fit_line_equation_calculator
# by brussels-sprout


def title():
    print("\033[1m" + "Best fit line equation calculator" + "\033[0;0m" + "\nby brussels-sprout\n")
    # weird things make it bold


def input_():  # todo fix bug
    total = input("Input the total number of points: ")
    try:
        i = float(total)
        if i == float("inf") or i == float("-inf") or not i.is_integer() or i <= 1:
            raise ValueError
    except ValueError:
        print("Please input a positive integer larger than one for the total number of points.\n")
        input_()
    dp = input("Input the number of decimal places to calculate result to: ")
    try:
        j = float(dp)
        if j == float("inf") or j == float("-inf") or not j.is_integer() or j <= 0:
            raise ValueError
    except ValueError:
        print("Please input a positive integer for the number of decimal places.\n")
        input_()
    total = int(total)
    dp = int(dp)
    points = []
    n = 0
    for i in range(total):
        print(f"\n--- Point {i + 1} ---")
        x = input("Input x coordinate: ")
        y = input("Input y coordinate: ")
        try:
            x = float(x)
            y = float(y)
            if x == float("inf") or x == float("-inf") or y == float("inf") or y == float("-inf"):
                raise ValueError
        except ValueError:
            print("Please input numbers for the coordinates.\n")
            input_()
        point = [x, y]
        points.append(point)
        n += 1
    if check_duplicates(points):
        print("Please do not input duplicate points.\n")
        input_()
    return points, dp


def check_duplicates(i):  # i is a list
    for j in i:
        if i.count(j) > 1:
            return True
    return False


def operation(points, dp):  # uses least square method
    sum_x = 0.0
    sum_y = 0.0
    list_x = []
    list_y = []
    for point in points:
        x = point[0]
        sum_x += x
        list_x.append(x)
        y = point[1]
        sum_y += y
        list_y.append(y)
    total = len(points)
    avg_x = sum_x / total
    avg_y = sum_y / total
    list_x_minus_avg = []
    list_y_minus_avg = []
    for x in list_x:
        list_x_minus_avg.append(x - avg_x)
    for y in list_y:
        list_y_minus_avg.append(y - avg_y)
    sum_square_list_x_minus_avg = 0.0
    sum_product_list_x_minus_avg_and_list_y_minus_avg = 0.0
    for i in range(total):
        sum_square_list_x_minus_avg += list_x_minus_avg[i] ** 2
        sum_product_list_x_minus_avg_and_list_y_minus_avg += list_x_minus_avg[i] * list_y_minus_avg[i]
    a = sum_product_list_x_minus_avg_and_list_y_minus_avg / sum_square_list_x_minus_avg
    b = avg_y - a * avg_x
    return round(a, dp), round(b, dp)


def end():
    if input("\nInput any character(s) to make a new calculation or simply press ENTER to exit: ") == "":
        print("\nDone.")
        exit()
    else:
        print("")
        main()


def main():
    try:
        result = operation(*input_())
        print(f"\nBest fit line equation: y = ({result[0]})x + ({result[1]})")
    except (OverflowError, MemoryError):
        print("\nNumbers too large.")
        main()
    end()


title()
main()
